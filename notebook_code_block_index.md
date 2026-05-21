# Code Block Index and Quick Interpretation

This appendix is a companion to the main report. It lists every code cell across the uploaded notebooks and gives a short explanation of what the cell is doing, why it exists, and what its output means. The main report gives the deeper narrative; this file is meant as a quick cross-reference.

## materials_clustering_analysis.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `from pathlib import Path`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 2 (notebook cell 2)
**Starts with:** `cwd = Path.cwd().resolve()`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 3 (notebook cell 3)
**Starts with:** `for path in [reference_path, features_path]:`
**What it does:** Missing-data audit.
**Why it is there:** Measures null patterns so the notebook can decide whether to drop, fill, or preserve fields.
**How to read the output:** The output shows where data quality problems are concentrated.

### Code block 4 (notebook cell 5)
**Starts with:** `reference_df = pd.read_csv(reference_path)`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 5 (notebook cell 7)
**Starts with:** `feature_names = features_df.columns.tolist()`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 6 (notebook cell 9)
**Starts with:** `cluster_runs = []`
**What it does:** Clustering.
**Why it is there:** Groups observations by similarity so hidden structure can be analysed without labels.
**How to read the output:** The output is usually a set of cluster assignments or cluster-quality scores.

### Code block 7 (notebook cell 11)
**Starts with:** `plot_df = cluster_metrics_df.sort_values("silhouette_score", ascending=False).reset_index(drop=True)`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 8 (notebook cell 13)
**Starts with:** `kmeans_only_df = cluster_metrics_df[cluster_metrics_df["model"].str.startswith("KMeans_")].copy()`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 9 (notebook cell 15)
**Starts with:** `valid_metrics_df = cluster_metrics_df.dropna(subset=["silhouette_score"]).copy()`
**What it does:** Cluster evaluation.
**Why it is there:** Measures how compact and well-separated the clusters are so the notebook can choose a defensible configuration.
**How to read the output:** The output is a metrics table comparing candidate clustering solutions.

### Code block 10 (notebook cell 17)
**Starts with:** `plt.figure(figsize=(8, 6))`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 11 (notebook cell 19)
**Starts with:** `cluster_assignments_df = reference_df.copy()`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 12 (notebook cell 21)
**Starts with:** `plt.figure(figsize=(8, 5))`
**What it does:** Cleaning and type fixing.
**Why it is there:** Normalises formats so later modelling or matching steps do not fail on inconsistent types or missing values.
**How to read the output:** The output usually confirms that values were converted or imputed successfully.

### Code block 13 (notebook cell 22)
**Starts with:** `heatmap_values = cluster_feature_zscore_df.to_numpy(dtype=float)`
**What it does:** Cleaning and type fixing.
**Why it is there:** Normalises formats so later modelling or matching steps do not fail on inconsistent types or missing values.
**How to read the output:** The output usually confirms that values were converted or imputed successfully.

