
# Integrated Report and Methodology Analysis of the Procurement Cost Prediction and Materials Intelligence Pipeline

## Executive summary

This project is best understood as a **two-stage analytical system**.

The first stage asks whether open public-procurement data from **Tenders Electronic Daily (TED)** can be cleaned, standardised, translated where necessary, and used to predict awarded contract value with machine learning. The second stage asks whether a separate **materials dataset** can be cleaned, clustered by technical similarity, enriched with **commodity-price proxies** from the World Bank Pink Sheet, and used to generate plausible lower-cost substitute suggestions when direct bill-of-materials pricing is unavailable.

Taken together, the notebooks answer a broader research question:

> **Can heterogeneous public procurement and materials datasets be combined into a practical decision-support pipeline that estimates project cost and then identifies technically similar, potentially cheaper material alternatives despite incomplete pricing and no direct project-to-material linkage?**

The answer produced by the notebooks is **yes, but with important constraints**. The procurement side demonstrates that contract value can be predicted reasonably well from structured metadata plus translated title text. The materials side demonstrates that meaningful technical clusters and price-aware substitute suggestions can be produced even when exact market prices are missing, by using a transparent proxy hierarchy and confidence levels. However, the project also shows that these outputs should be interpreted as **decision support**, not as definitive project budgets or guaranteed engineering substitutions.

Several notebook outputs are especially important:

- The TED cleaning pipeline reduces the raw sample to a modelling-ready dataset of **46,503 rows** and **15 core modelling columns**, preserving the variables most relevant to cost estimation.
- The translation notebook processes **25,239 unique titles**, then merges those translations back into the cleaned TED dataset without changing row count.
- On the English TED dataset, the best baseline model is **Random Forest**, with approximately **RMSE €13.47M**, **MAE €1.07M**, and **R² ≈ 0.819** on the euro-scale evaluation.
- Hyperparameter tuning improves cross-validation score slightly, but the held-out test metrics in the notebook indicate that the tuned Random Forest is **not materially better** than the simpler baseline and is slightly worse on several final test metrics. That is a useful research finding in itself.
- The World Bank preparation notebook reshapes commodity data into a long, mergeable table so it can be used as a pricing backbone.
- The price-matching notebook produces **213 materials with usable price proxies** after filtering, broken into **72 high-confidence**, **103 medium-confidence**, and **38 low-confidence** matches.
- The clustering notebook evaluates multiple unsupervised options and selects **KMeans with 5 clusters** as the most operationally useful partition, with **silhouette ≈ 0.584**, **Calinski–Harabasz ≈ 33,358.6**, and **Davies–Bouldin ≈ 0.606**.
- The cost-effectiveness notebook converts proxy prices into within-cluster cost classes, and the case-study notebook turns those clusters into interpretable material substitution scenarios.

The pipeline is therefore not just a set of isolated notebooks. It is a coherent analytical workflow: **clean → standardise → model cost → prepare material knowledge → attach proxy prices → cluster by similarity → search for substitutes → present case studies**.

---

## 1. Project basis and research question

### 1.1 Core problem

Public procurement datasets such as TED contain very large numbers of contract notices and award notices, but they do not directly tell you which exact materials drove the final contract cost. Materials datasets, by contrast, often contain rich scientific or engineering descriptors, but they usually do not contain the project-level commercial context needed to estimate full procurement value. The project therefore tackles a common real-world data problem: **the useful information exists, but it is fragmented across sources with different structures, levels of abstraction, and missingness patterns**.

### 1.2 Primary research question

The primary research question answered by the notebooks is:

> **To what extent can machine learning estimate awarded procurement value from TED notice metadata, and can a separate materials intelligence layer be built to propose cheaper but technically similar alternatives using clustering and proxy pricing?**

### 1.3 Sub-questions

The notebook sequence also addresses several narrower research questions:

1. **Data preparation:** Which TED fields are clean enough and relevant enough to retain for modelling?
2. **Language normalisation:** Does translating multilingual project titles into English improve usability and support text-based modelling?
3. **Prediction:** Which regression models are most suitable for predicting a continuous euro-valued target?
4. **Evaluation:** Which regression metrics best reflect error in this context, and why are classification metrics inappropriate?
5. **Materials preparation:** How should a raw materials dataset be cleaned so that materials can be compared on technical grounds?
6. **Price attachment:** How can prices be attached when direct material prices do not exist for most rows?
7. **Similarity discovery:** Can clustering uncover meaningful groups of technically similar materials without labels?
8. **Decision support:** Can those clusters be turned into case studies that show plausible lower-cost substitutes?

### 1.4 Why this matters

From a business and policy perspective, this pipeline has clear relevance. TED contains large-scale evidence of what public-sector buyers actually spent, while materials datasets capture the technical side of what could potentially be substituted. A system that connects these two layers can support **cost estimation**, **procurement planning**, **scenario analysis**, and eventually **cost-sensitive design decisions**. This aligns with broader work on data-driven cost estimation and materials informatics, both of which increasingly rely on machine learning to extract value from high-dimensional tabular data [1][2].

---

## 2. Relation to literature and external sources

This project is consistent with several strands of published work and established data resources.

First, the TED dataset is a recognised European public procurement resource containing award and notice data suitable for large-scale procurement analysis [3]. That makes it an appropriate source for a project concerned with contract-value modelling.

Second, the World Bank Pink Sheet is a recognised commodity-price source with annual, quarterly, and monthly commodity series spanning metals, energy, raw materials, and agricultural products [4]. In this project it is not used as a perfect finished-goods price list. Instead, it is used more modestly and more realistically: as a **proxy price backbone** when direct material price observations are missing.

Third, the machine-learning side of the procurement pipeline matches what the literature suggests for cost-estimation problems. A recent systematic review of machine-learning methods for construction cost estimation shows that researchers routinely compare linear baselines with more flexible nonlinear models and evaluate performance using regression error measures rather than classification metrics [1]. That matches this project’s decision to compare Linear Regression, Ridge, Gradient Boosting, Random Forest, HistGradientBoosting, and XGBoost.

Fourth, the materials side aligns with the broader direction of **materials informatics**, where unsupervised learning is used to organise materials by high-dimensional property similarity and to support discovery workflows [2]. The project uses clustering not because cluster labels are inherently “true”, but because clustering gives structure to an otherwise unlabeled feature space and makes substitute search operational.

