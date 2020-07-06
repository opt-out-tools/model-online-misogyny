# Contributor's Guide

The purpose of this guide is to help you contribute to
this repository.

Quick links:

- [Requirements](#Requirements)
- [Start to Contribute](#Start-to-contribute)
- [Issues](#Issues)

## Requirements

### OOT dataset

To work on this repository, you might need the
**OOT** dataset.

Please contact one of the maintainers to obtain the dataset.

### Repo download and setup

Please follow the below steps to set up the repository
on your local disk:

1. [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
   the repository and
   [clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
   the forked repository on your local disk.
1. Copy the **OOT** dataset in the `data` folder of the repository and
   rename it to `gold_data_en.csv`.

### Dependencies

1. *(optional but strongly recommended)* Make sure you have
   _conda_ installed (you can get it with the
   [Anaconda distribution](https://www.anaconda.com/products/individual#Downloads))
   and then follow these steps:

   - In your terminal, create a new Conda environment:

     ```bash
     conda create -n model-online-misogyny python=3.8
     ```

   - Activate the environment using the following command:

     ```bash
     conda activate model-online-misogyny
     ```

1. At the root of the repository, install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. Run the following command to set up the
   pre-commit scripts:

   ```bash
   pre-commit install
   ```

1. (optional, depending on the pipeline setup) download the spaCy
   language model needed for our machine
   learning pipeline with the following command:

   ```bash
   python -m spacy download en_core_web_md
   ```

Congratulations, you're all set!

## Start to contribute

You can contribute in many ways to this repository.
Most of the times your written contribution will be
in the form of Jupyter Notebooks, Python code, or documentation.

Once you've decided what to work on (see [Issues](#Issues)),
the standard GitHub workflow is the following:

1. Start working on a new branch, on a fork of the repo
   you have previously created;
1. Once you're satisfied with your work, open a
   [pull request](#pull-requests)
   (PR) from your branch to the original repo's `master`
   branch, asking for a review of your changes.
1. If your PR stems from a discussion in an issue
   on the repository page, it's good practice to add as reviewer
   one of the maintainers who might have given you permission
   within that context.
   Otherwise, the maintainers will take care of assigning the
   review of the PR for you.
1. Answer and address any comment reviewers add to your PR.
1. Once your PR is approved and has passed all CI checks,
   it will be merged to the main branch.


### Pull requests

Creating a
[pull request (PR)](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
is the formal act of asking to integrate your work with
the main trunk of the code repository.
When you create a PR, make sure to:
1. Give it a helpful title that summarizes what your contribution
  does.
  If you expect to do more work on your PR before
  receiving a full review, you may prefix the title with
  `WIP:` and remove it when it is ready to be merged.
1. Add a description with all relevant information on the
  changes you made and anything you deem noteworthy.
  Every little bit helps!
1. If the PR fixes an existing issue, add a line to the description
  of the PR that addresses that.
  Usually you just need to add a single line stating
  `Fixes #<ISSUE_NUMBER>` or `Closes #<ISSUE_NUMBER>`
  where `ISSUE_NUMBER` should be replaced by the actual number
  of the issue.
  See also [this link](https://help.github.com/en/enterprise/2.16/user/github/managing-your-work-on-github/closing-issues-using-keywords)
  for more info on the subject.
1. Assign one or several reviewers to your PR.

### Jupyter notebooks

Jupyter notebooks are a great way to quickly experiment
and prototype.
Jupyter notebooks should be self-contained experiments
that later lead to Python code for the repo.
While we encourage experimenting with notebooks,
we'll try to keep a standard of readability and
accessibility for the notebooks available on the
repo.
Beside the Python code, the most important part of a
a notebook is the text accompanying the code.
It is important that a notebook is regarded as a sort
of _interactive article_ that people can read and, if they
want, modify and play with.

Here are a few points to keep in mind when dealing
with notebooks:

1. If you'd like to take an existing notebook and expand from
   that, create a copy of that notebook and work on your own
   copy.
   **Never modify and existing notebook** unless you are
   working on a specific fix.
1. Carry out your research.
1. Once you have finished your experiment, produce a notebook that
   clearly illustrates the results of your research with a
   comparison to baselines/benchmarks and acceptance criteria.
   The name of your notebook(s) must contain, in the
   following order, progressive number (for
   chronological ordering), your initials, and short title
   (e.g. `01-jqp-initial-data-exploration`).
   This is particularly important if your work is divided
   among multiple notebooks.
   
   
All notebooks should be contained in the dedicated
`notebooks` folder.

### Python code

If your work pertains directly to the machine-learning
pipeline, you'll be mostly working with code in the
`src` directory.
Once you're satisfied with your work, run the
machine-learning pipeline with the following command:

```bash
dvc repro
```
this will re-run the ML pipeline with your new modifications
and will allow you to see any performance differences.
For more information on how to use DVC, please see
[DVC.md](references/DVC.md).

You can also run tests using this command:

```bash
python -m pytest
```


### Documentation

At the moment we haven't settled for a Documentation
platform.
All documentation should be found in this repo in the `references`
folder until a decision is made.


## Issues

### Submitting an issue

We use Github issues to track all bugs and feature requests,
feel free to
[open](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue)
one if you have found a bug or wish to request a feature.

Before submitting an issue, please verify that your issue
is not being currently addressed by other issues
or pull requests.

#### Notes on bug reports

When submitting a bug report, please try and:

- Include a short reproducible code snippet.
  If your snippet is longer than 50 lines, please link to a
  gist or a Github repo.
  If you cannot include a reproducible snippet, please be
  specific about the models, data and functions involved
  in the bug.
- Provide the full traceback if an exception is raised.


### Finding an issue to work on

One great way to help the project is to pick open issues and
contribute to fix them.

You can find open issues on the
[Repository Issues tab](https://github.com/opt-out-tools/model-online-misogyny/issues)

When choosing an issue to work on:

- If the issue is unassigned, comment on the issue that you
  would like to take care of it and someone in the data team
  will assign it to you.
- If the issue is already assigned to someone, it's a good
  idea to contact that person on Slack or Github to see
  how you can work with them.

Once you are assigned on an issue:

- Make sure to check the full discussion on the issue
  before starting to work.
- Add to the discussion and ask for clarification if needed.


## About the software we use

- [Jupyter Notebook](https://jupyter.org/install)
- [Python](https://www.python.org/downloads/)
- [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [pre-commit](https://pre-commit.com/#install)
- [spaCy](https://spacy.io/usage)
- [DVC](https://dvc.org/doc/install)
