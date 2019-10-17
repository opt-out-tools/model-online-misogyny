from typing import Callable, List

import pandas as pd

from src.data.preprocess_text_helpers import (
    contractions_unpacker,
    punctuation_cleaner,
    remove_stopwords,
    lowercase,
    tokenizer,
    normalizer,
)


class TextPreProcessingPipeline:
    def __init__(self):
        self._processors: List[Callable[[str], str]] = []

    def register_processor(self, method: Callable[[str], str]):
        self._processors.append(method)

    def process_text(self, text):
        for processor in self._processors:
            text = processor(text)

        return text


def clean(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Returns cleaned text.

          Args
              df (pandas df) : the dataframe with the tweets under a column
              labeled text.

          Returns
              df (pandas df) : the cleaned tweets under the column cleaned.

    """
    pipeline = TextPreProcessingPipeline()
    pipeline.register_processor(contractions_unpacker)
    pipeline.register_processor(tokenizer)
    pipeline.register_processor(punctuation_cleaner)
    pipeline.register_processor(remove_stopwords)
    pipeline.register_processor(lowercase)

    dataframe["cleaned"] = dataframe["text"].apply(pipeline.process_text)
    return dataframe


def normalize(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Returns normalized text.

    Args
        df (pandas df) : the dataframe with the tweets under a column
        labeled text.

    Returns
        df (pandas df) : the normalized tweets under the column normalized.

    """
    pipeline = TextPreProcessingPipeline()
    pipeline.register_processor(contractions_unpacker)
    pipeline.register_processor(tokenizer)
    pipeline.register_processor(punctuation_cleaner)
    pipeline.register_processor(remove_stopwords)
    pipeline.register_processor(lowercase)

    dataframe["normalized"] = normalizer(dataframe["text"].apply(pipeline.process_text))
    return dataframe


def tokenize(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Returns tokenized text in string format.

       Args
           df (pandas df) : the dataframe with the tweets under a column
           labeled text.

       Returns
           df (pandas df) : the tokenized tweets under the column tokenized.

    """
    pipeline = TextPreProcessingPipeline()
    pipeline.register_processor(contractions_unpacker)
    pipeline.register_processor(tokenizer)
    pipeline.register_processor(lowercase)

    dataframe["tokenized"] = dataframe["text"].apply(pipeline.process_text)
    return dataframe