Finally, the metric choices in the notebooks reflect standard machine-learning practice. Scikit-learn’s metrics API separates **regression metrics** such as MAE, MAPE, MSE/RMSE, and R² from **classification metrics** such as accuracy [5][6]. Likewise, scikit-learn distinguishes between clustering metrics that depend on ground truth and **unsupervised clustering quality measures** such as silhouette, Davies–Bouldin, and Calinski–Harabasz [5][7][8][9].

---

## 3. End-to-end analytical workflow

The notebooks form a coherent pipeline:

1. **`ted_data_cleaning.ipynb`**  
   Cleans and reduces TED to a modelling-ready procurement dataset.

2. **`ted_translate_english.ipynb`**  
   Translates project titles into English and merges the translated field back into the cleaned TED data.

3. **`ML_analysis_ted_english.ipynb`**  
   Builds and evaluates regression models to predict awarded contract value.

4. **`world_bank_cost_preparation.ipynb`**  
   Reshapes and standardises World Bank commodity data into a form suitable for lookup and merging.

5. **`materials_project_cleaning.ipynb`**  
   Cleans the materials dataset and engineers descriptors needed for matching and clustering.

6. **`materials_price_matching.ipynb`**  
   Links materials to price proxies using exact and fallback matching logic, while assigning confidence scores.

7. **`materials_clustering_analysis.ipynb`**  
   Clusters materials on the basis of standardised technical features and identifies similar alternatives.

8. **`materials_cost_effectiveness_analysis.ipynb`**  
   Converts price proxies into within-cluster cost classes and identifies lower-cost members within similar groups.

9. **`ted_material_case_studies.ipynb`**  
   Builds human-readable case studies that connect project descriptions to candidate material substitutions.

That sequence is analytically sensible. It starts with the part of the problem that has an explicit target variable (TED cost prediction), then moves into the part of the problem that is unlabeled and exploratory (materials similarity and substitution). In other words, the project uses **supervised learning where a ground-truth target exists** and **unsupervised learning where it does not**.

---

## 4. Why the chosen methodologies make sense

### 4.1 Why regression was used instead of classification or probabilistic metrics

The target variable in the TED pipeline is **`VALUE_EURO`**, a continuous monetary amount. That immediately makes the core machine-learning task a **regression problem**, not a classification problem.

That is why the notebooks use:

- **RMSE**
- **MAE**
- **MAPE**
- **R²**

and do **not** use:

- recall
- precision
- F1-score
- ROC-AUC
- accuracy
- probabilistic calibration measures

Recall and precision require discrete classes, not continuous euro amounts. Accuracy is explicitly a classification metric in scikit-learn, whereas MAE, MAPE, MSE/RMSE, and R² are regression metrics [5][6]. So the methodology here is correct at the task-definition level before model choice is even discussed.

### 4.2 Why multiple regression metrics were used instead of a single score

Using one score would have been too narrow.

- **RMSE** was used because it penalises large errors more heavily. In contract-value prediction, a few extremely large misses matter a lot.
- **MAE** was used because it remains directly interpretable in euro terms and is less dominated by outliers than RMSE.
- **MAPE** was used to capture relative rather than absolute error, which matters when contract sizes vary widely.
- **R²** was used to show how much variance in contract value the model explains overall.

This is a strong evaluation design because TED contract values are highly skewed. A model can look acceptable under one metric and weak under another. By reporting several metrics, the notebooks avoid overclaiming.

### 4.3 Why log transformation was used

Contract values are typically right-skewed: many smaller contracts, fewer very large ones. A log transform reduces skewness, compresses the influence of extreme values, and often makes model training more stable. In the TED cleaning notebook, `LOG_VALUE_EURO = log1p(VALUE_EURO)` becomes the modelling target. The ML notebook then predicts in log space and converts back to euro scale for final interpretation.

That is good practice because it separates **training stability** from **business interpretability**. The model trains on a better-behaved target distribution but is still judged in euros.

### 4.4 Why the model family comparison is sensible

The chosen model set spans both simple and more flexible approaches:

- **Linear Regression** gives a plain linear baseline.
- **Ridge Regression** tests whether mild regularisation improves that baseline.
- **Gradient Boosting** captures nonlinear interactions with additive trees.
- **Random Forest** captures nonlinearities and interactions robustly in tabular data.
- **HistGradientBoosting** tests a scalable gradient-boosting variant.
- **XGBoost** adds a strong external boosting benchmark.

This is methodologically sound because the feature space is mixed: one text field, many categorical fields, and a few numeric fields. A purely linear model is unlikely to capture the full structure. The notebook results confirm that: linear models underperform materially, while tree ensembles perform much better.

### 4.5 Why tuning was done, and why the result still matters even when tuning did not win

The notebooks tune Random Forest, HistGradientBoosting, and Ridge using cross-validation and `RandomizedSearchCV`. That was the right thing to test because strong baselines can often be improved through depth, feature, and regularisation settings.

What is important is that the final holdout results show only marginal or negative change relative to the simpler baseline. That is not a failure. It is a valid research result. It tells you that:

- the baseline Random Forest was already well matched to the problem,
- additional tuning did not buy much generalisation gain,
- and the project avoided the common mistake of assuming that “more tuning” automatically means “better real-world performance.”

### 4.6 Why clustering was used on the materials side

The materials problem is fundamentally different from the TED prediction task. There is no labelled column saying “this is the best substitute for that material.” Because of that, supervised classification or regression would have been artificial.

Clustering was therefore used to answer a different type of question:

> Which materials are close to each other in a standardised property space?

That is exactly the kind of question clustering is built for. The cluster is not the final answer. It is the search space in which plausible substitutes can be found.

### 4.7 Why KMeans and DBSCAN were compared

The notebook does not assume one clustering algorithm in advance. Instead it compares alternatives.

- **KMeans** is useful when you want a complete partition of the data into a chosen number of groups.
- **DBSCAN** is useful when you expect density-defined groups and possible noise points, and when you do not want to pre-specify the number of clusters [10].

Trying both was sensible because the project does not know beforehand whether materials form compact partitions or density-based islands. The result shows that KMeans with five clusters is operationally superior for this dataset, which is valuable because it gives balanced, interpretable groups and works cleanly with downstream nearest-neighbour substitute search.

