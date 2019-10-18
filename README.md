Opt Out
==============================

Our study ito online misogyny and how to model it

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

Project Datasets
--------------------
The text must be under the column head **text** and the labels under the column head **label**. 
Misogynistic or harassing is always 1 and not 0. Only dataset with open access is stanford. Please ask about others.
```
hatespeech - obtained from Zeerak Waseem. 
aws_annotated - our annotations + hatespeech
stanford_hatespeech - stanford (aws_annotated+snorkel labels) + hatespeech
gold - stanford_hatespeech + AMI
metoo - tweet ids from https://github.com/datacamp/datacamp-metoo-analysis
rapeglish - scraped from random rape threat generator by Emma Jane
dataturks - obtained from dataturks crowdsource labeling
```

Installation
--------------------

### Conda

Create a new Conda environment
```
conda create -n find-out python=3.7
``` 
and activate it with
```bash
conda activate find-out
```
Move to the project root directory (e.g. `$ cd find-out/`)
and run the following command:
```bash
pip install -r requirements.txt
```

### Spacy Model

```bash
python -m spacy download en_core_web_md
```

### Pre-commit Hooks

```bash
pre-commit install
```

## Tests

Tests should be run from the root directory as
```bash
python -m pytest
```
