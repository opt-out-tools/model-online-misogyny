import sys
from time import time
from pathlib import Path
import json
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, roc_curve, auc
import spacy


np.random.seed(42)


def plot_roc_auc_f1(y_test, y_proba, title=None):
    """Plot ROC curve and random comparison, along with f1 and AUC metrics"""
    std_f1 = f1_score(y_test, y_proba[:, 1] > 0.5)
    fpr, tpr, _ = roc_curve(y_test, y_proba[:, 1])
    auc_score = auc(fpr, tpr)
    fig, axis = plt.subplots(figsize=(6, 6))
    if title is not None:
        axis.set_title(title)
    axis.plot([0, 1], [0, 1], "--", label="Random")
    axis.plot(fpr, tpr, label="Given model")
    axis.set_xlabel("False positive rate")
    axis.set_ylabel("True positive rate")
    axis.annotate(f"AUC: {auc_score:.4}", (0.8, 0.15))
    axis.annotate(f"F1: {std_f1:.4}", (0.8, 0.1))
    axis.legend()
    return std_f1, auc_score, fig, axis


def load_artifacts(test_set_file, trained_model_file):
    test_data = pd.read_csv(test_set_file)
    print("Loading language model...")
    nlp = spacy.load("en_core_web_md")
    print("Loading machine-learning model...")
    model = joblib.load(trained_model_file)
    return model, nlp, test_data


def write_results(output_folder, y_test, y_prob):
    """Save to disk results of model evaluation"""
    roc_img_file_png = output_folder / "roc_auc_f1.png"
    metrics_file = output_folder / "eval.json"

    with plt.style.context("ggplot"):
        f1_test, auc_test, _, _ = plot_roc_auc_f1(y_test, y_prob)

    with open(roc_img_file_png, "wb") as handler:
        plt.savefig(handler, dpi=150, format="png")

    metrics = dict(f1=f1_test, AUC=auc_test)
    with open(metrics_file, "w") as file:
        json.dump(metrics, file, ensure_ascii=False, indent=4)


def main():
    """Load test set and trained model and evaluate performance"""
    print("Command-line arguments:")
    for arg in sys.argv[1:]:
        print(arg)
    try:
        test_set_file, trained_model_file, output_folder = (
            Path(sys.argv[1]),
            Path(sys.argv[2]),
            Path(sys.argv[3]),
        )
    except (IndexError, ValueError) as error:
        print(f"Error: {error}. Please specify all input and output files!")
        sys.exit()
    # Load artifacts (this should be a one-time action in the API)
    model, nlp, test_data = load_artifacts(test_set_file, trained_model_file)
    x_test, y_test = test_data["text"], test_data["label"]
    # Prediction
    # ## Start recording prediction time from here ##
    start_time = time()
    # The .pipe() method batch processes all the text (might take a little while)
    print("Creating embeddings...")
    docs = list(nlp.pipe(x_test))
    feature_matrix = np.array(list(map(lambda x: x.vector, docs)))
    y_prob = model.predict_proba(feature_matrix)
    duration = time() - start_time
    print(f"Avg. single prediction time: {duration/len(y_prob)} s")
    write_results(output_folder, y_test, y_prob)


if __name__ == "__main__":
    main()
