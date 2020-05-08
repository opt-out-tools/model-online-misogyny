# pylint: disable=C0103,W0613,W0201, E1120
import numpy as np
import spacy
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted


class SpacyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y):
        self.nlp_ = spacy.load("en_core_web_md")
        return self

    def transform(self, X, y=None):
        check_is_fitted(self)
        try:
            docs = list(self.nlp_.pipe(X))
        except OSError:
            self.nlp_ = spacy.load("en_core_web_md")
            docs = list(self.nlp_.pipe(X))

        feature_matrix = np.array(list(map(lambda x: x.vector, docs)))
        return feature_matrix
