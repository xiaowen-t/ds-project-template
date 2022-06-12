# Essentials
Based on [cookiecutter data science project structure](https://drivendata.github.io/cookiecutter-data-science/).
```
root
├── data                      
|   ├── raw                    
|   └── processed             <- Data ready for modeling.
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
├── requirements.txt
└── .gitignore
```

# More
```
root  
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── setup.py           <- Make this project pip installable with `pip install -e`
├── docs               <- Sphinx or MKDocs?
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
└── tox.ini            <- Automate and standardize testing
```
