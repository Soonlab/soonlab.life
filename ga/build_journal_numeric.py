"""Journal-style graphical abstracts for the site themes (three cards + process strip).

Every number drawn here is taken from a source named next to it; anything that is
not data (tree shape, mini heatmap, axis icons) is labelled "schematic" in the panel.

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
             "multifocal organoid capturing of 12 colon cancers  ·  whole-exome and RNA sequencing  ·  24-drug panel")
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
    o += T(x1 + w1 / 2, CY + 172, "primary tumor, 3–4 regions sampled (S1–S4)", 12, GRAY, "middle")
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
    # cohort bar: MSI status, Table 1
    bx, by, bw = x1 + 28, CY + 320, w1 - 56
    o += T(bx, by - 10, "12 patients, microsatellite status", 12.5, INK, "start", "bold")
    parts = [("MSS", 8, "#5f7a8c"), ("MSI-L", 2, "#a9b8c2"), ("MSI-H", 2, CORAL)]
    cx = bx
    for name, n, col in parts:
        ww = bw * n / 12
        o += f'<rect x="{cx:.1f}" y="{by}" width="{ww-2:.1f}" height="20" rx="3" fill="{col}"/>' + T(cx + ww / 2 - 1, by + 14.5, str(n), 12, "#fff", "middle", "bold")
        o += T(cx + ww / 2 - 1, by + 37, name, 11.5, GRAY, "middle")
        cx += ww
    o += T(x1 + w1 / 2, CY + CH - 16, "tumor and normal mucosa sequenced alongside", 11.2, MUTE, "middle")

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
    o += T(gx + 13, gy - 40, "APC · TP53 · ARID1A", 11.8, INK, "start", "bold", "italic")
    o += T(gx + 13, gy - 25, "trunk of SNU-4849,", 10.8, GRAY)
    o += T(gx + 13, gy - 11, "VAF ≈ 0.95", 10.8, GRAY)
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
    o += T(x2 + 22, yy + 12, "13 of 24 drugs: heterogeneous response across subregions", 12.2, INK, "start", "bold")
    drugs = ["afatinib","apitolisib","AZD2014","buparlisib","capecitabine","fluorouracil","ICG-001","irinotecan","MK-5108","oxaliplatin","regorafenib","SAHA","trametinib"]
    px, py = x2 + 22, yy + 24
    for dname in drugs:
        ww = len(dname) * 6.35 + 16
        if px + ww > x2 + w2 - 20:
            px = x2 + 22; py += 24
        o += f'<rect x="{px:.1f}" y="{py}" width="{ww:.1f}" height="19" rx="9.5" fill="#f1efe8" stroke="{LINE}"/>' + T(px + ww / 2, py + 13.5, dname, 11.3, INK, "middle")
        px += ww + 6

    # ---------------- card 3: numbers
    x3, w3 = 826, 350
    o += arrow(x2 + w2 + 4, CY + CH / 2)
    o += card(x3, CY, w3, CH, "What the 12 sets showed")
    sy = CY + 52; sh = 70; gap = 9
    o += stat(x3 + 16, sy, w3 - 32, sh, GREEN, "43 + 23", "organoids + cell lines", "subregional, from 12 patients", 21, 122)
    o += stat(x3 + 16, sy + (sh + gap), w3 - 32, sh, CORAL, "13 / 24", "drugs, heterogeneous response", "between regions of one tumor", 21, 122)
    o += stat(x3 + 16, sy + 2 * (sh + gap), w3 - 32, sh, "#c9771c", "trunk", "drivers shared by all regions", "private mutations on branches", 21, 122)
    o += stat(x3 + 16, sy + 3 * (sh + gap), w3 - 32, sh, NAVY, "kept", "histology, genome, expression", "of the parent tumor, per organoid", 21, 122)
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
             "81 treatment-naive patients with colorectal cancer, profiled at baseline across six data layers")
    # ---------------- card 1
    x1, w1 = 24, 306
    o += card(x1, CY, w1, CH, "One cohort, six baseline data layers")
    layers = [("Stool 16S rRNA", 75, "#9a6b3f"), ("Saliva 16S rRNA", 66, "#4f8fc0"), ("Buffy-coat RNA-seq", 81, TEAL),
              ("Buffy-coat WGS", 60, "#5f7a8c"), ("Buffy-coat methylation", 81, "#7a6bb0"), ("Plasma liquid biopsy", 81, "#d9a21a")]
    ly = CY + 62; bw = w1 - 56
    for i, (name, n, col) in enumerate(layers):
        y = ly + i * 41
        o += T(x1 + 28, y + 2, name, 12.5, INK)
        o += f'<rect x="{x1+28}" y="{y+8}" width="{bw}" height="12" rx="4" fill="#efede6"/>'
        o += f'<rect x="{x1+28}" y="{y+8}" width="{bw*n/81:.1f}" height="12" rx="4" fill="{col}"/>'
        o += T(x1 + w1 - 28, y + 2, f"n = {n}", 12, GRAY, "end")
    sy = CY + 306
    o += f'<path d="M{x1+28} {sy-8}h{bw}" stroke="{LINE}" stroke-width="1.2"/>'
    o += T(x1 + 28, sy + 12, "AJCC stage", 12.5, INK, "start", "bold")
    cx = x1 + 28
    for name, n, col in [("I", 19, "#cfe0dc"), ("II", 24, "#9cc6bd"), ("III", 28, "#4fa394"), ("IV", 9, TEAL)]:
        ww = bw * n / 80
        o += f'<rect x="{cx:.1f}" y="{sy+22}" width="{ww-2:.1f}" height="20" rx="3" fill="{col}"/>'
        o += T(cx + ww / 2 - 1, sy + 36.5, str(n), 11.5, "#fff" if name in ("III", "IV") else INK, "middle", "bold")
        o += T(cx + ww / 2 - 1, sy + 56, name, 11.2, GRAY, "middle")
        cx += ww
    o += T(x1 + w1 / 2, CY + CH - 14, "before any treatment; one stage unrecorded", 11.2, MUTE, "middle")

    # ---------------- card 2: dumbbell + donut
    x2, w2 = 360, 452
    o += arrow(x1 + w1 + 4, CY + CH / 2)
    o += card(x2, CY, w2, CH, "Oral genera reach the gut in one third of patients")
    genera = [("Fusobacterium", 92, 23), ("Gemella", 86, 5), ("Campylobacter", 85, 0), ("Peptostreptococcus", 80, 20),
              ("Leptotrichia", 78, 3), ("Porphyromonas", 75, 3), ("Selenomonas", 51, 1), ("Parvimonas", 45, 17)]
    ax0, ax1 = x2 + 138, x2 + 300; ay = CY + 84
    SAL, STO = "#4f8fc0", "#9a6b3f"
    o += T(x2 + 22, CY + 60, "samples in which the genus was detected (%)", 11.5, GRAY)
    for v in (0, 50, 100):
        gx = ax0 + (ax1 - ax0) * v / 100
        o += f'<path d="M{gx:.1f} {ay-6}v{8*25+4}" stroke="#ebe8df" stroke-width="1.2"/>' + T(gx, ay + 8 * 25 + 14, str(v), 10.5, MUTE, "middle")
    for i, (g, sa, st) in enumerate(genera):
        y = ay + 8 + i * 25
        xs, xt = ax0 + (ax1 - ax0) * sa / 100, ax0 + (ax1 - ax0) * st / 100
        o += T(ax0 - 12, y + 4, g, 12, INK, "end", "normal", "italic")
        o += f'<path d="M{xt:.1f} {y}H{xs:.1f}" stroke="#cfcbbf" stroke-width="3"/>'
        o += f'<circle cx="{xs:.1f}" cy="{y}" r="5.6" fill="{SAL}"/><circle cx="{xt:.1f}" cy="{y}" r="5.6" fill="{STO}"/>'
    ky = ay + 8 * 25 + 36
    o += f'<circle cx="{ax0-40}" cy="{ky-4}" r="5.6" fill="{SAL}"/>' + T(ax0 - 30, ky, "saliva, n = 66", 11.5, GRAY)
    o += f'<circle cx="{ax0+74}" cy="{ky-4}" r="5.6" fill="{STO}"/>' + T(ax0 + 84, ky, "stool, n = 75", 11.5, GRAY)
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
    o += T(dcx, dcy + 2, "25", 24, INK, "middle", "bold") + T(dcx, dcy + 18, "of 75", 11.5, GRAY, "middle")
    o += T(dcx, dcy + R + 22, "oral panel detected", 12, CORAL, "middle", "bold") + T(dcx, dcy + R + 38, "in stool (33%)", 12, CORAL, "middle", "bold")
    o += T(dcx, dcy + R + 62, "absent in 50 of 75,", 11.2, GRAY, "middle") + T(dcx, dcy + R + 77, "so analysed as an event", 11.2, GRAY, "middle")
    o += f'<path d="M{x2+22} {CY+338}h{w2-44}" stroke="{LINE}" stroke-width="1.2"/>'
    o += T(x2 + w2 / 2, CY + 358, "detection by stage I–IV: 5/18 · 6/18 · 5/20 · 2/7  (P = 0.95, batch-free subset)", 11.8, INK, "middle")
    o += T(x2 + w2 / 2, CY + CH - 14, "6 of 8 panel genera enriched in cancer across 11 public stool cohorts (n = 1,395)", 11.2, MUTE, "middle")

    # ---------------- card 3
    x3, w3 = 842, 334
    o += arrow(x2 + w2 + 4, CY + CH / 2)
    o += card(x3, CY, w3, CH, "Detected versus not detected")
    sy = CY + 52; sh = 70; gap = 9; sp = 104
    o += stat(x3 + 16, sy, w3 - 32, sh, TEAL, "+0.44", "blood macrophage M2 signature", "Cliff's δ, q = 0.028, n = 63", 22, sp)
    o += stat(x3 + 16, sy + (sh + gap), w3 - 32, sh, "#4f8f86", "+0.43", "blood neutrophil signature", "δ, q = 0.028; batch-contingent", 22, sp)
    o += stat(x3 + 16, sy + 2 * (sh + gap), w3 - 32, sh, MAROON, "−0.45", "plasma cfDNA variant load", "Cliff's δ, P = 0.034, n = 42", 22, sp)
    o += stat(x3 + 16, sy + 3 * (sh + gap), w3 - 32, sh, NAVY, "ρ −0.47", "M2 signature vs variant load", "stage-adjusted, P = 2.3×10⁻⁴, n = 59", 20, sp)
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
             "patient-derived rectal organoids irradiated ex vivo  ·  17 public pre-treatment cohorts (n = 1,042)  ·  six paired datasets")
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
    ly = CY + 236; bw = w1 - 56
    o += f'<path d="M{x1+28} {ly-18}h{bw}" stroke="{LINE}" stroke-width="1.2"/>'
    for i, (name, n, col) in enumerate([("Tumor organoids", 30, TEAL), ("Normal organoids", 10, "#7fbfb3"),
                                         ("Paired RNA-seq", 11, NAVY), ("Olink proteomics", 10, "#7a6bb0")]):
        y = ly + i * 33
        o += T(x1 + 28, y + 2, name, 12.2, INK) + T(x1 + w1 - 28, y + 2, f"n = {n}", 11.8, GRAY, "end")
        o += f'<rect x="{x1+28}" y="{y+7}" width="{bw}" height="10" rx="4" fill="#efede6"/><rect x="{x1+28}" y="{y+7}" width="{bw*n/30:.1f}" height="10" rx="4" fill="{col}"/>'
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
    o += T(x2 + 22, CY + 58, "response AUC of the organoid-derived axis, per cohort (95% CI)", 11.3, GRAY)
    yb_ = ay + 17 * pitch + 22
    for v in (0, .25, .5, .75, 1):
        o += f'<path d="M{X(v):.1f} {ay-2}V{yb_}" stroke="{"#9aa19e" if v==.5 else "#ebe8df"}" stroke-width="{1.4 if v==.5 else 1.1}" {"stroke-dasharray=\"4 3\"" if v==.5 else ""}/>'
        o += T(X(v), yb_ + 13, f"{v:g}", 10.3, MUTE, "middle")
    for i, (g, n, a, lo, hi) in enumerate(coh):
        y = ay + 6 + i * pitch
        col = CORAL if hi < .5 else (TEAL if lo > .5 else "#8d9895")
        o += T(ax0 - 10, y + 3.6, g, 10.2, GRAY, "end") + T(ax1 + 10, y + 3.6, f"{n}", 10.2, MUTE)
        o += f'<path d="M{X(lo):.1f} {y}H{X(hi):.1f}" stroke="{col}" stroke-width="1.8"/>'
        o += f'<circle cx="{X(a):.1f}" cy="{y}" r="{2.6 + math.sqrt(n) * .22:.1f}" fill="{col}"/>'
    o += T(ax1 + 10, ay - 4, "n", 10.2, MUTE, "start", "bold")
    yp = ay + 17 * pitch + 10
    o += T(ax0 - 10, yp + 3.8, "pooled, 17 cohorts", 10.6, INK, "end", "bold")
    o += f'<path d="M{X(.460):.1f} {yp}L{X(.522):.1f} {yp-5.5}L{X(.584):.1f} {yp}L{X(.522):.1f} {yp+5.5}z" fill="{INK}"/>'
    o += T(x2 + w2 / 2, CY + 357, "pooled AUC 0.52 (95% CI 0.46–0.58, I² = 56%), n = 1,042", 12, INK, "middle", "bold")
    o += T(x2 + w2 / 2, CY + CH - 14, "0 of 52 pathway signatures at FDR < 0.25;  3 of 20,895 genes at FDR < 0.05", 11.2, MUTE, "middle")

    # ---------------- card 3: six paired datasets (S5b)
    x3, w3 = 796, 380
    o += arrow(x2 + w2 + 4, CY + CH / 2)
    o += card(x3, CY, w3, CH, "Under treatment: one direction in all six")
    ds = [("This study", "organoids", 10, -.905, True), ("GSE97543", "isogenic cell lines", 6, -1.0, False),
          ("GSE60331", "patients, paired biopsies", 10, -.52, False), ("PRJNA1198626", "organoids", 12, -.444, False),
          ("GSE294953", "organoids", 14, -.30, False), ("GSE7505", "NCI-60 cell lines", 31, -.191, False)]
    bx0, bx1 = x3 + 170, x3 + w3 - 30; by = CY + 84
    XR = lambda v: bx0 + (bx1 - bx0) * (v + 1) / 1.25          # axis -1 .. +0.25
    o += T(x3 + 22, CY + 58, "Wnt/Notch Δ score vs response, rank-biserial r", 11.3, GRAY)
    ybot = by + 6 * 29 + 30
    for v in (-1, -.5, 0):
        o += f'<path d="M{XR(v):.1f} {by-8}V{ybot}" stroke="{"#9aa19e" if v==0 else "#ebe8df"}" stroke-width="{1.4 if v==0 else 1.1}" {"stroke-dasharray=\"4 3\"" if v==0 else ""}/>'
        o += T(XR(v), ybot + 13, f"{v:g}".replace("-", "−"), 10.3, MUTE, "middle")
    for i, (g, mat, n, r, ours) in enumerate(ds):
        y = by + 8 + i * 29
        col = "#9aa19e" if ours else CORAL
        o += T(bx0 - 14, y, g, 11.4, INK, "end", "bold") + T(bx0 - 14, y + 13, f"{mat}, n = {n}", 10.2, GRAY, "end")
        o += f'<path d="M{XR(0):.1f} {y+3}H{XR(r):.1f}" stroke="{col}" stroke-width="3" opacity=".55"/><circle cx="{XR(r):.1f}" cy="{y+3}" r="6" fill="{col}"/>'
        o += T(XR(r) + 10 if r < -.5 else XR(r) - 10, y - 4, f"{r:.2f}".replace("-", "−"), 10.3, col, "start" if r < -.5 else "end", "bold")
    yp = by + 6 * 29 + 16
    o += T(bx0 - 14, yp + 4, "pooled, 5 external", 11, INK, "end", "bold")
    o += f'<path d="M{XR(-.607):.1f} {yp}L{XR(-.343):.1f} {yp-6}L{XR(-.078):.1f} {yp}L{XR(-.343):.1f} {yp+6}z" fill="{INK}"/>'
    o += T(x3 + w3 / 2, CY + 326, "pooled r = −0.34 (95% CI −0.61 to −0.08)", 12, INK, "middle", "bold")
    o += T(x3 + w3 / 2, CY + 343, "I² = 0%, P = 0.011; r < 0 = larger Δ in poor responders", 11.2, GRAY, "middle")
    o += T(x3 + w3 / 2, CY + CH - 28, "no single external dataset reached P < 0.05;", 11.2, MUTE, "middle")
    o += T(x3 + w3 / 2, CY + CH - 14, "the recovery arm of the axis did not replicate", 11.2, MUTE, "middle")

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
    o += T(362, my - 4, "baseline expression only", 13, INK, "start", "bold") + T(362, my + 13, "pooled AUC 0.52 across 1,042 patients", 11.5, CORAL)
    o += f'<path d="M640 {SY+16}v{SHh-32}" stroke="{TEAL}" stroke-width="1.2" stroke-dasharray="3 4"/>'
    o += node(702, "biopsy|before", TEAL) + T(745, my + 5, "+", 18, TEAL, "middle", "bold") + node(788, "during|therapy", TEAL) + arrow(828, my, 60)
    o += T(900, my - 4, "treatment-induced change", 13, INK, "start", "bold") + T(900, my + 13, "Wnt/Notch Δ tracked poor response, 6 of 6", 11.5, TEAL)
    return wrap(o, H, "j2")

html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><style>*{margin:0;padding:0;box-sizing:border-box}'
        'body{background:#555}.ja{display:block}.ja+.ja{margin-top:30px}svg{display:block}</style></head><body>'
        + j1() + j2() + j3() + '</body></html>')
(HERE / "journal_abstracts.html").write_text(html, encoding="utf-8")
print("journal_abstracts.html written")
