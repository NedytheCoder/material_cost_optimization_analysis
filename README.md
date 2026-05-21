# Data Analytics for Artificial Intelligence Project

This project is organised around two final parts:

- `Part 1`: contract cost prediction from cleaned English TED procurement data
- `Part 2`: material similarity, price-proxy matching, cost-effectiveness analysis, and TED case-study demonstration

## Project Structure

- `scripts/`: reusable Python scripts for downloading source data
- `notebooks/`: Jupyter notebooks for cleaning, clustering, pricing, modeling, and case studies
- `data/raw/`: original source datasets
- `data/processed/`: cleaned and intermediate datasets
- `results/`: generated outputs from the notebooks
- `docs/`: project documentation and Word report files

## Final Workflow

# Before you start, make sure you run all the scripts py files to get all the required datasets

### Part 1: Cost Prediction

Use these notebooks for the final Part 1 workflow:

1. [ted_data_cleaning.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ted_data_cleaning.ipynb)
2. [ted_translate_english.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ted_translate_english.ipynb)
3. [ML_analysis_ted_english.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ML_analysis_ted_english.ipynb)

Main Part 1 outputs:

- [part1_final_model_comparison.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/part1_ml_analysis/part1_final_model_comparison.csv)
- [part1_final_prediction_vs_actual.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/part1_ml_analysis/part1_final_prediction_vs_actual.csv)

### Part 2: Materials and Cost-Effectiveness

Use these notebooks for the final Part 2 workflow:

1. [materials_project_cleaning.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_project_cleaning.ipynb)
2. [world_bank_cost_preparation.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/world_bank_cost_preparation.ipynb)
3. [materials_clustering_analysis.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_clustering_analysis.ipynb)
4. [materials_price_matching.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_price_matching.ipynb)
5. [materials_cost_effectiveness_analysis.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_cost_effectiveness_analysis.ipynb)
6. [ted_material_case_studies.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ted_material_case_studies.ipynb)

Part 2 works as a staged decision-support pipeline:

- cluster materials into technically similar groups
- match price proxies to the material groups where reasonable
- classify cost inside technically similar clusters
- identify lower-cost candidate alternatives
- demonstrate the approach on selected TED case studies

## Recommended Run Order

If you want to run the full project from start to finish, use this order:

1. [ted_data_cleaning.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ted_data_cleaning.ipynb)
2. [ted_translate_english.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ted_translate_english.ipynb)
3. [ML_analysis_ted_english.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ML_analysis_ted_english.ipynb)
4. [materials_project_cleaning.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_project_cleaning.ipynb)
5. [world_bank_cost_preparation.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/world_bank_cost_preparation.ipynb)
6. [materials_clustering_analysis.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_clustering_analysis.ipynb)
7. [materials_price_matching.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_price_matching.ipynb)
8. [materials_cost_effectiveness_analysis.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/materials_cost_effectiveness_analysis.ipynb)
9. [ted_material_case_studies.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/ted_material_case_studies.ipynb)

## Main Output Files

### Part 1

- [ted_cleaned_for_cost_prediction_english.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/data/processed/ted_cleaned_for_cost_prediction_english.csv)
- [part1_final_model_comparison.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/part1_ml_analysis/part1_final_model_comparison.csv)
- [part1_final_prediction_vs_actual.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/part1_ml_analysis/part1_final_prediction_vs_actual.csv)

### Part 2 Core Outputs

- [materials_cluster_assignments.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_clustering/materials_cluster_assignments.csv)
- [materials_cluster_nearest_neighbors.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_clustering/materials_cluster_nearest_neighbors.csv)
- [materials_cluster_feature_rankings.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_clustering/materials_cluster_feature_rankings.csv)
- [materials_with_price_matches.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_pricing/materials_with_price_matches.csv)
- [materials_cluster_cost_classes.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_pricing/materials_cluster_cost_classes.csv)
- [cost_effective_alternatives.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_pricing/cost_effective_alternatives.csv)
- [ted_case_studies_selected.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/ted_case_studies/ted_case_studies_selected.csv)
- [ted_case_material_options.csv](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/ted_case_studies/ted_case_material_options.csv)

## Supporting Output Folders

Supporting analysis and methodology outputs are stored in:

- [results/materials_clustering/supporting](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_clustering/supporting)
- [results/materials_pricing/supporting](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/materials_pricing/supporting)
- [results/ted_case_studies/supporting](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/results/ted_case_studies/supporting)

These files support evaluation, interpretation, and report writing, but they are not the main downstream deliverables.

## Legacy / Not Used in Final Part 2

These notebooks are not part of the current final Part 2 workflow:

- [TED_material_preprocessing.ipynb](/C:/Users/spinn/OneDrive/Documents/NCI%20AI%20Masters/Data%20analytics%20for%20Artificial%20intelligence/Project/notebooks/TED_material_preprocessing.ipynb)

They belong to the older mapping-heavy approach and should be treated as legacy unless you specifically want to review earlier work.

## Notes

- The project now uses the English TED dataset for the final TED case-study stage.
- The final Part 2 workflow is best described as an interpretable decision-support pipeline rather than a fully automated material recommender.
- Price matching uses transparent proxy logic, not exact market prices for every scientific material.
- Case studies are designed to be manually curated TED examples that demonstrate how the system can surface technically similar and potentially lower-cost candidate materials.
#   M a t e r i a l - a n d - p r i c i n g - D a t a - A n a l y t i c s - P r o j e c t 
 
 