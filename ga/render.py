from pathlib import Path
from playwright.sync_api import sync_playwright
HERE = Path(__file__).parent
OUT = HERE.parent / "public" / "img"
# (source html, element id) -> output name
JOBS = [("journal_abstracts.html", "j1", "ga_models"),
        ("journal_abstracts.html", "j2", "ga_response"),
        ("journal_abstracts.html", "j3", "ga_bloodgut")]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1260, "height": 900}, device_scale_factor=2)
    cur = None
    for src, sid, name in JOBS:
        if src != cur:
            pg.goto((HERE / src).as_uri()); pg.wait_for_timeout(900); cur = src
        pg.locator(f"#{sid}").screenshot(path=str(OUT / f"{name}.png"))
        print(name, "ok")
    b.close()
