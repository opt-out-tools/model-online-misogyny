<p align="center"> <img width="250" height="250" src="opt_out_logo.png"> </p>

# Opt Out Tools Machine Learning R&D Repository

Welcome to the **Opt Out Tools (OOT)** Machine Learning R&D repository. This
repository contains the research and production code allowing us to build the
model used by the **Opt Out** [browser extension](https://github.com/opt-out-tools/opt-out).
The extension is currently in its alpha version and available for download in the
[Firefox add-ons library](https://addons.mozilla.org/en-US/firefox/addon/opt-out-tools/).

Quick links:

- [Purpose of the repository](#Purpose-of-the-repository)
- [Repository structure](#Repository-structure)
- [Software requirements](#Software-requirements)
- [Repository management](#Repository-management)
- [Code of Conduct](#Code-of-Conduct)

## Purpose of the repository

There are three purposes of this repo:

- Researching online misogyny
- Building a production model for the browser extension based on our research
- Developing a toolkit for identifying online misogyny (long-term)

## Repository structure

    ├── .circleci               <- Folder containing the
    │                              [CircleCI](https://circleci.com/docs/2.0/about-circleci/#section=getting-started)
    │                              configuration file for this repository.
    ├── .dvc                    <- Folder containing the [DVC](https://dvc.org/doc/home) configuration file for this
    │                              repository.
    ├── .github/ISSUE_TEMPLATE  <- Folder containing templates to create different types of
    │                              [issues](https://github.com/opt-out-tools/model-online-misogyny/issues) for this
    │                              repository.
    ├── data                    <- Folder for documenting and analyzing datasets that tackle the problem of misogyny/hate speech and their labeling process, and
    │                              instructions on how to request them if necessary.
    ├── docs                    <- Folder containing the files necessary to produce documentation with
    │                              [Sphinx](https://www.sphinx-doc.org/en/master/).
    ├── models                  <- Folder for saving trained and serialized models fit for production.
    ├── notebooks               <- Folder for saving [Jupyter](https://jupyter.org/) notebooks (research folder).
    ├── reports                 <- Folder for saving data analysis in formats other than Jupyter (HTML, PDF, LaTeX, etc.).
    ├── src                     <- Folder containing the source code to train models. The source code currently
    │   │                          runs preprocessing pipelines, error analysis scripts and acceptance criteria
    │   │                          scripts.
    │   └── text                <- Folder containing the utility modules for text processing in the pipeline.
    ├── stages                  <- Folder containing the files necessary to run the machine learning pipeline.
    ├── tests                   <- Folder for saving tests for the machine learning pipeline to make sure that the source code works as expected.
    ├── .flake8                 <- ???
    ├── .gitignore              <- List of the files not to add to this repository when committing to it.
    ├── .pre-commit-config.yaml <- ???
    ├── .pylintrc               <- ???
    ├── CONTRIBUTING.md         <- Instructions on how to contribute to this repository.
    ├── Dvcfile                 <- ???
    ├── LICENSE                 <- Folder containing the license for use of this repository.
    ├── README.md               <- General information about this repository.
    ├── mypy.ini                <- ???
    ├── opt_out_logo.png        <- Logo used in the README of this repository.
    ├── requirements.txt        <- Requirements file for reproducing the analysis environment.
    └── setup.py                <- Installation file for the source code.

## Software requirements

### Python

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

### Spacy Model

There is a separate command for downloading the Spacy language model
needed for our ML pipeline:
```bash
python -m spacy download en_core_web_md
```

### Pre-commit Hooks

Pre-commit will make sure that the code we commit is
kosher or close enough:
```bash
pre-commit install
```

## Repository management

This repository is managed by the OOT data team. If you have any question,
please reach out to the following people on Github:

- Andrada: `andra-pumnea`
- Matteo: `teoguso`

## Code of conduct

Please note that this repository is part of the **Opt Out Tools** project which is released with a
[Contributor Code of Conduct](https://github.com/malteserteresa/opt-out/blob/master/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.

--------

<p><small>Project structure based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
