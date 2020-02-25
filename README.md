<p align="center"> <img width="250" height="250" src="opt_out_logo.png"> </p>

<p></p> <h1 align="center"> Opt Out Tools </h1>
<p></p> <h2 align="center"> Open Source Modeling - Research & Production Code </h2>

Quick links:

- [Repository Structure](#Repository-Structure)
- [Purpose of the Repository](#Purpose-of-the-Repository)
- [How the Repository Works?](#How-the-Repsitory-Works?)
- [Use the Repository](#Use-the-Repository)
- [Code of Conduct](#Code-of-Conduct)


Repository Structure
------------

    ├── CONTRIBUTING.md    <- How to contribute to this repository
    ├── README.md          <- The top-level desciption for people interested
    ├── data               <- Our dataset. Access credentials required
    │    
    ├── models             <- Trained and serialized models fit for production
    │
    ├── notebooks          <- Jupyter notebooks. 
    │    
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.                     
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
    |
    ├── opt_out_logo.png   <-  Our logo
    ├── mypy.ini           <-  Used for static typing
    └── LICENSE            


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

Purpose of the Repository
--------------------
There are three purposes of this repo
- Open source research into online misogyny
- Using this research to build a production model for the browser extension
- (Long-term) develop a toolkit for identifying misogyny

How the Repository Works?
--------------------
### Research
The research will be carried out in notebooks. This will be used to
communicate results initially. Naming convention is a number (for ordering), 
the creator's initials, and a short `-` delimited description, e.g.
`1.0-jqp-initial-data-exploration`. Folders within the notebooks directory
 are named based on the type of model being studied.
 
For further information about contributing research and the PR process, please 
see [CONTRIBUTING.md](https://github.com/opt-out-tools/study-online-misogyny/blob/documentation/CONTRIBUTING.md).

### Production 
Once our research has culminated in a model that we believe is production
ready, it then needs to be implemented with a common API so we can deploy
it easily. This currently is only a .predict() function, but is subject to
change in the coming month.
 
### Toolkit 
The long-term vision for this repo is to develop a toolkit for identifying
/studying online misogyny with the code written in src/ folder. Currently
this folder contains preprocess pipelines, error analysis scripts and
acceptance criteria scripts.

To understand the finer details of how this works, please see the [CONTRIBUTING
.md](https://github.com/opt-out-tools/study-online-misogyny/blob/documentation/CONTRIBUTING.md)


Use the Repository
--------------------

## Datasets
The text must be under the column head **text** and the labels under the column 
head **label**. Misogynistic or harassing is always 1 and not 0. Only dataset 
with open access is stanford. Please ask about others.

```
hatespeech - obtained from Zeerak Waseem. 
aws_annotated - our annotations + hatespeech
stanford_hatespeech - stanford (aws_annotated+snorkel labels) + hatespeech
gold - stanford_hatespeech + AMI
metoo - tweet ids from https://github.com/datacamp/datacamp-metoo-analysis
rapeglish - scraped from random rape threat generator by Emma Jane
dataturks - obtained from dataturks crowdsource labeling
```

## Installation

#### Conda

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

#### Spacy Model

```bash
python -m spacy download en_core_web_md
```

#### Pre-commit Hooks

```bash
pre-commit install
```

## Tests

Tests should be run from the root directory as
```bash
python -m pytest
```

## Get the latest Model/Dataset
We are using [dvc](https://dvc.org/) for this. 

Initially we're just using DVC to provide a basic useful framework to track, 
save and share models and large data files.
 
Eventually to achieve full reproducibility, we'll have to connect code and 
configuration with the data it processes to produce the result. 


To get the model:
1) Check `dvc` is installed
```
 dvc --version   
```
2) Add the s3 bucket as a remote if not already there
```
dvc remote add -d myremote s3://opt-out-tools-models/models
dvc remote modify myremote region eu-central-1
```
3) Pull the cache  of the models from the s3 bucket
```
dvc pull
```
4) Checkout the `.dvc` of the model
```
dvc checkout <model_filename>.dvc
```
## Add a new Model/Dataset

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

## Rerun Model building
Coming soon


## Code of Conduct

> Please note that this project is released with a [Contributor Code of 
Conduct](https://github.com/malteserteresa/opt-out/blob/master/CODE_OF_CONDUCT.
md). By participating in this project you agree to abide by its terms.
