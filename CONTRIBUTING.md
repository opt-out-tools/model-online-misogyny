# Contributor's Guide

The purpose of this guide is to help you contribute to Opt Out Tools modeling,
regardless of your skill level or amount of time you are able to contribute.

Quick links:

- [Getting Started](#Getting-started)
- [Project Management](#Project-Management)
- [Feature Request/Bug Report](#Feature-Request/Bug-Report)
- [Contributing Code](#Contributing-Code)
- [Non Code Contributions](#Non-Code-Contributions)
- [Code of Conduct](#Code-of-Conduct)

## Project overview


## Contributing research

## Contributing code

## Project Management

We use the Github projects board to organise our work on the organization
page. For a high-level overview of our modeling strategy please see the
[Modeling Roadmap](https://github.com/orgs/opt-out-tools/projects/41). For
more specific projects, please check the
[organization's projects list](https://github.com/orgs/opt-out-tools/projects).

We use Github issues to create, discuss or carry out work. Each issue can take
one of three forms, a either a bug, a feature request or feature
implementation (task).

- Bug: a problem with the code that needs fixing
- Feature request: an idea for new features
- Feature implementation: concrete steps to be completed to add
  the feature/fix the bug

Bug and feature requests become feature implementations when someone has a
brainwave of how to complete the task.
Thus a feature implementation issue
will contain clear instructions of how to complete task.

Each issue should be labeled with a minimum of two labels, one to indicate
priority and the second to indicate size of task.
It should also belong to a milestone.
We have four milestones over the next months, which look like this:

Milestone name and description:

- 0.1: the minimum viable product (MVP), the minimum
   functionality our tool/s can have to be ready
- 0.2: what is then expected by the end user for the tool/s to have
- 0.3: what features would be good to have in the tool/s
- 0.4: the future of our tool/s

Concrete details of what each milestone contains can be found
in the tool's roadmap.
For example, to see what we want to achieve in terms of Activism
by the 0.1 milestone, see the
[Activism Roadmap](https://github.com/orgs/opt-out-tools/projects/37)

To find out what tools we have, please see
[Our Tools and Our Vision](https://github.com/opt-out-tools/start-here#Our-Tools-and-Our-Vision).
An overview of tasks for each milestone can be found
[here](https://github.com/opt-out-tools/start-her#Tools-Roadmap).

Each issue should belong to a step in the roadmap which will then be sorted
into a project.

Issues may have two kinds of squared bracket labels in the title:

- [WIP]: indicate you are working on something to avoid duplicated work,
request broad review of functionality or API, or seek collaborators (use the
help wanted label).
- [MRG]: the contribution is complete and should be subjected to a detailed
review

## Feature Request/Bug Report

We use GitHub issues to track all bugs and feature requests;
feel free to open an issue if you have found a bug
or wish to request a feature.

In case you experience issues using any repo, do not hesitate
to submit a ticket to the Bug Tracker of the relevant repo.
You are also welcome to post feature requests or pull requests.

It is recommended to check that your issue complies with
the following rules before submitting:

- Verify that your issue is not being currently addressed by
  other issues or pull requests.

- If you are submitting a bug report, we strongly encourage you
  to follow the guidelines in the _How to write a good Bug Report_ section.

### How to write a good Bug Report

When you submit an issue to Github, please do your best
to follow these guidelines!
This will make it a lot easier to provide you with good feedback:

1. The ideal bug report contains a short reproducible code snippet,
   this way anyone can try to reproduce the bug easily
   (see this for more details).
   If your snippet is longer than around 50 lines,
   please link to a gist or a github repo.

1. If not feasible to include a reproducible snippet, please
   be specific about what models, data and functions that are involved.

1. If an exception is raised, please provide the full traceback.

1. Please include your operating system type and version number,
   as well as your laguage (python, javacript) version and other
   important packages such as scikit-learn, numpy, and scipy.

### How to write a good Feature Request

When submitting a feature request, please try and:

- Be clear as possible

- Include relevant documentation wireframes etc.

##  Contributing Code

Feature requests and bug fixes become a feature implementation
issue when anyone has a eureka moment.
The aim of the feature implementation issue is to identify
the steps to complete the feature/fix.

When you've found a feature to implement and are ready to contribute
to a repo, then begin by forking it on GitHub,
then submit a “pull request” (PR).

The first few steps are generic to all Opt Out Tools repos
and involves setting up your git repository:

1. Create an account on GitHub if you do not already have one.

1. Fork the project repo: click on the ‘Fork’ button
   near the top of the page.
   This creates a copy of the code under your account
   on the GitHub user account.
   For more details on how to fork a repository see
   <https://help.github.com/en/github/getting-started-with-github/fork-a-repo>

1. Clone your fork of the repo from your GitHub account to your local disk

Once these steps are complete please see the repository README.md
for specific installation details.

### Workflow for code contributions
1. You found an interesting issue you want to work on
    - If someone else is already working on it, contact that person on slack or github and organize yourself
    - If you want to work on an open issue, post a comment telling that you will work on that issue; we will assign you
    - Make sure to check the comments before starting to work on an open issue even when no one is assigned to it (there might have been a delay)
    - **Ask for clarification from whom created the issue if needed**
1. Create a new branch to take care of the issue
    - Use the following naming scheme for the branch:
        - For new features: `feature/<issue-number>-<name>`
        - For bug fixes: `fix/<name>`
        - Where `<name>` is freely chosen descriptive name
1. Submit a pull request for the issue
    - Give your pull request a helpful title that summarises what your contribution does
    - Remember to mention which issue the PR will close.
    - Make sure your code passes the tests.
    - Make sure your code is properly commented and documented, and make sure the documentation renders properly
    - Tests are necessary for enhancements to be accepted.
    - Make sure that your PR does not add any linter violations.
1. Developer assigns / someone takes the PR to review
    - Ask someone to review your PR
1. Reviewer accepts PR
    - Reviewer writes comments that you are supposed to take care of.
    - After taking care of things, ping reviewer.
    - Wait that reviewer accepts your PR
1. Merge PR to development branch
    - Merge your PR to the current release branch(see [Branch Naming Convention](#Branch-Naming-Convention)) not to `master`

### Pull Request Checklist

#### Research

The PR checklist:

1) Correct naming convention of branch/notebooks/scripts
2) Sufficiently novel to be merged, otherwise will stay on branch
3) Notebook is in correct folder
4) Clear illustration of results: comparison to baselines/benchmarks and acceptance criteria


If you have written a function that you think _"wow that is so great/useful
I think others should have access to it"_ then this brilliant piece of code
belongs in the src/ folder! Please see the toolkit heading for contributing
this code.

#### Production

Eventually there will be a validation suite to check the input, interface
and benchmarking of the production model.
There will also be the facility to use Sphinx documentation
to explain the model.

The PR checklist:

1) Correct naming convention
2) Correct API (to be designed/built)
3) dvc commands to run
4) Reference to research in study-online-misogyny that support the proposed algorithm or to  sufficiently cited research papers


#### Tool-kit

Coming soon

#### General

Before a PR can be merged, it needs to be approved by one core developer.
Please prefix the title of your pull request with [MRG] if the
contribution is complete and should be subjected to a detailed review.
An incomplete contribution – where you expect to do more
work before receiving a full review – should be prefixed with [WIP]
(to indicate a work in progress) and changed to [MRG] when it matures.
For a more detailed explanation of what these mean to the
organization please see [Project Management](#Project-Management).

Follow the Coding guidelines:

- When applicable, use the validation tools and scripts.

- Often pull requests resolve one or more other issues (or pull requests).
  If merging your pull request means that some other issues/PRs
  should be closed, you should use keywords to create link
  to them (e.g., Fixes #1234; multiple issues/PRs are allowed
  as long as each one is preceded by a keyword).
  Upon merging, those issues/PRs will automatically be closed by GitHub.
  If your pull request is simply related to some other issues/PRs,
  create a link to them without using the keywords (e.g., See also #1234).

- New features often need to be illustrated with narrative documentation
  in the user guide, with small code snippets.
  If relevant, please also add references in the literature,
  with PDF links when possible.

### CI/CD

We have Circle CI in two of our code repos.

### Branch Naming Convention

We use a branch for each major release, and tags on
that branch for each minor release.

For example, beta users will use a beta or a release candidate,
which will have a 0.2beta1 release name and tag on the 0.2.X branch.

## Non Code Contributions

Non code contributions are vital to this project. A prime example of this is
 sharing papers and notes. We do this via the wiki attached to this project.

## Code of Conduct

Please note that this project is released with a
[Contributor Code of Conduct](https://github.com/opt-out-tools/opt-out/blob/master/CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
