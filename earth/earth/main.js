/**
 * The Earth prototype for earth.333.eco. Every number is made up, by the small simulation below, which keeps the one thing that matters: each Kiitos
 * adds one to one place and takes one from another, so the world sums to exactly zero on every day.
 *
 *   shape = amplitude: a crest where people have been kind, a trough where they have been thankful.
 *   color = frequency: the aura ramp, from how often a place's own balance has crossed zero (the published ƒ's buckets).
 *   the grain = the mesh: 980 triangles about 1,100 km across. No borders are drawn.
 */
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { mergeVertices } from "three/addons/utils/BufferGeometryUtils.js";
import { feature, mesh as topoMesh } from "topojson-client";
import land from "world-atlas/land-110m.json";

const FETCH = document.getElementById("earth").dataset.live === "1", LIVE = FETCH || location.search.includes("calm"); // calm: no made-up numbers, for the live page's still picture
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
const SEASON_DAYS = 42, STEP_MS = reduce ? 1e12 : 2600;
// The published ramp: brand.333.eco data/auras.json, in crossings a month.
const RAMP = [[0.5, "#dc2626"], [1.5, "#ea580c"], [3, "#ca8a04"], [6, "#16a34a"], [12, "#2563eb"], [24, "#4f46e5"], [Infinity, "#7c3aed"]].map(([u, c]) => [u, new THREE.Color(c)]);
const auraOf = (perMonth) => RAMP.find(([u]) => perMonth < u)[1];
const AURA = Object.fromEntries(["red", "orange", "yellow", "green", "blue", "indigo", "violet"].map((n, i) => [n, RAMP[i][1]]));
/** The real sea, once fetched: the last days, oldest first. */
let frames = [], sampleRun = false;

// ── seeded, so everyone reviews the same sea ──
let seed = 333;
const rand = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };

// ── the land, for a mask only ──
// A ring that goes all the way round (Antarctica) ends 360° from where it began: close it over the pole, or everything south of its coast reads as sea.
const closePole = (r) => { const f = r[0], l = r[r.length - 1]; if (Math.abs(l[0] - f[0]) < 359) return r; const pole = f[1] < 0 ? -90 : 90; return [...r, [l[0], pole], [f[0], pole], f]; };
const polys = feature(land, land.objects.land).features.flatMap((f) => f.geometry.type === "Polygon" ? [f.geometry.coordinates] : f.geometry.coordinates).map((raw) => {
    // ⚠️ A ring that crosses the 180° line jumps from +180 to -180: unwrap it, or an island in Fiji reads as a strip around the whole planet (founder saw a row of "hexagons" at 16°S, 2026-11-09). The jump along the South Pole's edge is real and stays.
    const rings = raw.map((r) => { let off = 0; return r.map(([x, y], i) => { if (i && Math.abs(y) < 89 && Math.abs(r[i - 1][1]) < 89) { const dx = x - r[i - 1][0]; if (dx > 180) off -= 360; else if (dx < -180) off += 360; } return [x + off, y]; }); }).map(closePole);
    let a = Infinity, b = -Infinity, c = 90, d = -90;
    for (const [x, y] of rings[0]) { a = Math.min(a, x); b = Math.max(b, x); c = Math.min(c, y); d = Math.max(d, y); }
    return { rings, a, b, c, d };
});
function inRing(r, x, y) { let on = false; for (let i = 0, j = r.length - 1; i < r.length; j = i++) { const [xi, yi] = r[i], [xj, yj] = r[j]; if ((yi > y) !== (yj > y) && x < ((xj - xi) * (y - yi)) / (yj - yi) + xi) on = !on; } return on; }
function isLand(lon, lat) { for (const p of polys) for (const x of [lon, lon + 360, lon - 360]) if (x >= p.a && x <= p.b && lat >= p.c && lat <= p.d && inRing(p.rings[0], x, lat) && !p.rings.slice(1).some((h) => inRing(h, x, lat))) return true; return false; }
const toLL = (v) => [(Math.atan2(v.x, v.z) * 180) / Math.PI, (Math.asin(THREE.MathUtils.clamp(v.y, -1, 1)) * 180) / Math.PI];
const fromLL = (lon, lat, r = 1) => { const a = (lon * Math.PI) / 180, b = (lat * Math.PI) / 180; return new THREE.Vector3(r * Math.cos(b) * Math.sin(a), r * Math.sin(b), r * Math.cos(b) * Math.cos(a)); };

