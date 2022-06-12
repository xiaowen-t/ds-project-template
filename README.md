# Basic structure
```
root
├── data                      
|   ├──raw                    
|   └── processed             <- Data ready for modeling.
│
├── notebooks                 <- Jupyter notebooks.
|   └── 0.0-name-description.ipynb
│
├── reports                   <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── src                       <- Source code for use in this project.
|   ├── data                  <- Scripts to prepare data
|   ├── model                 <- Scripts to train models
|   ├── utils                 <- Helper functions for use in this project.
|     ├── data
|     └── model  
|   └── tests                 <- Testing functions with the same structure in /src 
|     ├── test_utils.py                
|     ├── test_data.py                  
|     ├── test_model.py                
|     └── ...
│
└── requirements.txt
```

# Others
```
root  
├── docs              <- Sphinx or MKDocs?
│
├── setup.py          <- Make this project pip installable with `pip install -e`
└── tox.ini
```
