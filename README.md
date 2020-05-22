<p align="center">
<img width="250" height="250" src="opt_out_logo.png">
</p>

# Opt Out Tools Machine Learning R&D Repository

Welcome to the **Opt Out Tools (OOT)** Machine Learning
R&D repository.
This repository contains the research and the production
code allowing us to build a machine learning model for
the automatic detection of online misogyny on Twitter.

A first version of this model is currently in use in the
**Opt Out**
[browser extension](https://github.com/opt-out-tools/opt-out).
The extension is currently itself in its alpha version and
available for download in the
[Firefox add-ons library](https://addons.mozilla.org/en-US/firefox/addon/opt-out-tools/).
A data statement of the dataset used for the first version
of the model can be found on **OOT's**
[website](https://www.optoutools.com/tech).

Please read the [CONTRIBUTING.md](./CONTRIBUTING.md) file
in this repository to know how you can contribute to it.

Quick links:

- [Repository purpose](#Repository-purpose)
- [Repository structure](#Repository-structure)
- [Repository management](#Repository-management)
- [Repository status](#Repository-status)
- [Code of conduct](#Code-of-conduct)

## Repository purpose

This repository has two purposes:

- Researching online misogyny automatic detection, i.e. exploring
  hate speech datasets and experimenting with machine learning
  algorithms.
- Building a machine learning model for the browser extension
  based on our research.

## Repository structure

    ├── .circleci               <- CircleCI configuration for this repository.
    │                              repository.
    ├── data                    <- Folder containing data, raw or processed.
    │
    ├── docs                    <- Code documentation
    │
    ├── models                  <- Trained and serialized models.
    ├── notebooks               <- Folder for Jupyter notebooks.
    ├── reports                 <- Pipeline metrics and reports
    │
    ├── src                     <- Source Python code for the ML pipeline.
    │
    ├── stages                  <- DVC files describing the ML pipeline.
    ├── tests                   <- tests for the machine learning pipeline
    │
    ├── .flake8                 <- Flake8 configuration file.
    ├── .pre-commit-config.yaml <- Pre-commit configuration file.
    ├── .pylintrc               <- PyLint configuration file.
    ├── CONTRIBUTING.md         <- Instructions on how to contribute to this repository.
    ├── Dvcfile                 <- Configuration for final stage (i.e evaluation stage) of the ML pipeline.
    ├── LICENSE                 <- License file.
    ├── README.md               <- General information about this repository.
    ├── mypy.ini                <- MyPy configuration file.
    ├── opt_out_logo.png        <- Logo used in the README of this repository.
    ├── requirements.txt        <- Python dependencies file.
    └── setup.py                <- Python package installation file.

## Repository management

This repository is managed by the **Opt Out Tools** data team.
If you have any question, please reach out to one of the
following members of the team on Github:

- Andrada: `andra-pumnea`
- Verena: `Ver2307`

## Repository status

We use [CircleCI](https://circleci.com/) for
[CI/CD](https://en.wikipedia.org/wiki/CI/CD).
You can always check if anything is broken in the repository
in this section.

Current status:
[![CircleCI](https://circleci.com/gh/opt-out-tools/model-online-misogyny.svg?style=svg)](https://circleci.com/gh/opt-out-tools/model-online-misogyny)

**NOTE: We do not currently have an automated model
deployment mechanism.**

## Code of conduct

Please note that this repository is part of the **Opt
Out Tools** project which is released with a
[Contributor Code of Conduct](https://github.com/opt-out-tools/opt-out/blob/master/CODE_OF_CONDUCT.md).
By participating in this project you agree to abide by its terms.

--------

<p><small>Project structure based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