// ── the 980 cells ──
const coarse = new THREE.IcosahedronGeometry(1, 6), cp = coarse.attributes.position, cells = [];
for (let i = 0; i < cp.count; i += 3) {
    const a = new THREE.Vector3().fromBufferAttribute(cp, i), b = new THREE.Vector3().fromBufferAttribute(cp, i + 1), c = new THREE.Vector3().fromBufferAttribute(cp, i + 2);
    const d = a.clone().add(b).add(c).normalize();
    cells.push({ d, land: isLand(...toLL(d)) });
}
const nearestCell = (v) => { let best = -1, bd = -2; for (let i = 0; i < cells.length; i++) { const q = cells[i].d.dot(v); if (q > bd) { bd = q; best = i; } } return best; };

// ── made-up people: placed around where people live, plus some who said nothing and so sit in the open sea ──
const towns = [[104.9, 11.6], [103.8, 13.4], [-118.2, 33.8], [-119.8, 36.7], [100.5, 13.8], [106.7, 10.8], [139.7, 35.7], [121.5, 31.2], [77.2, 28.6], [72.9, 19.1], [90.4, 23.8], [-0.1, 51.5], [2.4, 48.9], [13.4, 52.5], [37.6, 55.8], [31.2, 30.0], [3.4, 6.5], [36.8, -1.3], [28.0, -26.2], [-46.6, -23.5], [-58.4, -34.6], [-99.1, 19.4], [-74.0, 40.7], [-79.4, 43.7], [151.2, -33.9], [174.8, -36.9], [126.9, 37.6], [120.9, 14.6], [106.8, -6.2], [55.3, 25.3]];
const placed = [...new Set(towns.flatMap(([x, y]) => { const c = nearestCell(fromLL(x, y)); return [c, nearestCell(fromLL(x + (rand() - 0.5) * 14, y + (rand() - 0.5) * 10))]; }))];
const open = cells.map((c, i) => (!c.land ? i : -1)).filter((i) => i >= 0).sort(() => rand() - 0.5).slice(0, 5);
const live = [...placed, ...open];
const series = LIVE ? { kiitos: new Map(), kiitti: new Map() } : { kiitos: new Map(live.map((c) => [c, [0]])), kiitti: new Map(placed.map((c) => [c, [0]])) };
const crossings = (s, upto) => { let n = 0; for (let i = 1; i <= upto; i++) if ((s[i - 1] > 0 && s[i] <= 0) || (s[i - 1] < 0 && s[i] >= 0)) n++; return n; };
for (let d = 1; !LIVE && d < SEASON_DAYS; d++) {
    for (const s of series.kiitos.values()) s.push(s.at(-1));
    for (const s of series.kiitti.values()) s.push(s.at(-1));
    for (let m = 0; m < 26; m++) { const a = live[Math.floor(rand() * live.length)], b = live[Math.floor(rand() * live.length)]; if (a === b) continue; series.kiitos.get(a)[d]++; series.kiitos.get(b)[d]--; }
    for (let m = 0; m < 18; m++) { const a = placed[Math.floor(rand() * placed.length)]; series.kiitti.get(a)[d] += rand() < 0.62 ? 1 : -1; }
}

