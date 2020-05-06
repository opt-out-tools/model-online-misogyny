# pylint: disable=C0103,W0613,W0201,W0611
import logging
import sys
import cloudpickle
import pandas as pd
from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import HistGradientBoostingClassifier

from src.transformers import SpacyTransformer

logger = logging.getLogger(__name__)


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

    classifier = HistGradientBoostingClassifier(
        verbose=2,
        # n_estimators=400, random_state=42, n_jobs=-1, verbose=2
    )
    pipeline = make_pipeline(SpacyTransformer(), classifier)
    pipeline.fit(df_in["text"], df_in["label"])

    # print(f"Input: {input_file}")
    # print(f"Output: {output_file}")
    # with open(input_file, "rb") as handler:
    #     feature_matrix = cloudpickle.load(handler)
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
        cloudpickle.dump(pipeline, handler)  # , compress="zlib")


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    main()
