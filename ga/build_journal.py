"""Journal-style graphical abstracts for the site themes (three cards + process strip).

The site introduces the research in general terms, so the panels carry concepts rather than
statistics: chart SHAPES (forest, lollipops, dumbbells, donut) are still drawn from the sourced
values listed below, but numeric labels, accessions and P values are deliberately left out.
Anything that is not data (tree shape, mini heatmap) is labelled "schematic" in the panel.
The fully numeric version is kept next to this file as build_journal_numeric.py (not rendered).

  j1  Kim SC et al., Adv Sci 2022;9(5):e2103360 (PMC8844556): 12 patients, 3-4 regions
      (S1-S4), 43 subregional PDOs + 23 PDCs, WES + RNA-seq, 24 drugs, 13 drugs with
      heterogeneous responses (named in Results 2.4), Treeomics trunk/shared/individual,
      SNU-4849 trunk APC/TP53/ARID1A at VAF ~0.95, Table 1 MSI status (8 MSS, 2 MSI-L, 2 MSI-H).
  j3  /data/data/SNUH_KMJ/ebiomedicine_revised/01_manuscript/manuscript_FINAL.md (2026-09-19):
      sample n (Results 1), genus prevalence saliva vs stool (Results 2), 25/75 detected,
      stage counts 5/18 6/18 5/20 2/7 P=0.95, M2 d=+0.440 q=0.028, neutrophil d=+0.430 q=0.028
      (n=63), plasma variant load d=-0.447 P=0.034 (n=42), M2 vs load rho=-0.465 P=2.3e-4 (n=59).
"""
from pathlib import Path
import math

HERE = Path(__file__).parent
W = 1200
BG = "#F7F5F0"; INK = "#1b1f1e"; GRAY = "#4a4f4d"; MUTE = "#7b827f"; LINE = "#dcd8cd"
TEAL = "#0a7d6e"; CORAL = "#c53e1f"; NAVY = "#1f4e79"; GREEN = "#2f7d55"; MAROON = "#8d2b3f"; SLATE = "#3d4446"
RC = ["#2f6db5", "#8a4fb0", "#d9971a", "#d1477a"]
RL = ["#c9d9ee", "#dfcdec", "#f5e2b8", "#f3cbda"]

def T(x, y, s, size=13, fill=INK, anchor="start", weight="normal", style="normal", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}" font-style="{style}" {extra}>{s}</text>')

def card(x, y, w, h, title):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="{LINE}" stroke-width="1.2"/>'
            + T(x + w / 2, y + 32, title, 15.5, INK, "middle", "bold"))

def arrow(x, y, w=22, col=SLATE):
    return (f'<path d="M{x} {y}h{w-7}" stroke="{col}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
            f'<path d="M{x+w-9} {y-5.5}l9 5.5-9 5.5z" fill="{col}"/>')

def stat(x, y, w, h, col, big, l1, l2, bigsize=23, split=112):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#fff" stroke="{col}" stroke-width="1.8"/>'
            f'<path d="M{x+9} {y}h-0a9 9 0 0 0-9 9v{h-18}a9 9 0 0 0 9 9z" fill="{col}"/>'
            + T(x + 22, y + h / 2 + bigsize * .36, big, bigsize, col, "start", "bold")
            + T(x + split, y + h / 2 - 3, l1, 13, INK)
            + T(x + split, y + h / 2 + 15, l2, 11.5, GRAY))

def chips(x, y, wmax, items, size=11.3, pitch=24):
    out, px, py = "", x, y
    for it in items:
        ww = len(it) * size * .56 + 18
        if px + ww > x + wmax:
            px = x; py += pitch
        out += f'<rect x="{px:.1f}" y="{py}" width="{ww:.1f}" height="19" rx="9.5" fill="#f1efe8" stroke="{LINE}"/>' + T(px + ww / 2, py + 13.5, it, size, INK, "middle")
        px += ww + 6
    return out

def head(title, sub):
    return T(W / 2, 46, title, 22.5, INK, "middle", "bold") + T(W / 2, 74, sub, 15.5, GRAY, "middle")

def strip(y, h, label, col=GREEN, fill="#EEF3EE"):
    return (f'<rect x="24" y="{y}" width="{W-48}" height="{h}" rx="12" fill="{fill}" stroke="{col}" stroke-width="1.5"/>'
            + T(48, y + 25, label, 13.5, col, "start", "bold"))

