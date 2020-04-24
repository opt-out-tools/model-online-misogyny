# Using DVC

The **OOT** data team is using [DVC](https://dvc.org/) to track and manage the
machine learning workflow. This file lists useful DVC commands.

## Check if the pipeline is up-to-date

To check if the pipeline is up-to-date, run:

```bash
dvc status
```

## Visualize the pipeline

The pipeline can be visualized in ASCII art with the following command:

```bash
dvc pipeline show --ascii
```
The command visualizes the DVC files responsible for each stage and their mutual
connection. The default (and final) stage is the evaluation stage, which is
specified in `Dvcfile` at the root of the repository. All other DVC files can be
found in the `stages` folder.

## Visualize metrics

Metrics are defined within the DVC pipeline and can be visualized for the
current branch with the following command:

```bash
dvc metrics show
```

To get a quick comparison with all other experiments in the repo, run:

```bash
dvc metrics show -a
```
For more info on comparing experiments see [https://dvc.org/doc/tutorials/deep/reproducibility](https://dvc.org/doc/tutorials/deep/reproducibility.).

## Modify the pipeline

A generic modification of the pipeline should focus on the Python source code in the
`src` folder, most notably `featurize.py` or `train.py`.

To have a closer look at the pipeline setup, investigate the DVC files in the `stages` folder or run:

```bash
dvc pipeline show --ascii -c stages/train.py
```
