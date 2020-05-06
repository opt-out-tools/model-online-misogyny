# pylint: disable=C0103,W0613,W0201
import logging
import sys
import joblib
import numpy as np
import pandas as pd
import spacy
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier


logger = logging.getLogger(__name__)


class SpacyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y):
        self.nlp_ = spacy.load("en_core_web_md")
        return self

    def transform(self, X, y=None):
        check_is_fitted(self)
        docs = list(self.nlp_.pipe(X))
        feature_matrix = np.array(list(map(lambda x: x.vector, docs)))
        return feature_matrix


def main():
    # """Take text from input dataframe and vectorize it to build a feature matrix"""
    """Take text as input, create feature matrix, and train model with sklearn pipeline"""
    try:
        input_file, output_file = sys.argv[1], sys.argv[2]
    except (IndexError, ValueError) as error:
        print(error)
        print("Error: please specify input and output files.")

    # # Featurizer here
    df_in = pd.read_csv(input_file)
    # print("Loading language model...")
    # nlp = spacy.load("en_core_web_md")
    # # The .pipe() method batch processes all the text (will take a little while)
    # print("Creating embeddings...")
    # docs = list(nlp.pipe(df_in["text"]))
    # feature_matrix = np.array(list(map(lambda x: x.vector, docs)))

    classifier = RandomForestClassifier(
        n_estimators=400, random_state=42, n_jobs=-1, verbose=2
    )
    pipeline = make_pipeline(SpacyTransformer(), classifier)
    pipeline.fit(df_in["text"], df_in["label"])

    # print(f"Input: {input_file}")
    # print(f"Output: {output_file}")
    # with open(input_file, "rb") as handler:
    #     feature_matrix = joblib.load(handler)
    # labels = feature_matrix[:, -1]
    # feature_matrix = feature_matrix[:, :-1]
    # print(f"The feature matrix has dimensions {feature_matrix.shape}.")
    # classifier = RandomForestClassifier(
    #     n_estimators=400, random_state=42, n_jobs=-1, verbose=2
    # )
    # x_train = feature_matrix
    # print("Training model...")
    # classifier.fit(x_train, labels)
    with open(output_file, "wb") as handler:
        joblib.dump(pipeline, handler, compress="zlib")


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    main()