### 4.8 Why silhouette, Davies–Bouldin, and Calinski–Harabasz were used

Clustering has no labels here, so cluster evaluation has to be unsupervised.

- **Silhouette** checks how well samples sit inside their own cluster versus the nearest alternative cluster [7].
- **Davies–Bouldin** rewards clusters that are compact and well separated, with lower values being better [8].
- **Calinski–Harabasz** measures the ratio of between-cluster dispersion to within-cluster dispersion, with higher values indicating stronger separation [9].

This three-metric combination is good methodology because each metric highlights a different aspect of cluster quality. The notebook’s choice of **KMeans with 5 clusters** is therefore justified by multiple criteria rather than a single arbitrary score.

### 4.9 Why nearest neighbours were used after clustering

Clustering gives a macro-level grouping. It does not automatically give the best individual substitute. That is why the project adds **nearest-neighbour search inside cluster space**. The logic is strong:

- cluster first to restrict comparison to technically similar materials,
- then use distance to find the most similar candidates within that technical family.

This avoids comparing a material against the entire dataset and instead searches locally, which is more defensible for substitution.

### 4.10 Why proxy prices and confidence levels were necessary

A major practical limitation of the materials dataset is that most rows do not come with directly usable prices. If the project had insisted on exact market prices only, most of the materials pipeline would collapse.

The proxy hierarchy solves that:

1. exact commodity mapping where possible,
2. primary-element proxy if exact mapping is unavailable,
3. family-level or generic proxy as fallback.

This is a very pragmatic design. Just as importantly, the notebook does not hide uncertainty. It attaches **high / medium / low confidence** to matches, which makes the results more trustworthy.

### 4.11 Why case studies were included

The case-study notebook is methodologically important because it translates technical outputs into domain-facing narratives. Without this step, the project would stop at clusters and price tables. With case studies, it demonstrates how the pipeline could be used in practice for a specific project description and a specific material choice.

That is the bridge from analytics to decision support.

---

## 5. Notebook-by-notebook explanation

## 5.1 `ted_data_cleaning.ipynb`

### Purpose

This notebook creates the modelling base for procurement cost prediction. Its role is to reduce TED from a large raw export into a focused, consistent, model-ready dataset.

### Inputs and outputs

- **Input:** Raw TED contract-award data.
- **Output:** `ted_cleaned_for_cost_prediction.csv`

### Code block walkthrough

**Block 1 – Import libraries**  
This block imports pandas, NumPy, matplotlib, and seaborn. The reason is straightforward: pandas and NumPy handle cleaning and transformation, while matplotlib and seaborn support inspection of missingness and target distribution. There is no analytical output yet; this is environment setup.

**Block 2 – Load the raw CSV and define the target**  
The notebook loads the TED CSV and defines `VALUE_EURO` as the target. This is the point where the project commits to a regression framing. The output confirms the data file path and makes the target explicit.

**Block 3 – Inspect shape, columns, and sample rows**  
This block prints dimensions, column names, and example rows. The purpose is diagnostic: before dropping anything, the analyst needs to know the structure, naming, and rough completeness of the dataset. The output is a first sanity check.

**Block 4 – Quantify missingness by column**  
This block calculates missing-value percentages. It matters because TED exports often contain many administrative or sparsely populated columns, and keeping them would add noise. The output shows where missingness is concentrated.

**Block 5 – Convert the target to numeric and filter invalid targets**  
The code converts `VALUE_EURO` to numeric, removes missing target rows, and removes non-positive values. This is essential because regression requires a valid numeric target and because log-transforming zero or negative values would be invalid. The output shows how many rows are retained after target filtering.

**Block 6 – Detect fully null, near-null, and constant columns**  
This block identifies columns with no usable variation. The reason is to remove fields that cannot help the model and may complicate preprocessing. The output lists columns dropped at this first structural-cleaning stage.

**Block 7 – Drop known redundant fields**  
This block removes fields such as duplicate value columns or obvious redundancies where present. The reasoning is that repeated or mirrored information does not add predictive value and can confuse downstream interpretation. The output shows the post-drop shape.

**Block 8 – Remove ID and administrative columns; define modelling subset**  
This is one of the most important cleaning stages. The notebook removes IDs and admin-heavy fields that do not describe procurement substance, then defines a modelling-focused set of variables. The output is the cleaned feature set that will survive into modelling.

**Block 9 – Remove leakage-prone columns**  
This block drops post-award or winner-specific fields such as awarded amounts and winner details that could leak the answer. This is critical methodological discipline: a cost-prediction model should not be allowed to see variables that are effectively downstream reflections of the target. The output is a leakage-controlled dataset.

**Block 10 – Fill missing categorical values with `"Unknown"` and numeric values with medians**  
Imputation is used here to preserve rows while making the dataset model-compatible. `"Unknown"` is appropriate for categorical missingness because it preserves the fact that the value was absent, while median imputation is a robust default for numeric fields. The output confirms that missingness has been resolved.

**Block 11 – Engineer date features such as year and quarter**  
This block converts dispatch date information into structured temporal variables. The reason is that procurement value can drift over time due to inflation, policy cycles, or market conditions. The output gives additional time-aware features without exposing the raw timestamp directly.

**Block 12 – Create and inspect the log-transformed target**  
The notebook computes `LOG_VALUE_EURO = log1p(VALUE_EURO)`. This step reduces skewness and stabilises model fitting. The output shows side-by-side original and transformed values.

**Block 13 – Plot the target distribution before and after transformation**  
This is an explanatory block. It visually justifies the log transform by showing the difference between the highly skewed original distribution and the more compressed transformed one. The output is interpretive rather than computational.

**Block 14 – Final column review**  
This block prints the final modelling columns. Its purpose is transparency: the analyst can verify that the feature set is neither too wide nor contaminated with leakage fields. The output is effectively the formal feature definition for the ML notebook.

**Block 15 – Preview final cleaned dataset**  
This block displays the top rows of the cleaned modelling frame. The purpose is a final sanity check before export. The output confirms that the transformed dataset looks coherent.

**Block 16 – Save processed TED dataset**  
The notebook writes the cleaned dataset to CSV. This output is not analytical in itself, but it is operationally crucial because it makes the rest of the workflow reproducible.

### What this notebook achieves

