import sys
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import BaseEstimator, TransformerMixin


class SpacyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self):
        self.spacy_ = spacy.load()
        return self

    def transform(self, X, y=None):
        return spacy.magic(X)

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier



def main():
    """Take text from input dataframe and vectorize it to build a feature matrix"""
    try:
        input_file, output_file = sys.argv[1], sys.argv[2]
    except (IndexError, ValueError) as error:
        print(error)
        print("Error: please specify input and output files.")
    print(f"Input: {input_file}")
    print(f"Output: {output_file}")
    with open(input_file, "rb") as handler:
        feature_matrix = joblib.load(handler)
    labels = feature_matrix[:, -1]
    feature_matrix = feature_matrix[:, :-1]
    print(f"The feature matrix has dimensions {feature_matrix.shape}.")
    classifier = RandomForestClassifier(
        n_estimators=400, random_state=42, n_jobs=-1, verbose=2
    )
    x_train = feature_matrix
    print("Training model...")
    classifier.fit(x_train, labels)
    with open(output_file, "wb") as handler:
        joblib.dump(classifier, handler, compress="zlib")


if __name__ == "__main__":
    main()