def wrap(body, h, sid):
    return (f'<section class="ja" id="{sid}" style="width:{W}px;height:{h}px">'
            f'<svg viewBox="0 0 {W} {h}" width="{W}" height="{h}" font-family="Arial, \'Liberation Sans\', Helvetica, sans-serif">'
            f'<rect width="{W}" height="{h}" fill="{BG}"/>{body}</svg></section>')

def badge(cx, cy, i, r=11, label=None):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{RC[i]}" stroke="#fff" stroke-width="2"/>'
            + T(cx, cy + 3.8, label or f"S{i+1}", 10.5, "#fff", "middle", "bold"))

# =====================================================================  J1
def j1():
    H = 640; CY = 100; CH = 392
    o = head("Regions of a single colon tumor yield organoids that respond differently to the same drugs",
             "multifocal organoid capturing of colon cancer  ·  genome, transcriptome and drug response read in every region")
    # ---------------- card 1: sampling
    x1, w1 = 24, 306
    o += card(x1, CY, w1, CH, "Multifocal sampling of one tumor")
    BLOB = [(262,152,46),(330,130,58),(412,122,64),(495,128,58),(562,120,60),(640,134,56),(712,152,46),(370,166,40),(610,170,40),(487,166,45)]
    circ = lambda extra: "".join(f'<circle cx="{x}" cy="{y}" r="{r}" {extra}/>' for x, y, r in BLOB)
    s = .465; tx = x1 + w1 / 2 - 487 * s; ty = CY + 50 - 56 * s
    o += (f'<g transform="translate({tx:.1f},{ty:.1f}) scale({s})" stroke="{INK}" stroke-width="3.4" stroke-linejoin="round">'
          f'<clipPath id="j1clip">{circ("")}</clipPath>'
          f'<rect x="196" y="182" width="582" height="42" rx="21" fill="#e0a284" stroke="#b0714f" stroke-width="3"/>'
          f'<g>{circ(chr(102)+"ill=\'#fff\'")}</g><g stroke="none">{circ(chr(102)+"ill=\'#fff\'")}</g>'
          f'<g clip-path="url(#j1clip)" stroke="none"><rect x="180" y="40" width="620" height="200" fill="{RL[0]}"/>'
          f'<path d="M340 40c-14 60 18 110-6 200h470V40z" fill="{RL[1]}"/><path d="M486 40c16 70-16 120 4 200h320V40z" fill="{RL[2]}"/>'
          f'<path d="M640 40c-16 66 14 124-4 200h170V40z" fill="{RL[3]}"/>'
          f'<g fill="none" stroke="#fff" stroke-width="3.4"><path d="M340 40c-14 60 18 110-6 200"/><path d="M486 40c16 70-16 120 4 200"/><path d="M640 40c-16 66 14 124-4 200"/></g></g></g>')
    cols = [x1 + 45 + k * 72 for k in range(4)]
    for k, (bx, by) in enumerate([(262,150),(412,128),(562,126),(712,150)]):
        o += badge(tx + bx * s, ty + by * s, k)
    o += T(x1 + w1 / 2, CY + 172, "one primary tumor, several regions sampled", 12, GRAY, "middle")
    ORG = [[(38,27,11,0),(70,24,9,0),(84,38,8,0),(56,40,6,0)],
           [(34,28,6,0),(50,23,5,0),(64,30,6,0),(80,25,5,0),(90,37,5,0),(46,40,5,0),(70,41,5,0)],
           [(40,28,9,1),(66,25,8,1),(84,37,7,1),(56,40,6,1)],
           [(36,28,9,0),(62,24,6,1),(82,32,10,0),(54,40,5,1),(70,42,4,0)]]
    for k, cx in enumerate(cols):
        o += f'<path d="M{cx} {CY+184}v18" stroke="{RC[k]}" stroke-width="2.4" fill="none"/><path d="M{cx-5} {CY+200}l5 8 5-8z" fill="{RC[k]}"/>'
        d = .52
        o += (f'<g transform="translate({cx-62*d:.1f},{CY+212}) scale({d})" stroke="{INK}" stroke-width="3.2">'
              f'<path fill="#fff" d="M2 30v11c0 11.1 26.9 20 60 20s60-8.9 60-20V30"/><ellipse cx="62" cy="30" rx="60" ry="20" fill="#fff"/>'
              f'<ellipse cx="62" cy="30" rx="50" ry="15.5" fill="{RL[k]}" stroke="none" opacity=".8"/>')
        for (px, py, r, f) in ORG[k]:
            o += (f'<circle cx="{px}" cy="{py}" r="{r}" fill="{RC[k]}" stroke="#fff" stroke-width="1.6"/>' if f else
                  f'<circle cx="{px}" cy="{py}" r="{r}" fill="#fff" stroke="{RC[k]}" stroke-width="{max(2.6, r*.42):.1f}"/>')
        o += '</g>'
    o += T(x1 + w1 / 2, CY + 266, "each region grown as its own", 11.5, GRAY, "middle")
    o += T(x1 + w1 / 2, CY + 281, "organoid (PDO) and cell line (PDC)", 11.5, GRAY, "middle")
    yy1 = CY + 308
    o += f'<path d="M{x1+28} {yy1-10}h{w1-56}" stroke="{LINE}" stroke-width="1.2"/>'
    o += T(x1 + 28, yy1 + 10, "read in every model", 12.5, INK, "start", "bold")
    o += chips(x1 + 28, yy1 + 22, w1 - 56, ["whole-exome", "RNA-seq", "histology", "drug panel"])

    # ---------------- card 2: trunk / branches / response
    x2, w2 = 360, 436
    o += arrow(x1 + w1 + 4, CY + CH / 2)
    o += card(x2, CY, w2, CH, "Shared trunk, private branches, divergent response")
    # tree (schematic), Treeomics classes coloured as in the paper
    TR, SH, IN = "#e08a2b", "#3f78c0", "#3f9a5c"
    gx, gy = x2 + 108, CY + 236
    tips = [gx - 75, gx - 27, gx + 27, gx + 75]
    o += f'<g fill="none" stroke-linecap="round" stroke-width="5">'
    o += f'<path d="M{gx} {gy}v-62" stroke="{TR}" stroke-width="9"/>'
    o += f'<path d="M{gx} {gy-62}L{gx-51} {gy-100}" stroke="{SH}"/><path d="M{gx} {gy-62}L{gx+51} {gy-100}" stroke="{SH}"/>'
    for k, tx_ in enumerate(tips):
        nx = gx - 51 if k < 2 else gx + 51
        o += f'<path d="M{nx} {gy-100}L{tx_} {gy-140}" stroke="{IN}"/>'
    o += '</g>'
    for k, tx_ in enumerate(tips):
        o += badge(tx_, gy - 150, k)
    o += f'<circle cx="{gx}" cy="{gy+4}" r="6" fill="#fff" stroke="{TR}" stroke-width="3"/>'
    o += T(gx - 12, gy + 8, "normal", 10.8, MUTE, "end")
    o += T(gx + 13, gy - 36, "driver mutations", 11.8, INK, "start", "bold")
    o += T(gx + 13, gy - 21, "sit in the trunk", 11.8, INK, "start", "bold")
    for k, (col, name) in enumerate([(TR, "trunk"), (SH, "shared"), (IN, "individual")]):
        lx = x2 + 22 + k * 72
        o += f'<path d="M{lx} {CY+266}h16" stroke="{col}" stroke-width="5" stroke-linecap="round"/>' + T(lx + 22, CY + 270, name, 11.5, GRAY)
    o += T(x2 + 22, CY + 60, "somatic mutations (whole exome)", 11.5, GRAY)
    # schematic response grid
    hx, hy = x2 + 268, CY + 84
    HEAT = ["#0a7d6e", "#7fbfb3", "#e6ebe9", "#e9a18d", "#c53e1f"]
    HM = [[0,0,1,0],[0,3,1,4],[1,0,4,2],[4,3,4,4],[2,4,0,1]]
    o += T(x2 + 262, CY + 60, "drug response (schematic)", 11.5, GRAY)
    for k in range(4):
        o += badge(hx + 17 + k * 38, hy, k, 10)
    for r in range(5):
        for k in range(4):
            o += f'<rect x="{hx + k*38}" y="{hy + 18 + r*24}" width="34" height="20" rx="3" fill="{HEAT[HM[r][k]]}"/>'
    for k, c in enumerate(HEAT):
        o += f'<rect x="{hx + 18 + k*23}" y="{hy+148}" width="23" height="8" fill="{c}"/>'
    o += T(hx + 75, hy + 172, "sensitive  →  resistant", 10.5, GRAY, "middle")
    # real drug names
    yy = CY + 292
    o += f'<path d="M{x2+22} {yy-8}h{w2-44}" stroke="{LINE}" stroke-width="1.2"/>'
    o += T(x2 + 22, yy + 12, "Response diverged for targeted drugs and chemotherapy alike", 12.2, INK, "start", "bold")
    o += chips(x2 + 22, yy + 26, w2 - 44, ["EGFR · MEK inhibitors", "PI3K · mTOR inhibitors", "fluoropyrimidines",
                                          "oxaliplatin · irinotecan", "HDAC inhibitor", "multikinase inhibitor"])

    # ---------------- card 3: numbers
    x3, w3 = 826, 350
    o += arrow(x2 + w2 + 4, CY + CH / 2)
    o += card(x3, CY, w3, CH, "What multiregion models show")
    sy = CY + 52; sh = 70; gap = 9
    o += stat(x3 + 16, sy, w3 - 32, sh, GREEN, "biobank", "a living model of every region", "organoids and cell lines, shared", 20, 122)
    o += stat(x3 + 16, sy + 2 * (sh + gap), w3 - 32, sh, CORAL, "branches", "private mutations per region", "and a different drug response", 20, 122)
    o += stat(x3 + 16, sy + (sh + gap), w3 - 32, sh, "#c9771c", "trunk", "drivers shared by all regions", "the common target", 20, 122)
    o += stat(x3 + 16, sy + 3 * (sh + gap), w3 - 32, sh, NAVY, "faithful", "histology, genome, expression", "of the parent tumor are kept", 20, 122)
    o += T(x3 + w3 / 2, CY + CH - 14, "Kim et al., Advanced Science 2022", 11.5, MUTE, "middle", "normal", "italic")

    # ---------------- strip
    SY = CY + CH + 22; SHh = 100
    o += strip(SY, SHh, "clinical implication")
    my = SY + 60
    def node(cx, text, col, r=30, sub=None):
        t = f'<circle cx="{cx}" cy="{my}" r="{r}" fill="#fff" stroke="{col}" stroke-width="2.2"/>'
        lines = text.split("|")
        for i, ln in enumerate(lines):
            t += T(cx, my + 4 - (len(lines) - 1) * 7 + i * 14, ln, 11.5, col, "middle", "bold")
        return t
    o += node(236, "single|biopsy", SLATE) + arrow(276, my, 60) + node(376, "one|organoid", SLATE) + arrow(416, my, 60)
    o += T(486, my - 4, "one drug answer", 13, INK, "start", "bold") + T(486, my + 13, "may miss a resistant region", 11.5, CORAL)
    o += f'<path d="M660 {SY+16}v{SHh-32}" stroke="{GREEN}" stroke-width="1.2" stroke-dasharray="3 4"/>'
    o += node(722, "multi-|region", GREEN) + arrow(762, my, 60) + node(862, "S1–S4|models", GREEN) + arrow(902, my, 60)
    o += T(972, my - 4, "range of responses", 13, INK, "start", "bold") + T(972, my + 13, "target drivers in the shared trunk", 11.5, GREEN)
    return wrap(o, H, "j1")