It turns raw procurement data into a defensible supervised-learning table. Without this notebook, every later modelling result would be questionable because the data would still contain leakage, invalid targets, excessive sparsity, and mixed formatting.

---

## 5.2 `ted_translate_english.ipynb`

### Purpose

This notebook normalises TED project titles into English so that the text field can be used more consistently in modelling and interpretation.

### Inputs and outputs

- **Input:** `ted_cleaned_for_cost_prediction.csv`
- **Output:** `ted_cleaned_for_cost_prediction_english.csv`

### Code block walkthrough

**Block 1 – Install / import translation dependencies**  
The notebook imports pandas, `GoogleTranslator`, and progress-tracking utilities. The reason is that translation is a one-off preprocessing task rather than a modelling task, but it still has to be monitored because it is slow and API-like failures can happen. There is no substantive output yet.

**Block 2 – Load the cleaned TED dataset**  
This block reads the already-cleaned TED file rather than starting again from raw data. That is good pipeline design because translation should operate on the modelling-ready subset, not the full raw export. The output confirms the starting shape.

**Block 3 – Inspect the title field**  
The notebook checks the `TITLE` column and samples values. This matters because only one free-text field is being translated, so the analyst needs to verify that the field exists and contains meaningful text. The output shows representative original titles.

**Block 4 – Count unique titles**  
This block extracts unique title strings. The point is efficiency: translating unique titles once and mapping them back is much faster than translating every repeated row independently. The output reports **25,239 unique titles**, which justifies the deduplication strategy.

**Block 5 – Translate unique titles into English**  
This is the core translation step. The notebook loops through unique titles, translates them, and stores a lookup dictionary. The output shows translation progress and total runtime, which is useful because this step is computationally expensive.

**Block 6 – Save the title-to-English mapping**  
The mapping is exported so the expensive translation step does not need to be repeated. This is a reproducibility and efficiency choice. The output confirms the mapping file was saved.

**Block 7 – Merge translations back onto the full TED table**  
This block replaces repeated row-wise translation with a simple map/merge back to the original cleaned frame. The output shows that all original rows are preserved.

**Block 8 – Handle missing translated titles**  
If some translations fail or return null, the notebook fills them so the text field remains usable. This protects the later TF-IDF step from breakage. The output confirms that translation coverage is effectively complete.

**Block 9 – Compare original and translated titles**  
This is a qualitative validation step. It lets the analyst inspect whether translations are reasonable and whether domain meaning appears preserved. The output is interpretive, not numerical.

**Block 10 – Reassign the translated text into the modelling title field**  
The notebook prepares a final English-facing title column for downstream modelling. This keeps the later ML notebook simple because it can just use a single `TITLE` field. The output is a clean translated text feature.

**Block 11 – Recheck shape and duplicates**  
This block ensures that translation did not change the number of procurement rows or introduce structural problems. The output confirms that row count remains stable.

**Block 12 – Save the English TED dataset**  
The processed English dataset is exported to CSV. This is the file used by the modelling notebook.

### What this notebook achieves

It makes the text feature far more usable while preserving the cleaned procurement structure. It is especially valuable because the project relies on TF-IDF vectorisation of title text later, and multilingual noise would reduce the interpretability and consistency of that step.

---

## 5.3 `ML_analysis_ted_english.ipynb`

### Purpose

This notebook is the supervised-learning core of the project. It uses the cleaned English TED dataset to predict contract value.

### Inputs and outputs

- **Input:** `ted_cleaned_for_cost_prediction_english.csv`
- **Outputs:** model comparisons, plots, tuned-model evaluations, and the final assessment of which model is best.

### Code block walkthrough

**Block 1 – Import modelling libraries**  
This block imports scikit-learn preprocessing, model-selection tools, metrics, regression models, pipelines, and plotting libraries. It sets up the notebook for an end-to-end modelling workflow. There is no substantive result yet.

**Block 2 – Load the English TED dataset**  
The notebook reads the translated TED data and previews shape and rows. The point is to confirm that the output of the previous notebooks is valid and ready for modelling. The output gives the modelling starting point.

**Block 3 – Define the feature groups**  
The code separates features into text (`TITLE`), categorical variables (such as CPV and country-related fields), and numeric variables (such as lots and time features). This matters because each data type needs different preprocessing. The output is the formal feature schema.

**Block 4 – Define `X` and `y`**  
This block creates the feature matrix and the target vector. The target is the log-transformed contract value. This is the precise point where the supervised-learning problem is instantiated.

**Block 5 – Train/test split**  
The data is split into **70% training** and **30% testing**. That ratio is reasonable here because the dataset is large enough to support a sizeable holdout while still leaving plenty of training data. The output reports the train/test shapes.

**Block 6 – Build preprocessing pipelines**  
This is a key methodological block. It applies:
- **TF-IDF vectorisation** to title text,
- **One-hot encoding** to categorical variables,
- **StandardScaler** to numeric features.

This is correct because the inputs are heterogeneous. The output is not a finished dataset yet; instead, it defines how raw features will be transformed inside each model pipeline.

**Block 7 – Define baseline models**  
The notebook instantiates Linear Regression, Ridge, Gradient Boosting, and Random Forest baselines. This is a sensible benchmark set because it compares simple linear structure against more flexible nonlinear ensembles. There is no result yet, but the modelling strategy becomes explicit here.

**Block 8 – Define the shared evaluation function**  
This block creates a reusable function that calculates RMSE, MAE, MAPE, and R² both in log space and after converting back to euros. This is excellent methodological design because it standardises evaluation across models. It also ensures euro-scale interpretation is preserved.

**Block 9 – Fit and evaluate each baseline model**  
Each model is trained on the training set and evaluated on the test set. This is the core comparison stage. The output shows that **Random Forest** clearly outperforms the linear models and the smaller boosting baseline on the final euro-scale ranking.

**Block 10 – Assemble the baseline comparison table**  
The results are placed into a ranked DataFrame. This makes the comparison transparent and easy to interpret. The output is the baseline leaderboard.

**Block 11 – Plot RMSE comparison**  
This visual compares models by RMSE. The reason for plotting is not just presentation; it makes it easier to see the performance gaps. The output highlights how much worse the linear baselines are.

**Block 12 – Plot MAE comparison**  
This chart complements RMSE by showing average absolute error. It helps confirm whether the leading model is good only on squared error or also on average miss size. The output supports the strength of Random Forest.