// ── the field: one sample per direction, for one sea on one day ──
const SIG = 2 * 0.13 * 0.13, TINT = 2 * 0.085 * 0.085, WIDE = 2 * 0.3 * 0.3;
function stateOf(sea, day) {
    if (LIVE) { const list = (frames[day]?.seas[sea] ?? []).map((x) => ({ d: fromLL(x.lon, x.lat), b: x.b, rgb: AURA[x.a] ?? AURA.red })); return { list, top: Math.max(4, ...list.map((x) => Math.abs(x.b))) }; }
    const list = [...series[sea]].map(([c, s]) => ({ d: cells[c].d, b: s[day], rgb: auraOf(day ? (crossings(s, day) / day) * 30 : 0) }));
    return { list, top: Math.max(4, ...list.map((x) => Math.abs(x.b))) };
}
function fill(state, count, dir, H, A, P, C) {
    const n = state.list.length, px = new Float32Array(n), py = new Float32Array(n), pz = new Float32Array(n), pb = new Float32Array(n);
    state.list.forEach((x, i) => { px[i] = x.d.x; py[i] = x.d.y; pz[i] = x.d.z; pb[i] = x.b / state.top; });
    for (let v = 0; v < count; v++) {
        const X = dir[v * 3], Y = dir[v * 3 + 1], Z = dir[v * 3 + 2];
        let h = 0, w = 0, best = -1, top = null, near = 9, amp = 0;
        for (let i = 0; i < n; i++) {
            const d2 = 2 - 2 * (X * px[i] + Y * py[i] + Z * pz[i]);
            if (d2 > 0.9) continue;
            const k = Math.exp(-d2 / SIG), t = Math.exp(-d2 / TINT);
            h += pb[i] * k;
            w += t; if (t > best) { best = t; top = state.list[i].rgb; } // the strongest area's own color: mixing the ramp's ends makes pink, which is reserved
            if (d2 < near) { near = d2; amp = Math.abs(pb[i]) * Math.exp(-d2 / WIDE); }
        }
        H[v] = h; A[v] = amp; P[v] = near > 8 ? 0 : Math.sqrt(near);
        if (top) { C[v * 4] = top.r; C[v * 4 + 1] = top.g; C[v * 4 + 2] = top.b; C[v * 4 + 3] = Math.min(1, w * 1.15); } else C[v * 4 + 3] = 0;
    }
}

// ── the scene ──
const canvas = document.getElementById("earth");
let renderer;
try { renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, preserveDrawingBuffer: true }); }
catch (e) { // A phone that cannot draw this gets the Earth as a picture (found by real Android Chrome at the floor, 2026-11-08).
    document.documentElement.classList.add("no-gl");
    throw e;
}
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
const scene = new THREE.Scene(), camera = new THREE.PerspectiveCamera(32, 1, 0.1, 50), globe = new THREE.Group();
camera.position.set(0, 0.5, 4.6);
globe.rotation.z = THREE.MathUtils.degToRad(-23.4);
scene.add(globe);
const uniforms = { uT: { value: 0 }, uMix: { value: 1 }, uOcean: { value: new THREE.Color() }, uLand: { value: new THREE.Color() }, uInk: { value: new THREE.Color() }, uSea: { value: 0 } };
const carry = `attribute float aH0, aH1, aA0, aA1, aP0, aP1; uniform float uT, uMix, uSea;
float lift(vec3 p){ float h=mix(aH0,aH1,uMix), a=mix(aA0,aA1,uMix), q=mix(aP0,aP1,uMix); return 0.15*h + 0.014*a*sin(q*30.0-uT*1.4) + uSea; }`;
const surface = new THREE.ShaderMaterial({
    uniforms,
    vertexShader: `${carry} attribute float aLand; attribute vec4 aC0, aC1; varying vec3 vP; varying float vLand; varying vec4 vC;
      void main(){ vec3 p=position*(1.0+lift(position)); vP=(modelViewMatrix*vec4(p,1.0)).xyz; vLand=aLand; vC=mix(aC0,aC1,uMix); gl_Position=projectionMatrix*vec4(vP,1.0); }`,
    fragmentShader: `uniform vec3 uOcean,uLand; varying vec3 vP; varying float vLand; varying vec4 vC;
      void main(){ vec3 n=normalize(cross(dFdx(vP),dFdy(vP))); float l=0.42+0.68*pow(max(0.0,dot(n,normalize(vec3(-0.45,0.65,0.62)))),1.3);
        vec3 base=mix(uOcean,uLand,vLand); vec3 c=mix(base,vC.rgb,vC.a*0.92); gl_FragColor=vec4(c*l,1.0);
#include <colorspace_fragment>
      }`,
});
const lineMat = (opacity) => new THREE.ShaderMaterial({
    uniforms: { ...uniforms, uAlpha: { value: opacity } }, transparent: true, depthWrite: false,
    vertexShader: `${carry} uniform float uOut; void main(){ vec3 p=position*(1.006+lift(position)); gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0); }`,
    fragmentShader: `uniform vec3 uInk; uniform float uAlpha; void main(){ gl_FragColor=vec4(uInk,uAlpha);
#include <colorspace_fragment>
      }`,
});

