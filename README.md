Opt Out
==============================

Our study into online misogyny and how to model it

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
conda create -n som python=3.7
``` 
and activate it with
```bash
conda activate som
```
Move to the project root directory (e.g. `$ cd study-online-misoginy/`)
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

## ML versioning
We are using [dvc](https://dvc.org/) for this. 

Initially we're just using DVC to provide a basic useful framework to track, save and share models and large data files.
 
Eventually to achieve full reproducibility, we'll have to connect code and configuration with the data it processes to produce the result. This will come later.


To get the model:
1) Check `dvc` is installed
```
 dvc --version   
```
2) Add the s3 bucket as a remote if not already there
```
dvc remote add -d myremote s3://opt-out-tools-models/models
dvc remote modify mynewremote region eu-central-1
```
3) Pull the cache  of the models from the s3 bucket
```
dvc pull
```
4) Checkout the `.dvc` of the model
```
dvc checkout <model_filename>.dvc
```

To add a new version of the model. 

```
dvc add <model_filename>
```
This command should be used instead of git add on the model file. The above
command tells Git to ignore the directory and puts it into the cache (while 
keeping a file link to it in the workspace, so you can continue working the 
same way as before). This is achieved by creating a simple human-readable
`.dvc` that serves as a pointer to the cache.

We need to let git know about the `.dvc` file.
```
git add <model_filename>.dvc
git commit <model_filename>.dvc .dvc/config
git push
```
Finally we need to sync the model with the cloud storage. To do this, all we
need to run is the command below.
```
dvc push
```
Simples!