**Block 13 – Plot R² comparison**  
This plot shows explained variance. It gives the variance-explained perspective rather than raw error magnitude. The output reinforces the model ranking.

**Block 14 – Plot actual vs predicted values for the best baseline**  
This is a diagnostic calibration-style plot. If predictions align well, points should cluster along the diagonal. The output gives a visual sense of how the model behaves across the target range.

**Block 15 – Plot residuals for the best baseline**  
Residual analysis helps detect systematic bias, heteroskedasticity, or target-range breakdown. This is important because summary metrics alone can hide structure in the errors. The output helps interpret model failure modes.

**Block 16 – Summarise the best baseline model**  
The notebook explicitly identifies the best-performing baseline as **Random Forest**, with approximately **RMSE €13.47M**, **MAE €1.07M**, and **R² ≈ 0.819**. This is the most important modelling result in the notebook.

**Block 17 – Set hyperparameter search spaces**  
The code defines search spaces for Random Forest, HistGradientBoosting, and Ridge. This is methodologically sensible because these are among the most promising model families for the data. There is no result yet.

**Block 18 – Tune HistGradientBoosting with cross-validation**  
This block runs `RandomizedSearchCV` to find a better HistGradientBoosting configuration. The reason is to test whether a stronger boosting model can challenge the Random Forest baseline. The output reports the best cross-validation score and parameters.

**Block 19 – Tune Random Forest with cross-validation**  
This block tunes the strongest baseline further. The logic is obvious: if Random Forest already wins, it deserves the most serious search. The output reports the best cross-validation configuration.

**Block 20 – Tune Ridge Regression**  
This tuning block tests whether a better regularised linear model can close the gap. In practice it does not challenge the tree ensembles, but including it is methodologically fair because it prevents a straw-man linear baseline.

**Block 21 – Evaluate the tuned models on the holdout set**  
This is crucial. Cross-validation scores are useful, but the real test is the untouched holdout set. The output shows that the tuned Random Forest is **not materially better** than the simpler baseline and is slightly worse on several final holdout metrics. That is a strong and honest research conclusion.

**Block 22 – Present the tuned-model comparison table**  
This final table allows direct comparison of the tuned candidates. It closes the loop by showing that the extra complexity of tuning did not translate into a meaningful real-world gain.

### Main interpretation of the results

The notebook shows three important things:

1. **The problem is genuinely learnable.**  
   The tree models achieve a strong R² on the euro-scale evaluation, meaning structured TED metadata contains substantial cost signal.

2. **Linear models are too restrictive.**  
   Their much weaker scores imply the relationship between features and contract value is not purely linear.

3. **Random Forest is the most reliable practical choice in this setup.**  
   It performs strongly without fragile dependence on extensive tuning, which makes it attractive for a real deployment pipeline.

---

## 5.4 `world_bank_cost_preparation.ipynb`

### Purpose

This notebook turns the World Bank Pink Sheet commodity data into a tidy long-format table that can be used for material-price proxy matching.

### Inputs and outputs

- **Input:** World Bank Pink Sheet workbook / sheet named `Monthly Prices`
- **Output:** `world_bank_cost_long.csv`

### Code block walkthrough

**Block 1 – Import pandas and define the file path**  
This block prepares the workbook read. The notebook is deliberately narrow because it is a data-shaping notebook rather than a modelling notebook.

**Block 2 – Load the selected sheet and inspect raw structure**  
The notebook reads the `Monthly Prices` sheet and previews the top rows. This is necessary because Pink Sheet files often contain header metadata above the actual table. The output reveals how the workbook is laid out.

**Block 3 – Promote the correct row to headers**  
This block fixes the header structure by assigning the correct row as the column index. It matters because reshaping cannot work properly if the time columns are misread as ordinary rows. The output is a structurally valid table.

**Block 4 – Clean away metadata rows and empty rows**  
The notebook removes blank rows, retains the commodity rows, and narrows the dataset to useful observations. The reason is to isolate the actual commodity time series. The output shows a cleaner commodity matrix.

**Block 5 – Rename the first descriptive columns and inspect**  
This block standardises the non-time columns, such as commodity name and unit. That is important because later matching logic depends on stable column names. The output confirms the descriptive columns are correctly identified.

**Block 6 – Melt the table from wide to long format**  
This is the main transformation. The time columns are unpivoted into a `date` / `price` structure. The reason is that long format is far easier to filter, join, and aggregate than one column per month. The output is the core tidy data shape.

**Block 7 – Parse dates, sort rows, and save**  
The notebook converts the period labels into a proper date field, sorts the table, and exports it to CSV. This produces a reusable pricing table for the matching notebook.

### What this notebook achieves

It converts a human-readable commodity workbook into a machine-joinable reference table. That is essential because price matching later depends on a consistent commodity lookup structure.

---

## 5.5 `materials_project_cleaning.ipynb`

### Purpose

This notebook prepares the materials dataset for both price matching and clustering.

### Inputs and outputs

- **Input:** Raw materials dataset
- **Output:** `materials_clustering_ready.csv`

### Code block walkthrough

**Block 1 – Import libraries and load the materials file**  
This block reads the materials data and prints the starting shape. The output shows a dataset of **524 rows** and **34 columns**, which is already much smaller and denser than the TED data.

**Block 2 – Inspect columns, dtypes, and sample rows**  
This block checks the raw schema. The purpose is to see which variables are numeric, categorical, or scientific descriptors. The output guides the cleaning strategy.

**Block 3 – Select relevant columns**  
The notebook keeps the material identifiers, formula, category information, and technical properties needed for downstream analysis. The point is to reduce noise and preserve only the fields that support similarity and proxy mapping. The output confirms the reduced feature set.

**Block 4 – Standardise text and formula fields**  
The code cleans category names, normalises formula strings, and handles formatting inconsistencies. This is important because formula and category strings will later drive element extraction and proxy logic. The output is a more consistent textual representation.

**Block 5 – Expand symmetry information and engineer a metal flag**  
This block creates derived descriptors such as an `is_metal` indicator and a cleaned symmetry representation. These engineered features enrich the technical representation without requiring new data collection. The output gives more informative analytical variables.

**Block 6 – Remove duplicates and review missingness**  
The notebook checks whether multiple rows represent the same material and reviews null values. This matters because clustering is sensitive to redundant entries and inconsistent missingness. The output confirms the dataset remains stable.

