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
        raise

    # # Featurizer here
    df_in = pd.read_csv(input_file)

    classifier = HistGradientBoostingClassifier(verbose=2)
    pipeline = make_pipeline(SpacyTransformer(), classifier)
    pipeline.fit(df_in["text"], df_in["label"])

    with open(output_file, "wb") as handler:
        cloudpickle.dump(pipeline, handler)  # , compress="zlib")


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)
    main()