# =====================================================================  J3
def j3():
    H = 640; CY = 100; CH = 392
    o = head("Oral bacteria in the gut coincide with a blood myeloid state and a lower plasma cell-free DNA variant load",
             "patients with colorectal cancer profiled before any treatment: microbiome, blood cells and plasma from the same person")
    # ---------------- card 1
    x1, w1 = 24, 306
    o += card(x1, CY, w1, CH, "One patient, three compartments")
    groups = [("MOUTH AND GUT MICROBIOME", CORAL, ["saliva", "stool"]),
              ("BLOOD CELLS", TEAL, ["RNA", "genome", "methylation"]),
              ("PLASMA", MAROON, ["cell-free DNA"])]
    gy_ = CY + 56
    for name, col, items in groups:
        o += f'<rect x="{x1+24}" y="{gy_}" width="{w1-48}" height="80" rx="9" fill="#fff" stroke="{col}" stroke-width="1.6"/>'
        o += f'<path d="M{x1+33} {gy_}a9 9 0 0 0-9 9v62a9 9 0 0 0 9 9z" fill="{col}"/>'
        o += T(x1 + 46, gy_ + 27, name, 12.2, col, "start", "bold")
        o += chips(x1 + 46, gy_ + 42, w1 - 80, items)
        gy_ += 98
    o += T(x1 + w1 / 2, CY + CH - 14, "all sampled at diagnosis, before any treatment", 11.2, MUTE, "middle")

    # ---------------- card 2: dumbbell + donut
    x2, w2 = 360, 452
    o += arrow(x1 + w1 + 4, CY + CH / 2)
    o += card(x2, CY, w2, CH, "Oral genera reach the gut in one third of patients")
    genera = [("Fusobacterium", 92, 23), ("Gemella", 86, 5), ("Campylobacter", 85, 0), ("Peptostreptococcus", 80, 20),
              ("Leptotrichia", 78, 3), ("Porphyromonas", 75, 3), ("Selenomonas", 51, 1), ("Parvimonas", 45, 17)]
    ax0, ax1 = x2 + 138, x2 + 300; ay = CY + 84
    SAL, STO = "#4f8fc0", "#9a6b3f"
    o += T(x2 + 22, CY + 60, "share of samples in which each oral genus is found", 11.5, GRAY)
    for v in (0, 50, 100):
        gx = ax0 + (ax1 - ax0) * v / 100
        o += f'<path d="M{gx:.1f} {ay-6}v{8*25+4}" stroke="#ebe8df" stroke-width="1.2"/>' + T(gx, ay + 8 * 25 + 14, f"{v}%", 10.5, MUTE, "middle")
    for i, (g, sa, st) in enumerate(genera):
        y = ay + 8 + i * 25
        xs, xt = ax0 + (ax1 - ax0) * sa / 100, ax0 + (ax1 - ax0) * st / 100
        o += T(ax0 - 12, y + 4, g, 12, INK, "end", "normal", "italic")
        o += f'<path d="M{xt:.1f} {y}H{xs:.1f}" stroke="#cfcbbf" stroke-width="3"/>'
        o += f'<circle cx="{xs:.1f}" cy="{y}" r="5.6" fill="{SAL}"/><circle cx="{xt:.1f}" cy="{y}" r="5.6" fill="{STO}"/>'
    ky = ay + 8 * 25 + 36
    o += f'<circle cx="{ax0-40}" cy="{ky-4}" r="5.6" fill="{SAL}"/>' + T(ax0 - 30, ky, "saliva", 11.5, GRAY)
    o += f'<circle cx="{ax0+74}" cy="{ky-4}" r="5.6" fill="{STO}"/>' + T(ax0 + 84, ky, "stool", 11.5, GRAY)
    # donut 25 / 75
    dcx, dcy, R, r = x2 + 376, CY + 158, 56, 35
    frac = 25 / 75
    def arc(a0, a1, col):
        p = lambda a, rad: (dcx + rad * math.sin(a), dcy - rad * math.cos(a))
        (x0, y0), (x1_, y1_) = p(a0, R), p(a1, R); (x2_, y2_), (x3_, y3_) = p(a1, r), p(a0, r)
        big = 1 if (a1 - a0) > math.pi else 0
        return (f'<path d="M{x0:.2f} {y0:.2f}A{R} {R} 0 {big} 1 {x1_:.2f} {y1_:.2f}L{x2_:.2f} {y2_:.2f}'
                f'A{r} {r} 0 {big} 0 {x3_:.2f} {y3_:.2f}z" fill="{col}" stroke="#fff" stroke-width="2"/>')
    o += arc(0, 2 * math.pi * frac, CORAL) + arc(2 * math.pi * frac, 2 * math.pi, "#d7dbd8")
    o += T(dcx, dcy + 1, "1 in 3", 19, INK, "middle", "bold") + T(dcx, dcy + 17, "patients", 11.5, GRAY, "middle")
    o += T(dcx, dcy + R + 22, "oral bacteria reach", 12, CORAL, "middle", "bold") + T(dcx, dcy + R + 38, "the gut", 12, CORAL, "middle", "bold")
    o += T(dcx, dcy + R + 62, "absent in the rest, so", 11.2, GRAY, "middle") + T(dcx, dcy + R + 77, "treated as an event", 11.2, GRAY, "middle")
    o += f'<path d="M{x2+22} {CY+338}h{w2-44}" stroke="{LINE}" stroke-width="1.2"/>'
    o += T(x2 + w2 / 2, CY + 358, "equally common at every tumor stage", 12, INK, "middle", "bold")
    o += T(x2 + w2 / 2, CY + CH - 14, "the same genera are enriched in cancer across public stool cohorts", 11.2, MUTE, "middle")

    # ---------------- card 3
    x3, w3 = 842, 334
    o += arrow(x2 + w2 + 4, CY + CH / 2)
    o += card(x3, CY, w3, CH, "When oral bacteria are in the gut")
    sy = CY + 52; sh = 70; gap = 9; sp = 104
    o += stat(x3 + 16, sy, w3 - 32, sh, TEAL, "higher", "macrophage M2 signature", "in circulating blood cells", 20, sp)
    o += stat(x3 + 16, sy + (sh + gap), w3 - 32, sh, "#4f8f86", "higher", "neutrophil signature", "secondary; needs replication", 20, sp)
    o += stat(x3 + 16, sy + 2 * (sh + gap), w3 - 32, sh, MAROON, "lower", "plasma cfDNA variant load", "measured in the same patients", 20, sp)
    o += stat(x3 + 16, sy + 3 * (sh + gap), w3 - 32, sh, NAVY, "inverse", "M2 signature vs variant load", "independent of tumor stage", 20, sp)
    o += T(x3 + w3 / 2, CY + CH - 14, "signatures inferred from buffy-coat RNA-seq", 11.2, MUTE, "middle")

    # ---------------- strip: three coupled axes
    SY = CY + CH + 22; SHh = 100
    o += strip(SY, SHh, "three coupled axes", TEAL, "#ECF3F1")
    my = SY + 58
    def axis(cx, col, l1, l2):
        return (f'<rect x="{cx-92}" y="{my-25}" width="184" height="50" rx="25" fill="#fff" stroke="{col}" stroke-width="2.2"/>'
                + T(cx, my - 3, l1, 13, col, "middle", "bold") + T(cx, my + 14, l2, 11.3, GRAY, "middle"))
    def link(xa, xb):
        return (f'<path d="M{xa+9} {my}H{xb-9}" stroke="{SLATE}" stroke-width="2.4"/>'
                f'<path d="M{xa} {my}l10-5.5v11z" fill="{SLATE}"/><path d="M{xb} {my}l-10-5.5v11z" fill="{SLATE}"/>')
    o += axis(312, CORAL, "GUT", "oral pathobionts in stool") + link(410, 466) + axis(564, TEAL, "BLOOD", "myeloid signature")
    o += link(662, 718) + axis(816, MAROON, "PLASMA", "cell-free DNA variant load")
    o += T(438, my - 12, "coupled", 10.8, MUTE, "middle") + T(690, my - 12, "coupled", 10.8, MUTE, "middle")
    o += T(940, my - 12, "association, not a causal chain", 12.2, INK, "start", "bold")
    o += T(940, my + 5, "direction and tumor-derived fraction", 11.2, GRAY) + T(940, my + 20, "not established; not yet replicated", 11.2, GRAY)
    return wrap(o, H, "j3")

