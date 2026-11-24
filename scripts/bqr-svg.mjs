// A B-QR as an SVG for the drawings, painted by the brand layer's OWN recipe (brand/bqr.ts, vendored byte-identical, brand.lock):
// paintBqr runs against a small recording 2D context, so every number (the dot, the outline, the decoration, the owner's ink) is
// the recipe's, never a copy here. Run when a drawn link changes:
//   node --experimental-strip-types scripts/bqr-svg.mjs <text> <owner> <size px> <a folder whose node_modules has qrcode> [--open] [--heart] [--autograph strokes.json] > marks-bqr.svg
// Since v1.9.0 the recipe turns every code and draws the small TM itself (an autograph, Open only, takes its place).
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
const [text, owner, sizeArg, qrFrom] = process.argv.slice(2);
if (!text || !owner || !sizeArg || !qrFrom) throw new Error("usage: <text> <owner> <size> <qrcode folder>");
globalThis.Path2D = class { constructor(d) { this.d = d; } };
const { paintBqr, BQR_ECC } = await import("../brand/bqr.ts");
const QRCode = createRequire(new URL(qrFrom.replace(/\/?$/, "/"), "file://" + process.cwd() + "/"))("qrcode");
const size = Number(sizeArg), q = QRCode.create(text, { errorCorrectionLevel: BQR_ECC }), has = (f) => process.argv.includes(f), after = (f) => process.argv[process.argv.indexOf(f) + 1];
const out = [], defs = [];
let s = { fill: "#000", stroke: "#000", lw: 1, join: "miter", k: 1, tx: 0, ty: 0, open: 0 }, stack = [];
const r = (v) => +v.toFixed(3);
const tf = () => `matrix(${r(s.k)} 0 0 ${r(s.k)} ${r(s.tx)} ${r(s.ty)})`;
const g = {
    set fillStyle(v) { s.fill = v; }, set strokeStyle(v) { s.stroke = v; }, set lineWidth(v) { s.lw = v; }, set lineJoin(v) { s.join = v; }, set lineCap(v) { s.cap = v; },
    // the sign's M and an autograph's strokes are paths of their own
    beginPath() { s.p = ""; }, moveTo(x, y) { s.p += `M${r(x)} ${r(y)}`; }, lineTo(x, y) { s.p += `L${r(x)} ${r(y)}`; }, closePath() { s.p += "Z"; },
    quadraticCurveTo(a, b, x, y) { s.p += `Q${r(a)} ${r(b)} ${r(x)} ${r(y)}`; }, rect(x, y, w, h) { s.p += `M${r(x)} ${r(y)}h${r(w)}v${r(h)}h${r(-w)}Z`; },
    arc(x, y, q) { s.p += `M${r(x - q)} ${r(y)}a${q} ${q} 0 1 0 ${2 * q} 0a${q} ${q} 0 1 0 ${-2 * q} 0Z`; },
    save() { stack.push(s); s = { ...s, open: 0 }; },
    restore() { out.push("</g>".repeat(s.open)); s = stack.pop(); },
    translate(x, y) { s.tx += s.k * x; s.ty += s.k * y; }, scale(a) { s.k *= a; },
    clearRect() {},
    fillRect(x, y, w, h) { out.push(s.k === 1 && !s.tx && !s.ty ? `<rect x="${r(x)}" y="${r(y)}" width="${r(w)}" height="${r(h)}" fill="${s.fill}"/>` : `<rect x="${r(x)}" y="${r(y)}" width="${r(w)}" height="${r(h)}" fill="${s.fill}" transform="${tf()}"/>`); },
    fill(p = { d: s.p }) { out.push(`<path d="${p.d}" fill="${s.fill}" transform="${tf()}"/>`); },
    stroke(p = { d: s.p }) { out.push(`<path d="${p.d}" fill="none" stroke="${s.stroke}" stroke-width="${s.lw}" stroke-linejoin="${s.join}"${s.cap ? ` stroke-linecap="${s.cap}"` : ""} transform="${tf()}"/>`); },
    clip(p = { d: s.p }) { const id = `bqrc${defs.length}`; defs.push(`<clipPath id="${id}"><path d="${p.d}" transform="${tf()}"/></clipPath>`); out.push(`<g clip-path="url(#${id})">`); s.open++; },
};
paintBqr(g, q.modules, text, { size, owner, style: has("--open") ? "outline" : "pixels", ground: has("--heart") ? "heart" : "paper", ...(has("--autograph") ? { autograph: JSON.parse(readFileSync(after("--autograph"), "utf8")) } : {}) });
process.stdout.write(`<svg class="bqr" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" shape-rendering="crispEdges" aria-hidden="true"><defs>${defs.join("")}</defs>${out.join("")}</svg>\n`);
