from pathlib import Path
from playwright.sync_api import sync_playwright
HERE = Path(__file__).parent
OUT = Path("/tmp/claude-1002/-home-soon/16dd1998-4233-420b-b704-0b717391c6ff/scratchpad/img/web")
NAMES = {"ga1": "ga_models", "ga2": "ga_response", "ga3": "ga_bloodgut"}
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 900, "height": 900}, device_scale_factor=2)
    pg.goto((HERE / "graphical_abstracts.html").as_uri())
    pg.wait_for_timeout(900)
    for sid, name in NAMES.items():
        pg.locator(f"#{sid}").screenshot(path=str(OUT / f"{name}.png"))
        print(name, "ok")
    b.close()
