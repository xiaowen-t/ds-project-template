# Data Science Project Template
This project aims to provide a standardized template for data science projects that ensures correctness and reproducibility. 
## Best practices
### Ensuring Correctness
- Data Validation
  - Use [Pandera](https://pandera.readthedocs.io/en/stable/) or other validation tools to ensure data accuracy, consistency, completeness, and format.
- Code Validation
  - Use unit testing to test code functionality.
  - Use PEP8 or other coding conventions to ensure coding style consistency.
  - Conduct code reviews to ensure code readability, maintainability, and correctness.
- Uncertainty Quantification
  - Quantify parameter uncertainty, structural uncertainty, and experimental uncertainty.
### Ensuring Reproducibility
- Consistent data
    - consistent raw data
      - Use consistent raw data, including time frame and data provenance.
      - Use consistent processing pipelines to transform the data.
    - consistent processing pipelines
- Consistent model 
    - Use fixed random seeds for the model to ensure that the results are replicable.
    - Use consistent hyperparameters.
- Documentation
  - Data, Assumptions, Methods, Parameters, Results, Limitations, Interpretation.

## Structure
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
2. [Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)