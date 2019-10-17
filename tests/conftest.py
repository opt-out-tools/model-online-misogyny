import pandas as pd
import pytest

from src.data.preprocess_text_helpers import contractions
from tests.domain_objects_for_testing import create_dataframe_of_labeled_tweets


@pytest.fixture
def contractions_mapping():
    return pd.DataFrame(
        {
            "contraction": list(contractions().keys()),
            "unpacked": list(contractions().values()),
        }
    )


@pytest.fixture
def labeled_tweets():
    return create_dataframe_of_labeled_tweets()
