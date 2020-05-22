# Contributor's Guide

The purpose of this guide is to help you contribute to
this repository.

Quick links:

- [Requirements](#Requirements)
- [Finding an issue to work on](#Finding-an-issue-to-work-on)
- [Working on a research issue](#Working-on-a-research-issue)
- [Working on a modeling issue](#Working-on-a-modeling-issue)
- [Submitting an issue](#Submitting-an-issue)

## Requirements

### OOT dataset

To work on any type of issue in this repository, you need the
**OOT** dataset.

Please follow the below instructions to request it:

__TODO:__ Add a way to obtain a/the dataset.

*TBD*

### Install dependencies

Please follow the below steps to set up the repository on your local disk:

1. Make sure you have requested the [**OOT** dataset](#OOT-dataset).
1. [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
   the repository and
   [clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
   the forked repository on your local disk.
1. Copy the **OOT** dataset in the `data` folder of the repository and
   rename it to `gold_data_en.csv`.

1. (_optional but strongly recommended_) Make sure you have _conda_ installed
   (you can get it with the
   [Anaconda distribution](https://www.anaconda.com/products/individual#Downloads))
   and then follow these steps:

   - In your terminal, use the following command to create a new
     Conda environment:

     ```bash
     conda create -n model-online-misogyny python=3.8
     ```

   - Activate the environment using the following command:

     ```bash
     conda activate model-online-misogyny
     ```

1. At the root of the repository, install the dependencies with
   the below command:

   ```bash
   pip install -r requirements.txt
   ```

1. Download the spaCy language model needed for our machine
   learning pipeline with the following command:

   ```bash
   python -m spacy download en_core_web_md
   ```

1. Run the following command to set up the
   pre-commit scripts:

   ```bash
   pre-commit install
   ```

Congratulations, you're all set!

## Finding an issue to work on

You can find issues to work on in the following places:

- [Data team project board](https://github.com/orgs/opt-out-tools/projects/41)
- [Repository Issues tab](https://github.com/opt-out-tools/model-online-misogyny/issues)

When choosing an issue to work on:

- If the issue is unassigned, comment on the issue that you would like to take
care of it and someone in the data team will assign you.
- If the issue is already assigned to someone, contact that person on Slack or
Github to see how you can work with them.

Once you are assigned on an issue:

- Make sure to check all comments on the issue before starting to work.
- Ask for clarification from the person who created the issue if needed.
- Create a branch and do your work on it.
- Push it to GitHub and submit a Pull Request when your
  contribution is ready.


**TODO: STREAMLINE AND SIMPLIFY THE PART THAT FOLLOWS**

**TODO: EXPAND AND COMPLETE DVC USAGE**

### Working on a research issue

Please follow the below steps if your issue is about researching and/or
analyzing a dataset or experimenting an algorithm:

1. Carry out your research on your machine using
   Jupyter Notebooks
2. Once you have finished your research, produce a notebook that clearly
   illustrates the results of your research with a comparison to
   baselines/benchmarks and acceptance criteria.
   The name(s) of your notebook(s) must contain, in the following order,
   progressive number (for ordering), your initials, short description
   (e.g. `01-jqp-initial-data-exploration`).
3. In your local copy of the repository, create a branch using the
   following naming convention for the branch:
   `research/<issue-number>-<descriptive_name>`
4. Copy your notebook in the `notebooks` folder of the repository and
   push it to your branch.
5. Submit a
   [pull request (PR)](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
   for your issue.
   Make sure to:
   - Give it a helpful title that summarizes what your contribution does.
     If you expect to do more work on your PR before
     receiving a full review, prefix it with a `[WIP]` label and
     remove it when it is ready to be merged.
   - Reference the issue the PR addresses in the description of the PR.
   - Assign one or several reviewers to your PR.
     If you do not know anyone in the data team, please assign one
     of the people listed in
     [Repository management](./README.md#Repository-management).
4. Answer and address any comment reviewers add to your PR.
5. Once your PR is approved by a reviewer and has passed all CI checks,
   the reviewer or an admin of the repo merges it to the current release.

**NOTE:** If merging your PR means that some other issues/PRs
should be closed, please use
[keywords](https://help.github.com/en/enterprise/2.16/user/github/managing-your-work-on-github/closing-issues-using-keywords)
to close them at the same time (e.g., "Fixes #1234";
multiple issues/PRs are
allowed as long as each one is preceded by a keyword).
If your PR is simply related to some other issues/PRs, create a link
to them without using the keywords (e.g., "See also #1234").

Congratulations, you have contributed research to the **OOT** project!

### Working on a modeling issue

Please follow the below steps if your issue is about implementing or
enhancing a code feature (e.g. new algorithm, algorithm enhancement,
 pipeline workflow enhancement, etc.) or fixing a code bug:

1. In your local copy of the repository, create a branch to
   take care of the issue using the following naming
   convention for the branch:
  - For feature implementations/enhancements:
    `feature/<issue-number>-<descriptive_name>`
  - For bug fixes: `fix/<issue-number>-<descriptive_name>`
2. Work in your branch in the `src` folder until you are
   satisfied with your code.
3. Once you're satisfied with your code, run the
   machine-learning pipeline with the following command:

   ```bash
   dvc repro
   ```
   For more information on how to use DVC, please see [DVC.md](references/DVC.md).

   4. Run the tests to check your code works with the machine learning pipeline using
   this command:

   ```bash
   python -m pytest
   ```

5. If the machine learning pipeline and the tests run without any
   problem, document your code using
   [Sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html).
   Make sure your documentation renders properly and save the generated
   reports in the `reports` folder of this repo.
6. Submit a
   [pull request (PR)](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
   for your issue.
   Make sure to:
   - Give it a helpful title that summarizes what your contribution does.
     If you expect to do more work on your PR before
     receiving a full review, prefix it with a `[WIP]` remove it
     when it matures.
   - In the description of the PR, reference:
      - The issue the PR addresses.
      - Your own research saved in the `notebooks` folder of this
        repository or sufficiently cited research papers to support
        the proposed algorithm.
      - Your code documentation saved in the `reports` folder of
        this repository.
   - Assign one or several reviewers to your PR.
     If you do not know anyone in the data team, please
     assign one of the people listed in
     [Repository management](./README.md#Repository-management).
7. Answer and address any comment reviewers add to your PR.
8. Once your PR is approved by a reviewer and has passed all
   CI checks, the reviewer or an admin of the repo merges it
   to the current release.

**NOTE:** If merging your PR means that some other
issues/PRs should be closed, please use
[keywords](https://help.github.com/en/enterprise/2.16/user/github/managing-your-work-on-github/closing-issues-using-keywords)
to close them at the same time (e.g., "Fixes #1234";
multiple issues/PRs are allowed as long as each one is
preceded by a keyword).
If your PR is simply related to some other issues/PRs, create
a link to them without using the keywords (e.g., "See also #1234").

Congratulations, you have contributed code to the **OOT** project!

## Submitting an issue

We use Github issues to track all bugs and feature requests,
feel free to
[open](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue)
one if you have found a bug or wish to request a feature.

Before submitting an issue, please do the following:

- Verify that your issue is not being currently addressed by
other issues or pull requests.
- Read the instructions on how to write a feature request or
  a bug report in the sections below.

### How to write a feature request

When submitting a feature request, please try and:

- Be as clear as possible.
- Include relevant documentation, wireframes, etc.

### How to write a bug report

When submitting a bug report, please try and:

- Include a short reproducible code snippet. If your snippet is longer than
50 lines, please link to a gist or a Github repo. If you cannot include a
reproducible snippet, please be specific about the models, data and functions
involved in the bug.
- Provide the full traceback if an exception is raised.
- Include your operating system type and version number, as well as your
language version (python, javacript) and other important packages such as
scikit-learn, numpy, and scipy.

### About the software we use

- [Jupyter Notebook](https://jupyter.org/install)
- [Python](https://www.python.org/downloads/)
- [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [pre-commit](https://pre-commit.com/#install)
- [spaCy](https://spacy.io/usage)
- [DVC](https://dvc.org/doc/install)