function body(geometry, extra) {
    const count = geometry.attributes.position.count, dir = geometry.attributes.position.array;
    const parts = { count, dir, H: [new Float32Array(count), new Float32Array(count)], A: [new Float32Array(count), new Float32Array(count)], P: [new Float32Array(count), new Float32Array(count)], C: [new Float32Array(count * 4), new Float32Array(count * 4)] };
    for (const i of [0, 1]) {
        geometry.setAttribute(`aH${i}`, new THREE.BufferAttribute(parts.H[i], 1).setUsage(THREE.DynamicDrawUsage));
        geometry.setAttribute(`aA${i}`, new THREE.BufferAttribute(parts.A[i], 1).setUsage(THREE.DynamicDrawUsage));
        geometry.setAttribute(`aP${i}`, new THREE.BufferAttribute(parts.P[i], 1).setUsage(THREE.DynamicDrawUsage));
        geometry.setAttribute(`aC${i}`, new THREE.BufferAttribute(parts.C[i], 4).setUsage(THREE.DynamicDrawUsage));
    }
    return Object.assign(parts, { geometry }, extra);
}

const fine = mergeVertices(new THREE.IcosahedronGeometry(1, 30).deleteAttribute("uv").deleteAttribute("normal"));
for (let i = 0; i < fine.attributes.position.count; i++) { const v = new THREE.Vector3().fromBufferAttribute(fine.attributes.position, i).normalize(); fine.attributes.position.setXYZ(i, v.x, v.y, v.z); }
const mask = new Float32Array(fine.attributes.position.count);
for (let i = 0; i < mask.length; i++) mask[i] = isLand(...toLL(new THREE.Vector3().fromBufferAttribute(fine.attributes.position, i))) ? 1 : 0;
fine.setAttribute("aLand", new THREE.BufferAttribute(mask, 1));
globe.add(new THREE.Mesh(fine, surface));

// The coasts, the only lines of geography on this Earth. No borders are drawn.
const coastPts = []; for (const line of topoMesh(land, land.objects.land).coordinates) for (let i = 0; i + 1 < line.length; i++) { const a = fromLL(...line[i]), b = fromLL(...line[i + 1]); coastPts.push(a.x, a.y, a.z, b.x, b.y, b.z); }
const coast = new THREE.BufferGeometry().setAttribute("position", new THREE.Float32BufferAttribute(coastPts, 3));
const coastMat = lineMat(0.55); globe.add(new THREE.LineSegments(coast, coastMat));

const bodies = [body(fine), body(coast)];
let sea = "kiitos", day = 0;
function sumOf(s, d) { if (LIVE) return frames[d]?.sums[s] ?? 0; let t = 0; for (const x of series[s].values()) t += x[d]; return t; }
const frameCount = () => (LIVE ? Math.max(1, frames.length) : SEASON_DAYS);
function load(slot, d) { const st = stateOf(sea, d); for (const b of bodies) { fill(st, b.count, b.dir, b.H[slot], b.A[slot], b.P[slot], b.C[slot]); for (const n of [`aH${slot}`, `aA${slot}`, `aP${slot}`, `aC${slot}`]) b.geometry.attributes[n].needsUpdate = true; } }
// Whatever is not shown on land sits in the open sea, which takes the mirror of it, so the world still sums to zero.
function seaLevel(d) { return (-sumOf(sea, d) / Math.max(1, stateOf(sea, d).top * 12)) * 0.15; }

