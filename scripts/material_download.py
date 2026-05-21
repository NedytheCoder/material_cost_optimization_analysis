from pathlib import Path
import pandas as pd
from mp_api.client import MPRester

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = PROJECT_ROOT / "data" / "raw" / "materials_project_materials.csv"
API_KEY = "GhBbW0tuXZmz0Ec5cQpmMGzOVgYeN3oP"

FIELDS = [
    "material_id",
    "formula_pretty",
    "elements",
    "nelements",
    "nsites",
    "density",
    "density_atomic",
    "volume",
    "band_gap",
    "energy_per_atom",
    "formation_energy_per_atom",
    "is_stable",
    "is_metal",
    "symmetry",
]

rows = []

with MPRester(API_KEY) as mpr:
    docs = mpr.materials.summary.search(
        fields=FIELDS,
        is_stable=True,
        num_elements=(1, 6),
    )

    for doc in docs:
        row = {}
        for field in FIELDS:
            value = getattr(doc, field, None)

            if field == "elements" and value is not None:
                value = [str(x) for x in value]

            if field == "symmetry" and value is not None:
                value = getattr(value, "crystal_system", None)

            row[field] = value

        rows.append(row)

df = pd.DataFrame(rows)
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_PATH, index=False)

print(f"Saved {len(df)} rows to {OUT_PATH.resolve()}")
print(df.head())
