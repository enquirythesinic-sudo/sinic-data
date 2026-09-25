"""由 JSON 數據出一張 1080x1350 圖卡。

用法：python3 graphics/render.py <card.json> <out.png>
QC 唔過會 exit 1，唔可以出街。
"""
import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

KIT = Path(__file__).resolve().parent.parent
SETTINGS = KIT / "settings.json"
CONFIG = json.loads(SETTINGS.read_text(encoding="utf-8")) if SETTINGS.exists() else {}
BRAND = os.environ.get("CARD_BRAND") or CONFIG.get("brand", "")
THEME = CONFIG.get("theme", "navy")


def chromium_path():
    base = Path("/opt/pw-browsers")
    for pattern in ("chromium-*/chrome-linux/chrome", "chromium-*/chrome-linux64/chrome"):
        found = sorted(base.glob(pattern))
        if found:
            return str(found[-1])
    return None


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path(sys.argv[2])
    brand = data.get("brand") or BRAND
    if not (KIT / "fonts" / "700.css").exists():
        print("WARN 未裝字體，請先跑 ./setup.sh（而家會用後備字體）")

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium_path(),
                                    args=["--disable-background-networking", "--disable-component-update"])
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        page.goto((KIT / "graphics" / "card.html").as_uri())
        page.evaluate("document.fonts.ready")
        result = page.evaluate("([d, b, t]) => renderCard(d, b, t)", [data, brand, THEME])
        page.evaluate("document.fonts.ready")
        # 字體載入後尺寸會變，再檢查一次
        result = page.evaluate("([d, b, t]) => renderCard(d, b, t)", [data, brand, THEME])
        page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        browser.close()

    for w in result.get("warnings", []):
        print(f"WARN {w}")
    for e in result.get("errors", []):
        print(f"BLOCK {e}")
    if result.get("errors"):
        sys.exit(1)
    print(f"OK {out}")


if __name__ == "__main__":
    main()