// ── what a person sees and does ──
const controls = new OrbitControls(camera, canvas);
Object.assign(controls, { enableDamping: true, dampingFactor: 0.07, enablePan: false, minDistance: 2.5, maxDistance: 7, autoRotate: !reduce, autoRotateSpeed: 0.55 });
const $ = (id) => document.getElementById(id);
const say = (l) => document.documentElement.dataset.lang === "km" ? l[1] : l[0];
const fmt = (n) => (n > 0 ? "+" : n < 0 ? "−" : "") + Math.abs(n);
function paint() {
    $("day").textContent = LIVE ? (sampleRun ? say(["Day ", "ថ្ងៃទី "]) + (day + 1) : (frames[day]?.day ?? "")) : say(["Day ", "ថ្ងៃទី "]) + (day + 1);
}
function goto(d, instant) { load(0, day); load(1, d); day = d; uniforms.uMix.value = instant ? 1 : 0; uniforms.uSea.value = seaLevel(d); paint(); }
$("sea").addEventListener("click", (e) => { const b = e.target.closest("button"); if (!b) return; sea = b.dataset.sea; document.querySelectorAll("#sea button").forEach((x) => x.classList.toggle("on", x === b)); $("card").hidden = true; goto(day, true); });
document.addEventListener("langchange", paint);
// Tiny stars behind the Earth, each blinking at its own pace; still under reduced motion.
const starN = 3200, starP = new Float32Array(starN * 3), starA = new Float32Array(starN), starS = new Float32Array(starN);
for (let i = 0; i < starN; i++) { const v = new THREE.Vector3(rand() * 2 - 1, rand() * 2 - 1, rand() * 2 - 1).normalize().multiplyScalar(30); starP.set([v.x, v.y, v.z], i * 3); starA[i] = rand() * 6.28; starS[i] = rand(); }
const starGeo = new THREE.BufferGeometry().setAttribute("position", new THREE.BufferAttribute(starP, 3)).setAttribute("aP", new THREE.BufferAttribute(starA, 1)).setAttribute("aS", new THREE.BufferAttribute(starS, 1));
const starUni = { uT: uniforms.uT, uStar: { value: new THREE.Color() }, uBright: { value: 1 }, uDpr: { value: renderer.getPixelRatio() } };
scene.add(new THREE.Points(starGeo, new THREE.ShaderMaterial({ uniforms: starUni, transparent: true, depthWrite: false,
    vertexShader: `attribute float aP, aS; uniform float uT, uDpr; varying float vB; void main(){ vB=0.28+0.72*pow(abs(sin(uT*(0.35+aS*1.1)+aP)),2.0); gl_PointSize=(6.0+aS*aS*11.0)*uDpr; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`,
    fragmentShader: `uniform vec3 uStar; uniform float uBright; varying float vB; void main(){ vec2 p=(gl_PointCoord-0.5)*2.0; float l=length(p); if(l>1.0) discard; float cross=smoothstep(0.05,0.0,abs(p.x)*abs(p.y))*smoothstep(1.0,0.12,l); float core=smoothstep(0.2,0.0,l); gl_FragColor=vec4(uStar,max(cross,core)*vB*uBright);
#include <colorspace_fragment>
    }` })));
const applyTheme = () => {
    const dark = document.documentElement.dataset.theme === "dark";
    uniforms.uOcean.value.set(dark ? "#10234a" : "#bcd0ee"); uniforms.uLand.value.set(dark ? "#3b4763" : "#f2eee2"); uniforms.uInk.value.set(dark ? "#d5def0" : "#26365a"); starUni.uStar.value.set(dark ? "#ffffff" : "#26365a"); starUni.uBright.value = dark ? 1 : 0.45;
};
document.addEventListener("themechange", applyTheme); applyTheme();

