from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BASE_DIR = PROJECT_ROOT / "data" / "raw" / "cost_data"
BASE_DIR.mkdir(parents=True, exist_ok=True)

session = requests.Session()
session.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.usgs.gov/",
        "Connection": "keep-alive",
    }
)
def download_file(url: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with session.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"Saved: {out_path}")

def download_world_bank_pink_sheet():
    page_url = "https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/world-bank-commodities-price-data-the-pink-sheet"
    html = session.get(page_url, timeout=60)
    html.raise_for_status()

    soup = BeautifulSoup(html.text, "html.parser")
    wanted = {
        "CMO-Historical-Data-Annual.xlsx": BASE_DIR / "world_bank" / "CMO-Historical-Data-Annual.xlsx",
        "CMO-Historical-Data-Monthly.xlsx": BASE_DIR / "world_bank" / "CMO-Historical-Data-Monthly.xlsx",
    }

    found = set()

    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True)
        if text in wanted:
            file_url = urljoin(page_url, a["href"])
            download_file(file_url, wanted[text])
            found.add(text)

    missing = set(wanted) - found
    if missing:
        raise RuntimeError(f"Could not find World Bank files: {sorted(missing)}")

def download_usgs_commodities(selected=None):
    page_url = "https://www.usgs.gov/centers/national-minerals-information-center/historical-statistics-mineral-commodities-united"
    html = session.get(page_url, timeout=60)
    html.raise_for_status()

    soup = BeautifulSoup(html.text, "html.parser")

    # Example list. Change this to match the materials you care about.
    if selected is None:
        selected = {
            "Aluminum",
            "Copper",
            "Iron ore",
            "Lead",
            "Nickel",
            "Silver",
            "Tin",
            "Titanium metal",
            "Zinc",
            "Lithium",
        }

    downloaded = []

    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True)
        href = a["href"]

        if text != "XLSX":
            continue
        if not href.lower().endswith((".xlsx", ".xlsm", ".xls")):
            continue

        # Commodity name is usually the previous visible text in the row
        parent_text = a.parent.get_text(" ", strip=True)

        for commodity in selected:
            if commodity.lower() in parent_text.lower():
                safe_name = commodity.lower().replace(" ", "_").replace("/", "_")
                out_path = BASE_DIR / "usgs" / f"{safe_name}.xlsx"
                file_url = urljoin(page_url, href)
                download_file(file_url, out_path)
                downloaded.append(commodity)
                break

    print("USGS downloaded:", sorted(set(downloaded)))

if __name__ == "__main__":
    print(f"Saving cost datasets to: {BASE_DIR}")
    download_world_bank_pink_sheet()
    download_usgs_commodities()
