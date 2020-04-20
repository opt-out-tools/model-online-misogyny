# Contributor's Guide

The purpose of this guide is to help you contribute to this repository.

Quick links:

- [Setting up the repository](#Setting-up-the-repository)
- [Finding an issue to work on](#Finding-an-issue-to-work-on)
- [Working on a research issue](#Working-on-a-research-issue)
- [Working on a code issue](#Working-on-a-code-issue)
- [Submitting an issue](#Submitting-an-issue)

## Setting up the repository

Please follow the below steps to set up the repository on your local disk:

1. Make sure your local environment meets the [software requirements](./README.md#Software-requirements)
for working with this repository.
2. [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
the repository and
[clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
the forked repository on your local disk.
4. In your terminal, use the following command to create a new Conda environment:

```bash
conda create -n som python=3.7
```

5. Activate the environment using the following command:

```bash
conda activate som
```

6. At the root of the repository, install the dependencies with the below command:

```bash
pip install -r requirements.txt
```

7. Download the spaCy language model needed for our machine learning pipeline with the following command:

```bash
python -m spacy download en_core_web_md
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
- **Ask for clarification from the person who created the issue if needed.**
- Make sure to add a `[WIP]` label in the issue title once you start actively
working on the issue.

## Working on a research issue

### Dataset research

### Algorithm research

<!-- The PR checklist:

1) Correct naming convention of branch/notebooks/scripts
2) Sufficiently novel to be merged, otherwise will stay on branch
3) Notebook is in correct folder
4) Clear illustration of results: comparison to baselines/benchmarks and acceptance criteria


If you have written a function that you think _"wow that is so great/useful
I think others should have access to it"_ then this brilliant piece of code
belongs in the src/ folder! Please see the toolkit heading for contributing
this code.-->


## Working on a code issue

Please follow the below steps if your issue is code-related:

1. In your local copy of the repository, create a branch to take care of the issue
using the following naming convention for the branch:
  - For feature implementations/enhancements: `feature/<issue-number>-<descriptive_name>`
  - For bug fixes: `fix/<descriptive_name>`
2. Work in your branch in the `src` folder until you are satisfied with your code.
3. Once you're satisfied with your code, run the machine learning pipeline with the following command:

```bash
dvc repro
```

4. If the machine learning pipeline runs without any problem, document your code
in the `docs` folder of this repository and make sure the documentation renders properly.
5. Submit a [pull request (PR)](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) for your issue. Make sure to:
  - Prefix your PR with an `[MRG]` label and give it a helpful title that summarizes
    what your contribution does. If you expect to do more work on your PR before
    receiving a full review, prefix it with a `[WIP]` label and change it to `[MRG]`
    when it matures.
  - Reference the issue the PR addresses in the description of the PR.
  - Either reference your research in the `notebooks` and/or `reports` folder of this
    repository or to sufficiently cited research papers to support the proposed
    algorithm in the description of the PR.
  - Assign one or several reviewers to your PR. If you do not know anyone in the
    data team, please assign one of the people listed in [Repository management](./README.md#Repository-management).
6. Answer and address any comment reviewers add to your PR.
7. Once your PR is approved by a reviewer and has passed all CI checks, **merge it
to the current release branch, not to `master`**. **NOTE:** If merging your PR
means that some other issues/PRs should be closed, please use [keywords](https://help.github.com/en/enterprise/2.16/user/github/managing-your-work-on-github/closing-issues-using-keywords) to close them at the same time (e.g., "Fixes #1234"; multiple issues/PRs are allowed as long as
each one is preceded by a keyword). If your PR is simply related to some other
issues/PRs, create a link to them without using the keywords (e.g., "See also #1234").
Congratulations, you have contributed code to the **OOT** project!

## Submitting an issue

We use Github issues to track all bugs and feature requests, feel free to [open](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue)
one if you have found a bug or wish to request a feature.

Before submitting an issue, please do the following:

- Verify that your issue is not being currently addressed by
other issues or pull requests.
- Read the instructions on how to write a feature request or a bug report in the
sections below.

### How to write a feature request

When submitting a feature request, please try and:

- Be clear as possible.
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
