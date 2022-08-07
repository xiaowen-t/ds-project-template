# Data Science Project Template
This project aims to build a common template that can guarantee the correctness and reproducibility of data science projects.  

It includes:
- A unified directory structure.
- Documents in each subdirectories.
- Example notebooks.
- Necessary utility and test functions.
## 1. Approach
### 1.1 Correctness
- Data Validation
  - [Pandera](https://pandera.readthedocs.io/en/stable/) or other tools
- Code Validation
  - Unit Testing
  - [PEP8](https://peps.python.org/pep-0008/) or other convention
  - Code reviews
- Assumption Verification
  - A/B Test
  - Endogenous feature
- Uncertainty Quantification
  - Parameter uncertainty
  - Structural uncertainty
  - Experimental uncertainty
### 1.2 Reproducibility
- Consistent data
    - consistent raw data
      - Time frame
      - Data Provenance
    - consistent processing pipelines
- Consistent model 
    - Fixed random seeds
    - Consistent hyperparameters
- Documentation
  - Keep a journal
  - Document ***why***

## 2. Basic Structure
Based on [cookiecutter data science project structure](https://drivendata.github.io/cookiecutter-data-science/).
```
project
├── data                      
|   ├── raw                       
|   ├── interim               <- Intermediate data that has been transformed.      
|   └── processed             <- Data ready for modeling
│
├── models                    <- Trained and serialized models.
|
├── reports                   <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── notebooks                 <- Jupyter notebooks.
|   └── 0.0-name-description.ipynb
│
├── src                       <- Source code for use in this project.
|   ├── __init__.py           <- Makes src a Python module
|   ├── data                  <- Scripts to prepare data
|   ├── model                 <- Scripts to train models
|   └── tests                 <- Unit testing
|     ├── test_data.py                  
|     ├── test_model.py                
|     └── ...
│
├── references                <- Data dictionaries, manuals, and all other explanatory materials.
│
├── requirements.txt          <- pip install requirements.txt
└── .gitignore
```

# More
```
project  
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── setup.py           <- Make this project pip installable with `pip install -e`
├── docs               <- Sphinx or MKDocs?
│
└── tox.ini            <- Automate and standardize testing
```

# Ref
1. [Cookiecutter data science project structure](https://drivendata.github.io/cookiecutter-data-science/).  
2. [Correctness in Data Science - Data Science Pop-up Seattle](https://www.slideshare.net/dominodatalab/data-science-popup-seattle-correctness-in-data-science).