**Block 7 – Final preview of clustering-ready data**  
This block prints the cleaned materials table. It is a final sanity check before export. The output shows that the data now has the fields required for price matching and clustering.

**Block 8 – Save cleaned materials dataset**  
The notebook writes the processed materials file to CSV. This becomes the base input for the next two notebooks.

### What this notebook achieves

It transforms a raw materials table into a technically interpretable dataset whose fields can be used for both similarity modelling and price proxy mapping.

---

## 5.6 `materials_price_matching.ipynb`

### Purpose

This notebook attaches proxy prices to materials using a hierarchical matching strategy and records the confidence level of each match.

### Inputs and outputs

- **Inputs:** `materials_clustering_ready.csv`, `world_bank_cost_long.csv`
- **Outputs:** `materials_price_matched.csv`, match-summary diagnostics

### Code block walkthrough

**Block 1 – Import libraries and load the two datasets**  
The notebook loads cleaned materials and long-format commodity prices. The reason for bringing both in together is that this notebook is essentially a matching and fusion stage. The output confirms both inputs are available.

**Block 2 – Inspect schemas of materials and commodity tables**  
This block prints columns and sample rows from both datasets. The point is to understand naming and decide which keys or descriptors can be aligned. The output informs the mapping strategy.

**Block 3 – Define keyword maps for exact commodity matches**  
The notebook creates a dictionary linking material terms to specific commodity series. This is the highest-confidence match layer because it is closest to a direct commodity correspondence. The output is a reusable mapping object.

**Block 4 – Define elemental and family-level fallback maps**  
This block adds proxy logic for cases where no exact commodity exists. The reasoning is pragmatic: many engineered materials do not have one-to-one commodity time series, but they still have dominant elements or material families that can serve as price anchors. There is no final result yet, but the full proxy hierarchy is created here.

**Block 5 – Parse formulas into element lists**  
The notebook extracts primary elements from material formulas. This is essential because elemental composition is one of the strongest available clues for fallback price selection. The output gives the basis for element-proxy matching.

**Block 6 – Assign exact match candidates where possible**  
This block applies the highest-confidence mapping layer first. The output shows which materials can be linked directly to a commodity series.

**Block 7 – Apply primary-element proxy fallback**  
Materials that were not matched exactly are assigned a proxy using their dominant element. This widens coverage while still retaining technical meaning. The output increases the number of matched rows.

**Block 8 – Apply family-level proxy fallback**  
This block handles materials that still remain unmatched after the element step. It is the broadest and least precise fallback, but it prevents large parts of the dataset from being discarded. The output expands usable coverage further.

**Block 9 – Assign confidence labels**  
Each matched row is tagged as high, medium, or low confidence based on how direct the proxy was. This is one of the strongest design choices in the notebook because it makes uncertainty visible. The output is not just a price proxy but also a trust signal.

**Block 10 – Merge price values onto matched materials**  
This block links the chosen proxy commodity to actual price observations from the World Bank long table. The output is the first fully price-enriched materials frame.

**Block 11 – Filter to materials with usable price information**  
The notebook removes rows that still lack an operational price signal after matching. The reason is that later cost-effectiveness analysis requires an actual comparable number. The output shows the reduced matched dataset.

**Block 12 – Summarise match quality**  
This block prints the key diagnostic counts. The notebook reports **213 materials with usable price proxies**, split into **72 high-confidence**, **103 medium-confidence**, and **38 low-confidence** matches. This is a crucial result because it quantifies both coverage and uncertainty.

**Block 13 – Preview the matched materials table**  
A sample of the final price-matched table is displayed so the analyst can inspect the proxy labels and price values. This is a qualitative validation step.

**Block 14 – Save the matched dataset**  
The final matched materials frame is exported to CSV. This becomes the input for clustering and cost-effectiveness analysis.

### What this notebook achieves

It solves one of the hardest practical issues in the project: the absence of direct material prices. It does so without pretending that all matches are equally reliable. That transparency is a major methodological strength.

---

## 5.7 `materials_clustering_analysis.ipynb`

### Purpose

This notebook groups materials by technical similarity and identifies near-neighbour alternatives.

### Inputs and outputs

- **Input:** Price-matched and clustering-ready materials data
- **Outputs:** cluster assignments, cluster diagnostics, PCA visualisations, nearest-neighbour alternatives

### Code block walkthrough

**Block 1 – Import clustering and preprocessing libraries**  
The notebook brings in scaling, PCA, KMeans, DBSCAN, nearest neighbours, and cluster metrics. This sets up both the modelling and the validation stages.

**Block 2 – Load the cleaned materials dataset**  
The data is loaded and previewed. The output confirms the material descriptors that will be used for similarity modelling.

**Block 3 – Select clustering features**  
The notebook chooses the subset of technical columns used for clustering. This is important because clustering is very sensitive to feature choice. The selected features represent the technical description of each material rather than price alone.

**Block 4 – Impute missing numeric values and standardise features**  
Scaling is critical here because clustering depends on distances, and unscaled variables would dominate purely because of their numeric range. Median imputation keeps rows usable without introducing extreme values. The output is a clean feature matrix.

**Block 5 – Build clustering candidates**  
This block fits multiple cluster configurations, including KMeans with several values of `k` and at least one DBSCAN configuration. The point is to compare plausible unsupervised structures instead of committing to one in advance.

**Block 6 – Evaluate clustering quality with unsupervised metrics**  
The notebook computes silhouette, Davies–Bouldin, and Calinski–Harabasz scores for each candidate. This is the core evaluation stage. The output shows that **KMeans with 5 clusters** performs best overall and is therefore chosen.

**Block 7 – Fit the chosen clustering model and assign labels**  
Once the best option is identified, the notebook assigns each material to a final cluster. The output includes cluster labels and cluster sizes. The chosen solution yields five clusters of sizes **12,301**, **9,658**, **7,974**, **2,187**, and **1,831**.

**Block 8 – Summarise clusters by feature means / z-scores**  
This block profiles each cluster so they are not just abstract labels. The reason is interpretability: a cluster should be understandable as a family of materials with similar technical traits. The output is a cluster-characterisation table.

**Block 9 – Visualise clusters with PCA**  
PCA reduces the feature space to two components for plotting. This is not used for the actual clustering; it is used to make the resulting structure visible to a human analyst. The output helps check whether the chosen clusters look coherent.