# =====================================================================  J2
def j2():
    """Rectal_Organoid manuscript_FINAL.md (revised 2026-09-18) + Supplementary_Tables_FINAL.xlsx:
    S4i per-cohort composite6 AUC with 95% CI (17 cohorts, n = 1,042; pooled 0.522, 0.460-0.584, I2 = 56%),
    S5b Wnt/Notch delta axis r per paired dataset; external pool r = -0.343 (-0.607 to -0.078), I2 = 0%, P = 0.011."""
    H = 640; CY = 100; CH = 392
    o = head("Treatment-induced, not pre-treatment, expression change carries response information in rectal cancer",
             "patient-derived rectal organoids irradiated ex vivo  ·  public pre-treatment cohorts  ·  paired before / during-treatment datasets")
    GOODC, BADC = TEAL, CORAL
    # ---------------- card 1
    x1, w1 = 24, 292
    o += card(x1, CY, w1, CH, "Paired irradiation of organoids")
    def dish(cx, cy, col, tint):
        d = .5
        g = (f'<g transform="translate({cx-62*d:.1f},{cy-30*d:.1f}) scale({d})" stroke="{INK}" stroke-width="3.2">'
             f'<path fill="#fff" d="M2 30v11c0 11.1 26.9 20 60 20s60-8.9 60-20V30"/><ellipse cx="62" cy="30" rx="60" ry="20" fill="#fff"/>'
             f'<ellipse cx="62" cy="30" rx="50" ry="15.5" fill="{tint}" stroke="none"/>')
        for (px, py, r) in [(38,27,10),(68,24,8),(84,37,8),(55,40,6)]:
            g += f'<circle cx="{px}" cy="{py}" r="{r}" fill="#fff" stroke="{col}" stroke-width="3.6"/>'
        return g + '</g>'
    ya, yb = CY + 84, CY + 146
    xl, xr = x1 + 62, x1 + w1 - 62
    o += dish(xl, ya, SLATE, "#e4e8e6") + dish(xr, ya, SLATE, "#e4e8e6")
    o += dish(xl, yb, SLATE, "#e4e8e6") + dish(xr, yb, CORAL, "#f6ddd5")
    o += arrow(xl + 40, ya, xr - xl - 80) + arrow(xl + 40, yb, xr - xl - 80)
    o += T((xl + xr) / 2, ya - 9, "0 Gy", 11.5, GRAY, "middle") + T((xl + xr) / 2, yb - 9, "8 Gy, single dose", 11.5, CORAL, "middle", "bold")
    o += T(xl, yb + 38, "day 0", 11.2, MUTE, "middle") + T(xr, yb + 38, "day 5", 11.2, MUTE, "middle")
    o += T(x1 + w1 / 2, yb + 60, "Δ = irradiated − control, same organoid", 11.8, INK, "middle", "bold")
    ly = CY + 252
    o += f'<path d="M{x1+28} {ly-16}h{w1-56}" stroke="{LINE}" stroke-width="1.2"/>'
    o += T(x1 + 28, ly + 4, "read before and after irradiation", 12.5, INK, "start", "bold")
    o += chips(x1 + 28, ly + 16, w1 - 56, ["RNA-seq", "proteomics", "imaging"])
    o += T(x1 + 28, ly + 62, "and at baseline", 12.5, INK, "start", "bold")
    o += chips(x1 + 28, ly + 74, w1 - 56, ["whole-exome", "normal organoids"])
    o += T(x1 + w1 / 2, CY + CH - 14, "response label: clinical tumor regression grade", 11.2, MUTE, "middle")

    # ---------------- card 2: 17 pre-treatment cohorts, AUC forest (S4i)
    x2, w2 = 346, 420
    o += arrow(x1 + w1 + 4, CY + CH / 2)
    o += card(x2, CY, w2, CH, "Before treatment: no reproducible signal")
    coh = [("GSE93375",13,.15,0,.485),("GSE150082",39,.25,.063,.437),("GSE209746",97,.414,.285,.543),("GSE119409",56,.418,.246,.59),
           ("GSE123390",28,.428,.205,.651),("GSE3493",46,.431,.233,.629),("GSE145037",31,.45,.234,.666),("GSE94104",40,.479,.282,.677),
           ("GSE242786",7,.5,.038,.962),("GSE60331",17,.542,.259,.825),("GSE87211",201,.567,.478,.656),("GSE35452",46,.619,.451,.788),
           ("GSE40492",231,.621,.545,.697),("GSE68204",59,.637,.487,.786),("GSE56699",56,.653,.5,.805),("GSE45404",42,.677,.5,.855),
           ("GSE133057",33,.681,.476,.885)]
    ax0, ax1 = x2 + 118, x2 + w2 - 60; ay = CY + 72; pitch = 13.6
    X = lambda v: ax0 + (ax1 - ax0) * v
    o += T(x2 + 22, CY + 58, "how well baseline expression separates responders, cohort by cohort", 11.3, GRAY)
    yb_ = ay + 17 * pitch + 22
    for v in (0, .5, 1):
        o += f'<path d="M{X(v):.1f} {ay-2}V{yb_}" stroke="{"#9aa19e" if v==.5 else "#ebe8df"}" stroke-width="{1.4 if v==.5 else 1.1}" {"stroke-dasharray=\"4 3\"" if v==.5 else ""}/>'
    o += T(X(.5), yb_ + 13, "chance", 10.8, GRAY, "middle", "bold") + T(X(.04), yb_ + 13, "inverted", 10.5, MUTE, "start") + T(X(.96), yb_ + 13, "predictive", 10.5, MUTE, "end")
    for i, (g, n, a, lo, hi) in enumerate(coh):
        y = ay + 6 + i * pitch
        col = CORAL if hi < .5 else (TEAL if lo > .5 else "#8d9895")
        o += f'<path d="M{X(lo):.1f} {y}H{X(hi):.1f}" stroke="{col}" stroke-width="1.8"/>'
        o += f'<circle cx="{X(a):.1f}" cy="{y}" r="{2.6 + math.sqrt(n) * .22:.1f}" fill="{col}"/>'
    o += T(ax0 - 12, ay + 8.5 * pitch - 4, "public cohorts,", 11, GRAY, "end") + T(ax0 - 12, ay + 8.5 * pitch + 10, "one per row", 11, GRAY, "end")
    yp = ay + 17 * pitch + 10
    o += T(ax0 - 12, yp + 3.8, "all pooled", 11, INK, "end", "bold")
    o += f'<path d="M{X(.460):.1f} {yp}L{X(.522):.1f} {yp-5.5}L{X(.584):.1f} {yp}L{X(.522):.1f} {yp+5.5}z" fill="{INK}"/>'
    o += T(x2 + w2 / 2, CY + 357, "pooled over a thousand patients: close to chance", 12, INK, "middle", "bold")
    o += T(x2 + w2 / 2, CY + CH - 14, "no pathway signature reproduced; cohorts even disagree on direction", 11.2, MUTE, "middle")

    # ---------------- card 3: six paired datasets (S5b)
    x3, w3 = 796, 380
    o += arrow(x2 + w2 + 4, CY + CH / 2)
    o += card(x3, CY, w3, CH, "Under treatment: one direction in all six")
    ds = [("Our organoids", "clinical response", 10, -.905, True), ("Isogenic cell lines", "derived radioresistance", 6, -1.0, False),
          ("Patients", "paired tumor biopsies", 10, -.52, False), ("Rectal organoids", "public, in vitro sensitivity", 12, -.444, False),
          ("Rectal organoids", "public, second series", 14, -.30, False), ("Cell-line panel", "radiation survival", 31, -.191, False)]
    bx0, bx1 = x3 + 170, x3 + w3 - 30; by = CY + 84
    XR = lambda v: bx0 + (bx1 - bx0) * (v + 1) / 1.25          # axis -1 .. +0.25
    o += T(x3 + 22, CY + 58, "Wnt/Notch change under treatment, by response", 11.3, GRAY)
    ybot = by + 6 * 29 + 30
    for v in (-1, 0):
        o += f'<path d="M{XR(v):.1f} {by-8}V{ybot}" stroke="{"#9aa19e" if v==0 else "#ebe8df"}" stroke-width="{1.4 if v==0 else 1.1}" {"stroke-dasharray=\"4 3\"" if v==0 else ""}/>'
    o += T(XR(0) + 8, ybot + 13, "no difference", 10.5, GRAY, "end", "bold") + T(XR(0) - 70, ybot + 13, "←  larger in poor responders", 10.5, CORAL, "end")
    for i, (g, mat, n, r, ours) in enumerate(ds):
        y = by + 8 + i * 29
        col = "#9aa19e" if ours else CORAL
        o += T(bx0 - 14, y, g, 11.4, INK, "end", "bold") + T(bx0 - 14, y + 13, mat, 10.2, GRAY, "end")
        o += f'<path d="M{XR(0):.1f} {y+3}H{XR(r):.1f}" stroke="{col}" stroke-width="3" opacity=".55"/><circle cx="{XR(r):.1f}" cy="{y+3}" r="6" fill="{col}"/>'
    yp = by + 6 * 29 + 16
    o += T(bx0 - 14, yp + 4, "public datasets pooled", 11, INK, "end", "bold")
    o += f'<path d="M{XR(-.607):.1f} {yp}L{XR(-.343):.1f} {yp-6}L{XR(-.078):.1f} {yp}L{XR(-.343):.1f} {yp+6}z" fill="{INK}"/>'
    o += T(x3 + w3 / 2, CY + 326, "the same direction in every paired dataset", 12, INK, "middle", "bold")
    o += T(x3 + w3 / 2, CY + 343, "organoids, cell lines and patients alike", 11.2, GRAY, "middle")
    o += T(x3 + w3 / 2, CY + CH - 28, "each dataset is small: the finding is the shared", 11.2, MUTE, "middle")
    o += T(x3 + w3 / 2, CY + CH - 14, "direction, not the size of any single effect", 11.2, MUTE, "middle")

    # ---------------- strip
    SY = CY + CH + 22; SHh = 100
    o += strip(SY, SHh, "sampling implication", TEAL, "#ECF3F1")
    my = SY + 60
    def node(cx, text, col, r=30):
        t = f'<circle cx="{cx}" cy="{my}" r="{r}" fill="#fff" stroke="{col}" stroke-width="2.2"/>'
        lines = text.split("|")
        for i, ln in enumerate(lines):
            t += T(cx, my + 4 - (len(lines) - 1) * 7 + i * 14, ln, 11.3, col, "middle", "bold")
        return t
    o += node(250, "biopsy|before", SLATE) + arrow(290, my, 60)
    o += T(362, my - 4, "baseline expression only", 13, INK, "start", "bold") + T(362, my + 13, "close to chance across public cohorts", 11.5, CORAL)
    o += f'<path d="M640 {SY+16}v{SHh-32}" stroke="{TEAL}" stroke-width="1.2" stroke-dasharray="3 4"/>'
    o += node(702, "biopsy|before", TEAL) + T(745, my + 5, "+", 18, TEAL, "middle", "bold") + node(788, "during|therapy", TEAL) + arrow(828, my, 60)
    o += T(900, my - 4, "treatment-induced change", 13, INK, "start", "bold") + T(900, my + 13, "Wnt/Notch change tracked poor response", 11.5, TEAL)
    return wrap(o, H, "j2")

html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><style>*{margin:0;padding:0;box-sizing:border-box}'
        'body{background:#555}.ja{display:block}.ja+.ja{margin-top:30px}svg{display:block}</style></head><body>'
        + j1() + j2() + j3() + '</body></html>')
(HERE / "journal_abstracts.html").write_text(html, encoding="utf-8")
print("journal_abstracts.html written")
