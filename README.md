# Data Analytics for Artificial Intelligence Project

> A two-part data analytics project for contract cost prediction, material similarity analysis, price-proxy matching, and TED procurement case-study demonstration.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Before You Start](#before-you-start)
- [Final Workflow](#final-workflow)
  - [Part 1: Cost Prediction](#part-1-cost-prediction)
  - [Part 2: Materials and Cost-Effectiveness](#part-2-materials-and-cost-effectiveness)
- [Recommended Run Order](#recommended-run-order)
- [Main Output Files](#main-output-files)
- [Supporting Output Folders](#supporting-output-folders)
- [Legacy Notebook](#legacy-notebook)
- [Notes](#notes)

---

## Overview

This project is organised around two final parts:

| Part | Focus | Description |
|---|---|---|
| **Part 1** | Contract cost prediction | Builds a machine learning workflow using cleaned English TED procurement data. |
| **Part 2** | Material decision support | Performs material similarity analysis, price-proxy matching, cost-effectiveness analysis, and TED case-study demonstration. |

The final Part 2 workflow is best understood as an **interpretable decision-support pipeline**, not a fully automated material recommender.

---

## Project Structure

```text
.
├── scripts/            # Reusable Python scripts for downloading source data
├── notebooks/          # Jupyter notebooks for cleaning, clustering, pricing, modeling, and case studies
├── data/
│   ├── raw/            # Original source datasets
│   └── processed/      # Cleaned and intermediate datasets
├── results/            # Generated notebook outputs
└── docs/               # Project documentation and Word report files
```

---

## Before You Start

Before running the notebooks, run the Python scripts in the `scripts/` folder to download or prepare the required datasets.

```bash
python scripts/download_cost_data.py
```

If your project uses `uv`, you can run scripts like this:

```bash
uv run python scripts/download_cost_data.py
```

> Make sure the required raw datasets are available before starting the notebook workflow.

---

## Final Workflow

### Part 1: Cost Prediction

Part 1 uses cleaned English TED procurement data to train and compare cost prediction models.

#### Notebooks

| Step | Notebook | Purpose |
|---:|---|---|
| 1 | [`ted_data_cleaning.ipynb`](notebooks/ted_data_cleaning.ipynb) | Clean and prepare TED procurement data. |
| 2 | [`ted_translate_english.ipynb`](notebooks/ted_translate_english.ipynb) | Translate or prepare TED records for the English dataset. |
| 3 | [`ML_analysis_ted_english.ipynb`](notebooks/ML_analysis_ted_english.ipynb) | Train, evaluate, and compare machine learning models. |

#### Main Outputs

| Output | Path |
|---|---|
| Model comparison results | [`results/part1_ml_analysis/part1_final_model_comparison.csv`](results/part1_ml_analysis/part1_final_model_comparison.csv) |
| Prediction vs actual values | [`results/part1_ml_analysis/part1_final_prediction_vs_actual.csv`](results/part1_ml_analysis/part1_final_prediction_vs_actual.csv) |

---

### Part 2: Materials and Cost-Effectiveness

Part 2 builds a staged decision-support workflow for comparing materials using similarity, price proxies, and case-study demonstration.

#### Notebooks

| Step | Notebook | Purpose |
|---:|---|---|
| 1 | [`materials_project_cleaning.ipynb`](notebooks/materials_project_cleaning.ipynb) | Clean and prepare the materials dataset. |
| 2 | [`world_bank_cost_preparation.ipynb`](notebooks/world_bank_cost_preparation.ipynb) | Prepare World Bank commodity cost data. |
| 3 | [`materials_clustering_analysis.ipynb`](notebooks/materials_clustering_analysis.ipynb) | Cluster technically similar materials. |
| 4 | [`materials_price_matching.ipynb`](notebooks/materials_price_matching.ipynb) | Match materials or groups to transparent price proxies. |
| 5 | [`materials_cost_effectiveness_analysis.ipynb`](notebooks/materials_cost_effectiveness_analysis.ipynb) | Classify cost and identify lower-cost candidate alternatives. |
| 6 | [`ted_material_case_studies.ipynb`](notebooks/ted_material_case_studies.ipynb) | Demonstrate the workflow on selected TED case studies. |

#### Part 2 Pipeline

```text
Material Cleaning
      ↓
Commodity Cost Preparation
      ↓
Material Clustering
      ↓
Price-Proxy Matching
      ↓
Cost-Effectiveness Analysis
      ↓
TED Case-Study Demonstration
```

The Part 2 workflow aims to:

- cluster materials into technically similar groups
- match price proxies to material groups where reasonable
- classify cost inside technically similar clusters
- identify lower-cost candidate alternatives
- demonstrate the approach on selected TED case studies

---

## Recommended Run Order

Run the project from start to finish in this order:

| Step | Notebook |
|---:|---|
| 1 | [`notebooks/ted_data_cleaning.ipynb`](notebooks/ted_data_cleaning.ipynb) |
| 2 | [`notebooks/ted_translate_english.ipynb`](notebooks/ted_translate_english.ipynb) |
| 3 | [`notebooks/ML_analysis_ted_english.ipynb`](notebooks/ML_analysis_ted_english.ipynb) |
| 4 | [`notebooks/materials_project_cleaning.ipynb`](notebooks/materials_project_cleaning.ipynb) |
| 5 | [`notebooks/world_bank_cost_preparation.ipynb`](notebooks/world_bank_cost_preparation.ipynb) |
| 6 | [`notebooks/materials_clustering_analysis.ipynb`](notebooks/materials_clustering_analysis.ipynb) |
| 7 | [`notebooks/materials_price_matching.ipynb`](notebooks/materials_price_matching.ipynb) |
| 8 | [`notebooks/materials_cost_effectiveness_analysis.ipynb`](notebooks/materials_cost_effectiveness_analysis.ipynb) |
| 9 | [`notebooks/ted_material_case_studies.ipynb`](notebooks/ted_material_case_studies.ipynb) |

---

## Main Output Files

### Part 1 Outputs

| File | Path |
|---|---|
| Cleaned English TED dataset | [`data/processed/ted_cleaned_for_cost_prediction_english.csv`](data/processed/ted_cleaned_for_cost_prediction_english.csv) |
| Final model comparison | [`results/part1_ml_analysis/part1_final_model_comparison.csv`](results/part1_ml_analysis/part1_final_model_comparison.csv) |
| Prediction vs actual comparison | [`results/part1_ml_analysis/part1_final_prediction_vs_actual.csv`](results/part1_ml_analysis/part1_final_prediction_vs_actual.csv) |

### Part 2 Core Outputs

| File | Path |
|---|---|
| Material cluster assignments | [`results/materials_clustering/materials_cluster_assignments.csv`](results/materials_clustering/materials_cluster_assignments.csv) |
| Cluster nearest neighbours | [`results/materials_clustering/materials_cluster_nearest_neighbors.csv`](results/materials_clustering/materials_cluster_nearest_neighbors.csv) |
| Cluster feature rankings | [`results/materials_clustering/materials_cluster_feature_rankings.csv`](results/materials_clustering/materials_cluster_feature_rankings.csv) |
| Materials with price matches | [`results/materials_pricing/materials_with_price_matches.csv`](results/materials_pricing/materials_with_price_matches.csv) |
| Material cluster cost classes | [`results/materials_pricing/materials_cluster_cost_classes.csv`](results/materials_pricing/materials_cluster_cost_classes.csv) |
| Cost-effective alternatives | [`results/materials_pricing/cost_effective_alternatives.csv`](results/materials_pricing/cost_effective_alternatives.csv) |
| Selected TED case studies | [`results/ted_case_studies/ted_case_studies_selected.csv`](results/ted_case_studies/ted_case_studies_selected.csv) |
| TED case material options | [`results/ted_case_studies/ted_case_material_options.csv`](results/ted_case_studies/ted_case_material_options.csv) |

---

## Supporting Output Folders

Supporting analysis and methodology outputs are stored in:

| Folder | Purpose |
|---|---|
| [`results/materials_clustering/supporting`](results/materials_clustering/supporting) | Supporting clustering outputs for evaluation and interpretation. |
| [`results/materials_pricing/supporting`](results/materials_pricing/supporting) | Supporting pricing outputs for proxy logic and cost interpretation. |
| [`results/ted_case_studies/supporting`](results/ted_case_studies/supporting) | Supporting outputs for TED case-study analysis. |

These files support evaluation, interpretation, and report writing, but they are not the main downstream deliverables.

---

## Legacy Notebook

The following notebook is **not part of the current final Part 2 workflow**:

| Notebook | Status |
|---|---|
| [`TED_material_preprocessing.ipynb`](notebooks/TED_material_preprocessing.ipynb) | Legacy notebook from the older mapping-heavy approach. |

Use this only if you want to review earlier work.

---

## Notes

- The project uses the English TED dataset for the final TED case-study stage.
- The final Part 2 workflow is an interpretable decision-support pipeline rather than a fully automated material recommender.
- Price matching uses transparent proxy logic, not exact market prices for every scientific material.
- Case studies are manually curated TED examples that demonstrate how the system can surface technically similar and potentially lower-cost candidate materials.