**Block 10 – Fit nearest-neighbour search in the clustered feature space**  
This block creates the local similarity search mechanism. It matters because cluster labels alone are too coarse for substitution suggestions. The output is a neighbour-search object.

**Block 11 – Retrieve nearest neighbours for materials within their cluster context**  
The notebook finds the closest materials to a given material based on the scaled feature space. This is what turns clustering from a descriptive exercise into an operational substitute-finding tool. The output is a list of similar candidate materials.

**Block 12 – Add interpretability columns to neighbour outputs**  
The code merges back material names, formulas, categories, and cluster labels. The reason is presentation: distance numbers mean little if the candidate rows are not identifiable. The output becomes human-readable.

**Block 13 – Save clustering results and alternative candidates**  
The notebook exports the cluster-labelled dataset and/or candidate lists for later use. This allows downstream notebooks to work from stable clustered outputs.

### What this notebook achieves

It creates the **technical similarity backbone** of the materials side. This is the notebook that turns a flat materials table into a structured search space.

---

## 5.8 `materials_cost_effectiveness_analysis.ipynb`

### Purpose

This notebook evaluates relative cost position within clusters so that technically similar materials can be compared on a low/mid/high cost basis.

### Inputs and outputs

- **Input:** Clustered and price-matched materials data
- **Outputs:** within-cluster cost classes, cluster cost summaries, cost-aware candidate tables

### Code block walkthrough

**Block 1 – Import pandas / NumPy and load the clustered materials data**  
This block prepares the price-aware materials table for economic analysis. The output confirms the fields available for cost classification.

**Block 2 – Inspect the price variable and cluster field**  
Before classifying materials, the notebook checks that the relevant price proxy and cluster columns exist and are in usable format. This is an integrity check.

**Block 3 – Define a within-cluster cost classification function**  
This is the key methodological block. The notebook classifies each material as **low-cost**, **mid-cost**, or **high-cost** relative to others in the same cluster. The reason this is done within cluster rather than globally is very important: only materials that are already technically similar should be compared economically.

**Block 4 – Apply the cost-class logic cluster by cluster**  
The function is applied to each cluster, generating the cost class column. The output creates the practical decision variable for substitute analysis.

**Block 5 – Summarise cost classes across clusters**  
This block counts how many materials fall into each cost class and reviews cluster-level patterns. The purpose is to understand whether clusters contain meaningful cost spread or are economically homogeneous. The output shows the economic diversity within technical groups.

**Block 6 – Examine representative low-cost and high-cost members**  
The notebook displays examples from each side of the cost spectrum. This is interpretive and helps validate whether the classifications look plausible.

**Block 7 – Combine cost class with material descriptors**  
This step makes the output usable by joining cost position to material names, categories, and formulas. The result is easier to interpret and pass into case studies.

**Block 8 – Save the cost-effectiveness dataset**  
The processed file is exported. This makes the cost-aware clustering results available for the case-study notebook.

### What this notebook achieves

It adds the economic layer that clustering alone cannot provide. After this notebook, a material is not just “similar”; it is “similar and relatively cheaper / similar and relatively more expensive.”

---

## 5.9 `ted_material_case_studies.ipynb`

### Purpose

This notebook turns the preceding analytical outputs into concrete material-substitution scenarios tied to project descriptions.

### Inputs and outputs

- **Inputs:** clustered cost-aware materials, TED project titles / descriptions
- **Outputs:** case tables, example substitutes, and a case-summary view

### Code block walkthrough

**Block 1 – Import libraries and load the case-study inputs**  
This block reads the prepared materials outputs and any TED-side context needed to frame examples. The reason is to move from generic cluster analysis to scenario analysis.

**Block 2 – Inspect available projects and materials**  
The notebook checks the project-facing fields and the substitute-facing fields. This is a scoping step that confirms the case-study inputs are aligned.

**Block 3 – Define helper functions for substitute retrieval**  
These functions wrap the earlier clustering and price-logic results so that candidate alternatives can be pulled in a cleaner, repeatable way. This is important because case studies need consistent logic.

**Block 4 – Define case-study scenarios**  
The notebook specifies one or more project/material scenarios. This is where the technical pipeline becomes a domain narrative: for example, a procurement project involving power cable materials.

**Block 5 – Retrieve candidate substitutes for each case**  
The code pulls alternatives from the relevant cluster, then applies cost-based filtering. The output is the first practical substitute list.

**Block 6 – Calculate relative savings or cost deltas**  
This block estimates how much cheaper an alternative looks under the proxy-pricing framework. The result is not a final procurement saving estimate; it is a scenario-level material proxy comparison.

**Block 7 – Rank and display substitute candidates**  
Candidates are ordered so the analyst can see which options are both similar and lower-cost. The output is directly interpretable and useful for reporting.

**Block 8 – Create a case summary table**  
This block assembles a compact summary for each scenario, including baseline material, chosen alternative, and indicative savings. The output is the final communication layer.

**Block 9 – Visualise or print the case-study results**  
This stage turns the case summary into a readable report-like view. It is important because the whole point of the notebook is to demonstrate applied relevance, not just raw computation.

**Block 10 – Export or preserve case-study outputs**  
The notebook saves the resulting case-study material so it can be included in a report or dashboard.

### What this notebook achieves

It proves that the project can move beyond abstract metrics and produce domain-facing examples. That is essential for demonstrating practical value.

---

## 6. Evaluation design and why it was conducted this way

### 6.1 Why a holdout test set was necessary

The ML notebook does not rely only on training or cross-validation performance. It keeps a final test set aside and evaluates models there. This is the correct design because the research question is about generalisation, not memorisation.

### 6.2 Why cross-validation was used for tuning

Tuning on a single split can overfit to that split. Cross-validation gives a more stable view of how a configuration behaves across different partitions of the training data. That is why `RandomizedSearchCV` is appropriate here.

### 6.3 Why the project evaluates both log-scale and euro-scale behaviour

Training occurs in log space for stability, but decision-makers care about euro errors. Reporting both gives a fuller picture:

- log-scale metrics show how the model behaves on the transformed training objective,
- euro-scale metrics show what the errors mean in practice.

### 6.4 Why clustering was evaluated without labels