### Code block 14 (notebook cell 23)
**Starts with:** `display_columns = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 15 (notebook cell 24)
**Starts with:** `distance_boxplot_data = []`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 16 (notebook cell 25)
**Starts with:** `cluster_feature_rank_pivot_df = cluster_feature_rank_df.pivot(`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 17 (notebook cell 27)
**Starts with:** `cluster_metrics_df.to_csv(cluster_metrics_output, index=False)`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.


## materials_cost_effectiveness_analysis.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `from pathlib import Path`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 2 (notebook cell 2)
**Starts with:** `cwd = Path.cwd().resolve()`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 3 (notebook cell 3)
**Starts with:** `for path in [matched_materials_path, cluster_neighbors_path]:`
**What it does:** Missing-data audit.
**Why it is there:** Measures null patterns so the notebook can decide whether to drop, fill, or preserve fields.
**How to read the output:** The output shows where data quality problems are concentrated.

### Code block 4 (notebook cell 5)
**Starts with:** `matched_materials_df = pd.read_csv(matched_materials_path)`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 5 (notebook cell 7)
**Starts with:** `usable_confidence_levels = ["high", "medium"]`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 6 (notebook cell 9)
**Starts with:** `def assign_within_cluster_cost_class(cluster_df, cluster_label):`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 7 (notebook cell 11)
**Starts with:** `cluster_neighbors_df = cluster_neighbors_df.sort_values(["cluster_label", "source_material_id", "similarity_distance"]).`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 8 (notebook cell 13)
**Starts with:** `source_cost_df = cluster_cost_classes_df[[`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 9 (notebook cell 15)
**Starts with:** `cluster_cost_summary_df = (`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 10 (notebook cell 16)
**Starts with:** `plt.figure(figsize=(8, 5))`
**What it does:** Cleaning and type fixing.
**Why it is there:** Normalises formats so later modelling or matching steps do not fail on inconsistent types or missing values.
**How to read the output:** The output usually confirms that values were converted or imputed successfully.

### Code block 11 (notebook cell 18)
**Starts with:** `cluster_cost_classes_df.to_csv(cluster_cost_classes_output, index=False)`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.


## materials_price_matching.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `from pathlib import Path`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 2 (notebook cell 2)
**Starts with:** `cwd = Path.cwd().resolve()`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 3 (notebook cell 3)
**Starts with:** `for path in [cost_path, cluster_assignments_path, cluster_neighbors_path]:`
**What it does:** Missing-data audit.
**Why it is there:** Measures null patterns so the notebook can decide whether to drop, fill, or preserve fields.
**How to read the output:** The output shows where data quality problems are concentrated.

### Code block 4 (notebook cell 5)
**Starts with:** `cost_df = pd.read_csv(cost_path)`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 5 (notebook cell 7)
**Starts with:** `def normalize_text(value):`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 6 (notebook cell 9)
**Starts with:** `element_symbol_to_name = {`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 7 (notebook cell 11)
**Starts with:** `latest_cost_df = (`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 8 (notebook cell 13)
**Starts with:** `confidence_order = ["high", "medium", "low", "none"]`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 9 (notebook cell 15)
**Starts with:** `cost_materials_df.to_csv(cost_materials_filtered_output, index=False)`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.


## materials_project_cleaning.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `from pathlib import Path`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 2 (notebook cell 2)
**Starts with:** `cwd = Path.cwd().resolve()`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 3 (notebook cell 3)
**Starts with:** `if not raw_path.exists():`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 4 (notebook cell 5)
**Starts with:** `print(df_raw.columns.tolist())`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 5 (notebook cell 7)
**Starts with:** `keep_cols = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 6 (notebook cell 9)
**Starts with:** `def parse_elements(value):`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 7 (notebook cell 11)
**Starts with:** `clustering_feature_cols = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 8 (notebook cell 13)
**Starts with:** `reference_cols = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 9 (notebook cell 15)
**Starts with:** `df.to_csv(output_path, index=False)`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.


## ML_analysis_ted_english.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `from pathlib import Path`
**What it does:** Train/test split.
**Why it is there:** Creates separate training and holdout sets so performance can be measured on unseen data.
**How to read the output:** The output typically reports the sizes of the split datasets.

### Code block 2 (notebook cell 3)
**Starts with:** `cwd = Path.cwd().resolve()`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 3 (notebook cell 5)
**Starts with:** `print(df.columns.tolist())`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 4 (notebook cell 7)
**Starts with:** `TARGET_RAW = "VALUE_EURO"`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 5 (notebook cell 8)
**Starts with:** `fig, axes = plt.subplots(1, 2, figsize=(14, 5))`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 6 (notebook cell 10)
**Starts with:** `text_features = ["TITLE"]`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 7 (notebook cell 12)
**Starts with:** `X = df[existing_features].copy()`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 8 (notebook cell 14)
**Starts with:** `text_features = [col for col in text_features if col in X.columns]`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 9 (notebook cell 16)
**Starts with:** `X_train, X_test, y_train, y_test = train_test_split(`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 10 (notebook cell 18)
**Starts with:** `transformers = []`
**What it does:** Preprocessing pipeline.
**Why it is there:** Builds the feature-engineering workflow so text, categorical, and numeric data are each handled correctly.
**How to read the output:** This cell usually defines reusable preprocessing objects rather than final results.

### Code block 11 (notebook cell 20)
**Starts with:** `models = {`
**What it does:** Model definition or training.
**Why it is there:** Instantiates or fits one or more predictive models so they can be compared objectively.
**How to read the output:** The output may be silent during definition or may print metrics during fitting.

### Code block 12 (notebook cell 22)
**Starts with:** `results = []`
**What it does:** Preprocessing pipeline.
**Why it is there:** Builds the feature-engineering workflow so text, categorical, and numeric data are each handled correctly.
**How to read the output:** This cell usually defines reusable preprocessing objects rather than final results.

### Code block 13 (notebook cell 24)
**Starts with:** `best_model_name = results_df.iloc[0]["Model"]`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 14 (notebook cell 26)
**Starts with:** `best_model = models[best_model_name]`
**What it does:** Preprocessing pipeline.
**Why it is there:** Builds the feature-engineering workflow so text, categorical, and numeric data are each handled correctly.
**How to read the output:** This cell usually defines reusable preprocessing objects rather than final results.

### Code block 15 (notebook cell 28)
**Starts with:** `sample_preds_log = best_pipeline.predict(X_test.iloc[:100])`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 16 (notebook cell 30)
**Starts with:** `display(results_df)`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 17 (notebook cell 32)
**Starts with:** `import matplotlib.pyplot as plt`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 18 (notebook cell 34)
**Starts with:** `plt.figure(figsize=(10, 6))`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 19 (notebook cell 36)
**Starts with:** `plt.figure(figsize=(10, 6))`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 20 (notebook cell 38)
**Starts with:** `plt.figure(figsize=(10, 6))`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 21 (notebook cell 40)
**Starts with:** `best_preds_log = best_pipeline.predict(X_test)`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 22 (notebook cell 42)
**Starts with:** `residuals = actual_raw - best_preds_raw`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 23 (notebook cell 44)
**Starts with:** `analysis_df = results_df.copy()`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 24 (notebook cell 46)
**Starts with:** `from sklearn.model_selection import GridSearchCV, RandomizedSearchCV`
**What it does:** Hyperparameter tuning.
**Why it is there:** Searches over candidate settings to see whether a stronger model configuration improves generalisation.
**How to read the output:** The output usually reports the best parameters and validation score.

### Code block 25 (notebook cell 48)
**Starts with:** `ridge_pipeline = Pipeline([`
**What it does:** Preprocessing pipeline.
**Why it is there:** Builds the feature-engineering workflow so text, categorical, and numeric data are each handled correctly.
**How to read the output:** This cell usually defines reusable preprocessing objects rather than final results.

### Code block 26 (notebook cell 50)
**Starts with:** `rf_pipeline = Pipeline([`
**What it does:** Preprocessing pipeline.
**Why it is there:** Builds the feature-engineering workflow so text, categorical, and numeric data are each handled correctly.
**How to read the output:** This cell usually defines reusable preprocessing objects rather than final results.

### Code block 27 (notebook cell 52)
**Starts with:** `tuned_results = []`
**What it does:** Evaluation.
**Why it is there:** Calculates performance metrics so the notebook can compare models or candidate solutions in a consistent way.
**How to read the output:** The output is typically a metrics table or ranked summary.

### Code block 28 (notebook cell 54)
**Starts with:** `comparison_df = pd.concat([`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 29 (notebook cell 55)
**Starts with:** `# Extra graph - tuned versus baseline model comparison`
**What it does:** Visualisation.
**Why it is there:** Creates a plot to make patterns, model behaviour, or cluster structure easier to interpret.
**How to read the output:** The output is a chart whose purpose is explanatory rather than transformational.

### Code block 30 (notebook cell 57)
**Starts with:** `candidate_pipelines = {`
**What it does:** Preprocessing pipeline.
**Why it is there:** Builds the feature-engineering workflow so text, categorical, and numeric data are each handled correctly.
**How to read the output:** This cell usually defines reusable preprocessing objects rather than final results.

### Code block 31 (notebook cell 59)
**Starts with:** `final_preds_log = final_best_pipeline.predict(X_test)`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.

### Code block 32 (notebook cell 61)
**Starts with:** `part1_results_df = comparison_df.copy()`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.


## ted_data_cleaning.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `import pandas as pd`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 2 (notebook cell 3)
**Starts with:** `file_path = "../data/raw/ted_most_recent_50000.csv"`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 3 (notebook cell 5)
**Starts with:** `print("Columns:")`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 4 (notebook cell 7)
**Starts with:** `before = df.shape[0]`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 5 (notebook cell 9)
**Starts with:** `TARGET = "VALUE_EURO"`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 6 (notebook cell 11)
**Starts with:** `# Convert target to numeric if needed`
**What it does:** Missing-data audit.
**Why it is there:** Measures null patterns so the notebook can decide whether to drop, fill, or preserve fields.
**How to read the output:** The output shows where data quality problems are concentrated.

### Code block 7 (notebook cell 13)
**Starts with:** `# Fully null columns`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 8 (notebook cell 15)
**Starts with:** `redundant_cols = []`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 9 (notebook cell 17)
**Starts with:** `id_admin_cols = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 10 (notebook cell 19)
**Starts with:** `leakage_cols = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 11 (notebook cell 21)
**Starts with:** `procedural_cols = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 12 (notebook cell 23)
**Starts with:** `core_columns = [`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 13 (notebook cell 25)
**Starts with:** `if "DT_DISPATCH" in df_model.columns:`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 14 (notebook cell 27)
**Starts with:** `# Fill text/categorical columns with "Unknown"`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 15 (notebook cell 29)
**Starts with:** `df_model["LOG_" + TARGET] = np.log1p(df_model[TARGET])`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 16 (notebook cell 31)
**Starts with:** `print("Final cleaned modelling dataset shape:", df_model.shape)`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 17 (notebook cell 33)
**Starts with:** `output_file = "../data/processed/ted_cleaned_for_cost_prediction.csv"`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.


## ted_material_case_studies.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `from pathlib import Path`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 2 (notebook cell 2)
**Starts with:** `cwd = Path.cwd().resolve()`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 3 (notebook cell 3)
**Starts with:** `for path in [ted_path, alternatives_path, cluster_cost_classes_path, feature_rankings_path]:`
**What it does:** Missing-data audit.
**Why it is there:** Measures null patterns so the notebook can decide whether to drop, fill, or preserve fields.
**How to read the output:** The output shows where data quality problems are concentrated.

### Code block 4 (notebook cell 5)
**Starts with:** `ted_df = pd.read_csv(ted_path, low_memory=False)`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 5 (notebook cell 7)
**Starts with:** `# Edit this input template for a new TED case.`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 6 (notebook cell 9)
**Starts with:** `selected_case_rows = []`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 7 (notebook cell 11)
**Starts with:** `selected_case_studies_df = selected_case_studies_df[[`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 8 (notebook cell 13)
**Starts with:** `cluster_feature_rank_pivot_df = feature_rankings_df.pivot(`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 9 (notebook cell 15)
**Starts with:** `case_option_frames = []`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 10 (notebook cell 17)
**Starts with:** `case_summary_df = (`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 11 (notebook cell 18)
**Starts with:** `if not case_summary_df.empty:`
**What it does:** Cleaning and type fixing.
**Why it is there:** Normalises formats so later modelling or matching steps do not fail on inconsistent types or missing values.
**How to read the output:** The output usually confirms that values were converted or imputed successfully.

### Code block 12 (notebook cell 20)
**Starts with:** `selected_case_studies_df.to_csv(case_studies_output, index=False)`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.


## ted_translate_english.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `!pip install deep-translator tqdm`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 2 (notebook cell 3)
**Starts with:** `import json`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 3 (notebook cell 5)
**Starts with:** `cleaned_file = "../data/processed/ted_cleaned_for_cost_prediction.csv"`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 4 (notebook cell 7)
**Starts with:** `if "TITLE" not in df_clean.columns:`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 5 (notebook cell 9)
**Starts with:** `# Safe defaults:`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 6 (notebook cell 11)
**Starts with:** `def normalize_title(text):`
**What it does:** Missing-data audit.
**Why it is there:** Measures null patterns so the notebook can decide whether to drop, fill, or preserve fields.
**How to read the output:** The output shows where data quality problems are concentrated.

### Code block 7 (notebook cell 13)
**Starts with:** `translation_map = {}`
**What it does:** Translation step.
**Why it is there:** Normalises multilingual text into English so downstream text processing becomes more consistent.
**How to read the output:** The output often shows progress, runtime, or example translations.

### Code block 8 (notebook cell 15)
**Starts with:** `def make_batches(texts, batch_size=BATCH_SIZE, max_batch_chars=MAX_BATCH_CHARS):`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 9 (notebook cell 17)
**Starts with:** `translator = GoogleTranslator(source="auto", target="en")`
**What it does:** Translation step.
**Why it is there:** Normalises multilingual text into English so downstream text processing becomes more consistent.
**How to read the output:** The output often shows progress, runtime, or example translations.

### Code block 10 (notebook cell 19)
**Starts with:** `df_clean["TITLE"] = df_clean["TITLE_NORM"]`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 11 (notebook cell 21)
**Starts with:** `sample_check = (`
**What it does:** Column/row reduction.
**Why it is there:** Removes redundant rows or low-value columns to make the dataset more focused and less noisy.
**How to read the output:** The output typically reports a new shape or the remaining columns.

### Code block 12 (notebook cell 23)
**Starts with:** `output_file_final = "../data/processed/ted_cleaned_for_cost_prediction_english.csv"`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 13 (notebook cell 25)
**Starts with:** `print("Translation complete.")`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.


## world_bank_cost_preparation.ipynb
### Code block 1 (notebook cell 1)
**Starts with:** `from pathlib import Path`
**What it does:** Environment setup.
**Why it is there:** Loads the libraries needed later so the notebook can run reproducibly.
**How to read the output:** No analytical output is expected; the cell should run quietly unless a package is missing.

### Code block 2 (notebook cell 2)
**Starts with:** `cwd = Path.cwd().resolve()`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 3 (notebook cell 3)
**Starts with:** `for path in [annual_path, monthly_path]:`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 4 (notebook cell 5)
**Starts with:** `annual_xls = pd.ExcelFile(annual_path)`
**What it does:** Transformation step.
**Why it is there:** Performs an intermediate transformation needed to move the notebook from raw data to final output.
**How to read the output:** The output depends on the stage and is usually a preview, summary, or saved object.

### Code block 5 (notebook cell 7)
**Starts with:** `ANNUAL_SHEET = "Annual Prices (Nominal)"`
**What it does:** Data loading.
**Why it is there:** Brings the source dataset into memory so the following steps operate on a concrete dataframe.
**How to read the output:** The output usually confirms shape, columns, or a sample preview.

### Code block 6 (notebook cell 9)
**Starts with:** `def parse_world_bank_price_sheet(df, header_row_idx, unit_row_idx, data_start_idx):`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 7 (notebook cell 11)
**Starts with:** `cost_for_classification = annual_long.copy()`
**What it does:** Initial inspection.
**Why it is there:** Checks structure, column names, and example rows before any transformations are applied.
**How to read the output:** The output is a sanity check that tells you whether the file was read correctly.

### Code block 8 (notebook cell 13)
**Starts with:** `annual_long.to_csv(annual_output, index=False)`
**What it does:** Export.
**Why it is there:** Writes the processed dataset so later notebooks can reuse a stable intermediate result.
**How to read the output:** The output normally confirms the save path.

