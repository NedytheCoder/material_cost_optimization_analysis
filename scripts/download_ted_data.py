import io
import zipfile
from pathlib import Path

import pandas as pd
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

def download_ted_most_recent_50000_rows(
    output_file=RAW_DATA_DIR / "ted_most_recent_50000.csv",
    target_rows=50000,
    start_year=2023,
    end_year=2006,
    chunk_size=5000,
):
    base_url = "https://data.europa.eu/api/hub/store/data/ted-contract-award-notices-{}.zip"

    collected_chunks = []
    rows_collected = 0
    years_used = []

    for year in range(start_year, end_year - 1, -1):
        if rows_collected >= target_rows:
            break

        url = base_url.format(year)
        print(f"\nTrying year {year}...")
        print(f"URL: {url}")

        try:
            response = requests.get(url, stream=True, timeout=120)
            response.raise_for_status()

            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                csv_files = [name for name in z.namelist() if name.lower().endswith(".csv")]

                if not csv_files:
                    print(f"No CSV found for {year}, skipping.")
                    continue

                csv_name = csv_files[0]
                print(f"Found CSV inside ZIP: {csv_name}")

                with z.open(csv_name) as f:
                    reader = pd.read_csv(
                        f,
                        dtype=str,
                        chunksize=chunk_size,
                        on_bad_lines="skip",
                        engine="python"
                    )

                    year_rows_before = rows_collected

                    for chunk in reader:
                        remaining = target_rows - rows_collected
                        if remaining <= 0:
                            break

                        chunk = chunk.iloc[:remaining].copy()
                        chunk["source_year"] = str(year)

                        collected_chunks.append(chunk)
                        rows_collected += len(chunk)

                    year_rows_added = rows_collected - year_rows_before
                    if year_rows_added > 0:
                        years_used.append((year, year_rows_added))
                        print(f"Added {year_rows_added} rows from {year}")

        except Exception as e:
            print(f"Skipping {year} due to error: {e}")
            continue

    if not collected_chunks:
        raise ValueError("No TED data could be downloaded.")

    final_df = pd.concat(collected_chunks, ignore_index=True)
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(output_file, index=False)

    print("\nDownload complete.")
    print(f"Saved file: {output_file}")
    print(f"Final shape: {final_df.shape}")
    print("Years used:")
    for year, count in years_used:
        print(f"  {year}: {count} rows")

    return final_df


if __name__ == "__main__":
    ted_df = download_ted_most_recent_50000_rows(
        output_file=RAW_DATA_DIR / "ted_most_recent_50000.csv",
        target_rows=50000,
        start_year=2023,
        end_year=2006,
        chunk_size=5000,
    )

    print("\nColumns:")
    print(ted_df.columns.tolist())

    print("\nPreview:")
    print(ted_df.head())