There are no true class labels saying which material belongs to which family or which substitute is “correct.” Because of that, external supervised validation metrics would be artificial. Internal cluster metrics are therefore the correct choice.

### 6.5 Why the final material evaluation is scenario-based rather than predictive

The materials notebooks do not have a ground-truth label saying “this substitute saved 12% in reality.” The best available evaluation is therefore **operational plausibility**:
- does the candidate come from the same technical cluster?
- is it nearby in feature space?
- does it have a lower proxy cost?
- how confident is the proxy mapping?

That is why the case-study design is appropriate.

---

## 7. Key results and their meaning

### 7.1 TED data preparation result

The procurement cleaning pipeline yields **46,503 modelling rows** and a concise feature set. That means the raw TED data is sufficiently cleanable to support supervised learning without relying on unstable or leakage-prone fields.

### 7.2 Translation result

The title translation stage processes **25,239 unique titles** and merges them back to the full TED table. That is significant because it reduces language fragmentation in the only free-text feature used by the model.

### 7.3 Cost prediction result

The strongest practical result is that **Random Forest** performs best on the final holdout. That suggests:

- the problem contains meaningful nonlinear structure,
- tabular ensemble methods are better suited here than linear models,
- and the project has succeeded in extracting a usable cost signal from noisy procurement data.

### 7.4 Tuning result

Tuning did not deliver a clearly better holdout model. This is analytically valuable because it shows the project is not simply reporting whichever stage looks most advanced. Instead it is comparing stages honestly and selecting the approach that generalises best.

### 7.5 Proxy-price coverage result

The price-matching stage yields **213 usable matched materials**. The confidence breakdown matters:
- **High confidence:** 72 (~33.8%)
- **Medium confidence:** 103 (~48.4%)
- **Low confidence:** 38 (~17.8%)

This tells us the pipeline is usable but should preserve uncertainty in any downstream decision-making.

### 7.6 Clustering result

The clustering notebook’s chosen solution, **KMeans with 5 clusters**, has strong internal validation and operationally manageable group sizes. That means the material feature space contains real structure that can support substitute search.

### 7.7 Cost-effectiveness and case-study result

Once price proxies and clusters are combined, the notebooks can identify lower-cost candidates within technically similar groups. This is exactly the type of intermediate output needed for a future recommendation system.

---

## 8. Strengths of the project

1. **Strong problem decomposition**  
   The project correctly separates supervised cost prediction from unsupervised materials discovery.

2. **Good data-engineering discipline**  
   The cleaning stages remove leakage, reduce redundancy, and save reusable intermediate datasets.

3. **Appropriate metric selection**  
   The evaluation design matches the actual task type.

4. **Transparent uncertainty handling**  
   The price-proxy confidence labels make the materials pipeline much more credible.

5. **Operational relevance**  
   The case-study notebook makes the results understandable to non-technical stakeholders.

---

## 9. Limitations and what they mean

### 9.1 TED contract value is not the same as material cost

A contract award value reflects labour, overhead, logistics, contractor margin, scale, and scope, not just materials. That means the TED model predicts **project-level procurement spend**, not direct bill-of-materials cost.

### 9.2 Title translation may introduce semantic drift

Machine translation improves consistency, but technical procurement wording can still shift subtly in translation. That means text-derived signals should be seen as useful but imperfect.

### 9.3 Proxy prices are not finished-goods prices

World Bank commodity series capture broad market prices, not the full commercial price of a fabricated engineering component. That is why the proxy-confidence layer is so important.

### 9.4 Cluster membership does not guarantee substitutability

Two materials can be similar in numeric feature space without being interchangeable in every engineering context. Human or domain validation would still be required before acting on a recommendation.

### 9.5 Time-aware validation could be added

A random train/test split is acceptable for a first pass, but a future version could test **time-based validation** to better simulate forward-looking procurement prediction.

---

## 10. Recommendations for how to present this in a thesis, article, or dissertation chapter

A strong write-up should present the project as a **hybrid predictive and exploratory analytics pipeline**. The TED notebooks answer the question of **what project value can be predicted**, while the materials notebooks answer the question of **what technically similar lower-cost materials might exist when direct pricing is sparse**.

The strongest framing is:

1. **Problem statement:** cost estimation is difficult because procurement and materials information are disconnected.
2. **Stage 1:** learn project-level cost from TED.
3. **Stage 2:** build a material-similarity and proxy-pricing engine.
4. **Stage 3:** demonstrate case-based decision support.
5. **Discussion:** explain strengths, uncertainty, and deployment limitations.

That structure makes the project look integrated rather than like separate experiments.

---

## 11. Final conclusion

This project successfully builds a multi-notebook analytical system that addresses a realistic and difficult data problem: combining procurement records with materials intelligence when the two data worlds do not join neatly.

The procurement side shows that contract award value can be predicted from cleaned TED metadata with meaningful accuracy, especially using Random Forest on a log-transformed target. The materials side shows that a cleaned technical materials dataset can be enriched with proxy prices, organised by clustering, and turned into plausible substitute-search logic. The final case-study stage demonstrates how these pieces can support practical decision-making.

The project therefore answers its research question positively:

> Yes, public procurement and materials datasets can be combined into a useful analytical pipeline for cost estimation and material-substitution exploration, provided the results are interpreted as decision support rather than exact engineering or commercial truth.

That is a strong project outcome because it is not only predictive, but also explainable, modular, and extensible.

---

## References

[1] Systematic review article on machine-learning methods for construction cost estimation (used to relate this project to broader cost-estimation research).

[2] Article on materials informatics and machine-learning-driven materials discovery (used to relate the clustering pipeline to existing materials analytics research).

[3] European Data Portal / TED dataset documentation describing TED as a public procurement data resource.

[4] World Bank Commodity Markets / Pink Sheet documentation describing the commodity price series used as proxy inputs.

[5] Scikit-learn metrics documentation distinguishing regression metrics from clustering and classification metrics.

[6] Scikit-learn `accuracy_score` documentation confirming accuracy as a classification metric rather than a regression metric.

[7] Scikit-learn `silhouette_score` documentation and the underlying silhouette formulation.

[8] Scikit-learn `davies_bouldin_score` documentation.

[9] Scikit-learn `calinski_harabasz_score` documentation.

[10] Scikit-learn DBSCAN documentation explaining density-based clustering and its ability to identify noise.
