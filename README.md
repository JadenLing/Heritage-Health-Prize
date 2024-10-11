# **Heritage-Health-Prize**
[COMP90051] Statistical Machine Learning - Assignment 3 - 2024 - Semester 2 
_____________________________

**Authors**: 
- Brian King 
- Jaden Ling
- Rasindu Samaranayake

## Running Instructions

### Prerequisites: 
**Python 3.12.4** is required for all notebooks.

Pandas, SciKit-Learn, PyTorch, [SeaBorn](https://seaborn.pydata.org/) (https://seaborn.pydata.org/) and [XGBoost](https://xgboost.readthedocs.io/en/stable/) (https://xgboost.readthedocs.io/en/stable/) are required to run the notebooks in this repository.

### Generating Preprocessed Data:
If missing, create directories `./data` in the root directory of the repository. Within this directory, create the following; 
- `./data/curated`
- `./data/raw`
- `./data/preprocessed`

From [ForeverData](https://foreverdata.org/1015/index.html) (https://foreverdata.org/1015/index.html), download `Release 3.zip`, and extract this data into `./data/raw`.

Run notebook `preprocess.ipynb` in `./notebooks`. This should populate `./data/curated` and `./data/preprocessed` with several CSV files. Note that `prp_combined_Y1.csv` and `prp_combined_Y2.csv` contain the final training and testing data respectively.

### Executing Models:
`./notebooks` contains `random_forests.ipynb`, `xgboost_model.ipynb` and `logistic_regression_final.ipynb`. Each model and their outputs will be contained within these Jupyter Notebooks. 
