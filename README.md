<p align="center"> <img width="250" height="250" src="opt_out_logo.png"> </p>

# Opt Out Tools

## Open Source Modeling - Research & Production Code

Welcome to the Opt-Out-Tools (OOT) Machine-Learning R&D repository.

Quick links:

- [Repository Structure](#Repository-Structure)
- [Purpose of the Repository](#Purpose-of-the-Repository)
- [How the Repository Works](#How-the-Repository-Works)
- [Dependencies](#Dependencies)
- [Run the ML Pipeline](#Run-the-ML-Pipeline)
- [Code of Conduct](#Code-of-Conduct)

## Repository Structure

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
    ├── setup.py           <- makes project pip-installable
    ├── src                <- Source code for use in this project.
    │   │
    │   └── text  <- Utility modules for text processing
    │       └── visualize.py
    |
    ├── opt_out_logo.png   <-  Our logo
    ├── mypy.ini           <-  Static type-checking configuration
    └── LICENSE            

## Purpose of the Repository

There are three purposes of this repo:

- Open source research into online misogyny
- Using this research to build a production model for the browser extension
- (Long-term) develop a toolkit for identifying misogyny

## How the Repository Works

### Research

The research will be carried out in notebooks.
This will be used to communicate results initially.
Naming convention is a number (for ordering), the creator's initials,
 and a short `-` delimited description, e.g.
`01-jqp-initial-data-exploration`.
Folders within the notebooks directory are named based on
the type of model being studied.

For further information about contributing research and
the PR process, please see
[CONTRIBUTING.md](https://github.com/opt-out-tools/study-online-misogyny/blob/documentation/CONTRIBUTING.md).

### Production

Once our research has culminated in a model that we believe is production
ready, it then needs to be implemented with a common API so we can deploy
it easily. This currently is only a .predict() function, but is subject to
change in the coming month.

### Toolkit

The long-term vision for this repo is to develop a toolkit for
identifying/studying online misogyny.
Currently the code runs preprocessing pipelines, error analysis scripts and
acceptance criteria scripts.

To understand the finer details of how this works, please see
[CONTRIBUTING.md](https://github.com/opt-out-tools/study-online-misogyny/blob/documentation/CONTRIBUTING.md)

## Dependencies

### Data

Please reach out to OOT ask about our golden dataset.
The dataset destination path is
`data/gold_data_en.csv`.
This has to be exact for the ML pipeline to wor correctly.

### Software

**NOTE: All commands in this section are required to
run successfully in order for you to contribute
to this repository.**

#### Python

Create a new Conda environment

```
conda create -n som python=3.7
```

and activate it with

```bash
conda activate som
```

(you can alternatively create an environment with `virtualenv`
but your mileage may vary).

Move to the project root directory (e.g. `$ cd study-online-misoginy/`)
and install package dependencies as follows:
```bash
pip install -r requirements.txt
```

#### Spacy Model

There is a separate command for downloading the Spacy language model
needed for our ML pipeline:
```bash
python -m spacy download en_core_web_md
```

#### Pre-commit Hooks

Pre-commit will make sure that the code we commit is
kosher or close enough:
```bash
pre-commit install
```

### Tests

Tests should be run from the root directory as

```bash
python -m pytest
```

## Run the ML pipeline

We are using [DVC](https://dvc.org/) to track and manage our
machine-learning workflow.

Once the repository is set up, one should be able to run:

```
dvc repro
```

This will run the full pipeline, from preprocessing to evaluation of the
model on the test data.
This will also update the pipeline every time there is a new change to
the code that affects it.

To check if the pipeline is up to date run

```
dvc status
```

### Visualize the pipeline

The pipeline can be visualized in ASCII art with the following command:

```
dvc pipeline show --ascii
```

which will visualize the DVC files responsible for each stage and their
mutual connection.
The default (and final) stage is the evaluation stage, which is specified
in `Dvcfile`.
All other DVC files can be found in the `stages/` folder.

### Visualize metrics

Metrics are defined within the DVC pipeline and can be visualize
(for the current branch) with the command:

```
dvc metrics show
```

One can get a quick comparison with all others experiment in the repo
with a similar command:

```
dvc metrics show -a
```

### Pipeline modifications

A generic modification of the pipeline should focus on the Python source
in `src/`, most notably `featurize.py` or `train.py`.

To have a closer look at the pipeline setup investigate the DVC files in
the `stages/` folder or run

```
dvc pipeline show --ascii -c stages/train.py
```

## Code of Conduct

Please note that this project is released with a
[Contributor Code of Conduct](https://github.com/malteserteresa/opt-out/blob/master/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.

--------

<p><small>Project structure based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