const ray = new THREE.Raycaster(), ptr = new THREE.Vector2(), sphere = new THREE.Sphere(new THREE.Vector3(), 1);
let down = null;
canvas.addEventListener("pointerdown", (e) => { down = [e.clientX, e.clientY]; });
canvas.addEventListener("pointerup", (e) => {
    if (!down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 6) return;
    const box = canvas.getBoundingClientRect(); ptr.set(((e.clientX - box.left) / box.width) * 2 - 1, -((e.clientY - box.top) / box.height) * 2 + 1);
    ray.setFromCamera(ptr, camera); const hit = ray.ray.intersectSphere(sphere, new THREE.Vector3());
    const at = hit ? globe.worldToLocal(hit).normalize() : null;
    let k, t;
    if (LIVE) {
        const near = (list) => { if (!at) return undefined; let best, bd = Math.cos((1.6 * Math.PI) / 180); for (const x of list) { const q = fromLL(x.lon, x.lat).dot(at); if (q > bd) { bd = q; best = x; } } return best?.b; };
        k = near(frames[day]?.seas.kiitos ?? []); t = near(frames[day]?.seas.kiitti ?? []);
    } else { const c = at ? nearestCell(at) : -1; k = series.kiitos.get(c)?.[day]; t = series.kiitti.get(c)?.[day]; }
    if (k === undefined && t === undefined) { $("card").hidden = true; return; }
    const dash = "\u2014";
    $("card-k").textContent = k === undefined ? dash : fmt(k); $("card-t").textContent = t === undefined ? dash : fmt(t); $("card").hidden = false;
});

let seenW = 0, seenH = 0, seenFit = 0;
/** Fits the whole Earth inside the shorter side. ⚠️ iPhone Safari reports its new size late when the phone turns, so this runs every frame and acts only on a real change (founder: cut off in landscape, 2026-11-09). */
// On the site the globe has its own band between the words and the legend, whatever the phone's height; the prototype has none and uses the whole canvas.
const band = document.querySelector(".g-band");
let seenBand = "";
function resize() {
    const w = canvas.clientWidth, h = canvas.clientHeight, b = band?.getBoundingClientRect(), bandTop = b ? b.top - canvas.getBoundingClientRect().top : 0, bandH = b ? b.height : h, key = `${Math.round(bandTop)}:${Math.round(bandH)}`;
    if (!w || !h || (w === seenW && h === seenH && key === seenBand)) return;
    seenW = w; seenH = h; seenBand = key;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    const halfV = THREE.MathUtils.degToRad(camera.fov / 2), half = Math.atan((Math.min(bandH, w) / h) * Math.tan(halfV)), fit = 1.2 / Math.sin(half);
    if (Math.abs(fit - seenFit) / fit > 0.02) { seenFit = fit; camera.position.setLength(fit); controls.minDistance = fit * 0.55; controls.maxDistance = fit * 1.5; }
    camera.setViewOffset(w, h, 0, band ? h / 2 - (bandTop + bandH / 2) : w < h ? h * 0.03 : 0, w, h);
    camera.updateProjectionMatrix();
}
addEventListener("resize", resize); resize();
goto(LIVE ? 0 : 24, true);
if (FETCH) fetch("/ledger/days.json").then((r) => r.json()).then((j) => { frames = j.days ?? []; sampleRun = !!j.sample; const o = $("opens"), n = $("sample"); if (o) o.hidden = frames.length > 0 || sampleRun; if (n) n.hidden = !sampleRun; if (frames.length) goto(frames.length - 1, true); }).catch(() => { /* the calm sea stays */ });
let last = performance.now(), hold = 0;
function frame(now) {
    const dt = now - last; last = now; hold += dt;
    uniforms.uT.value = reduce ? 0 : now / 1000;
    if (uniforms.uMix.value < 1) uniforms.uMix.value = Math.min(1, uniforms.uMix.value + dt / 1500);
    if (hold > STEP_MS && frameCount() > 1) { hold = 0; goto((day + 1) % frameCount()); }
    resize(); controls.update(); renderer.render(scene, camera); requestAnimationFrame(frame);
}
if (reduce) { if (!LIVE) goto(28, true); controls.autoRotate = false; }
if (location.search.includes("still")) { document.documentElement.classList.add("still"); controls.autoRotate = false; if (!LIVE) goto(24, true); uniforms.uMix.value = 1; }
requestAnimationFrame(frame);
window.__earth = { check: () => ({ kiitosZero: Array.from({ length: SEASON_DAYS }, (_, d) => sumOf("kiitos", d)).every((x) => x === 0), cells: cells.length, placed: placed.length, seaDays: SEASON_DAYS }) };
