"""Unit tests for parser.py module of parse_tweet_objects package."""

import logging

import pandas as pd
import pytest

from src.data.parse_tweet_objects.parser import ParseTweets, ParseTweetsFromJSONL


@pytest.fixture
def target_dataframe():
    return pd.DataFrame({'user.id': [11, 22], 'text': ['Alice Tweet', 'Bob Tweet'], 'label': ['', '']})


@pytest.fixture
def target_csv():
    return 'user.id,text,label\n11,Alice Tweet,\n22,Bob Tweet,\n'


class TestParseTweetsClass:
    @pytest.fixture
    def tweets_list(self, test_tweet_1_json, test_tweet_2_json):
        return [test_tweet_1_json, test_tweet_2_json]

    @pytest.fixture
    def tweets_list_with_dupes(self, test_tweet_1_json, test_tweet_2_json):
        return [test_tweet_1_json, test_tweet_1_json, test_tweet_2_json]

    @pytest.fixture
    def tweets_list_with_invalid_json(self, test_tweet_1_json, test_tweet_2_json):
        return [test_tweet_1_json, test_tweet_2_json] + ['{This is an invalid JSON}']

    def test_tweets_to_dataframe_method(self, tweets_list, target_dataframe):
        parser = ParseTweets()
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list,
                                                      attributes=('user.id', 'text'),
                                                      label=''
                                                      )

        pd.testing.assert_frame_equal(output_dataframe, target_dataframe)

    def test_tweets_to_dataframe_method_remove_dupes_true(self, tweets_list_with_dupes, target_dataframe):
        parser = ParseTweets()
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list_with_dupes,
                                                      attributes=('user.id', 'text'),
                                                      remove_dupes=True,
                                                      label=''
                                                      )

        pd.testing.assert_frame_equal(output_dataframe, target_dataframe)

    def test_tweets_to_dataframe_method_remove_dupes_true_warning_msg(self, tweets_list_with_dupes, caplog):
        parser = ParseTweets()
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list_with_dupes,
                                                      attributes=('user.id', 'text'),
                                                      remove_dupes=True,
                                                      label=''
                                                      )

        assert caplog.record_tuples == [('root', logging.WARNING,
                                         "Skipping dupe: Tweet 1: {'id': 1, 'text': 'Alice Tweet', 'user': {'id': 11, 'name': 'Alice', 'location': 'Berlin'}}")]

    def test_tweets_to_dataframe_method_remove_dupes_false(self, tweets_list_with_dupes):
        parser = ParseTweets()
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list_with_dupes,
                                                      attributes=('user.id', 'text'),
                                                      remove_dupes=False,
                                                      label=''
                                                      )

        target_dataframe = pd.DataFrame({'user.id': [11, 11, 22], 'text': ['Alice Tweet', 'Alice Tweet', 'Bob Tweet'],
                                         'label': ['', '', '']})

        pd.testing.assert_frame_equal(output_dataframe, target_dataframe)

    def test_tweets_to_dataframe_method_jsondecodeerror(self, tweets_list_with_invalid_json, target_dataframe):
        parser = ParseTweets()
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list_with_invalid_json,
                                                      attributes=('user.id', 'text'),
                                                      label=''
                                                      )

        pd.testing.assert_frame_equal(output_dataframe, target_dataframe)

    def test_tweets_to_dataframe_method_jsondecodeerror_warning_msg(self, tweets_list_with_invalid_json, caplog):
        parser = ParseTweets()
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list_with_invalid_json,
                                                      attributes=('user.id', 'text'),
                                                      label=''
                                                      )

        assert caplog.record_tuples == [('root', logging.WARNING, "JSONDecodeError: Expecting property name enclosed "
                                                                  "in double quotes in Tweet 2: {This is an invalid JSON}")]

    def test_tweets_to_dataframe_method_invalidtweet(self, tweets_list):
        parser = ParseTweets(required_attributes=('user.location',))  # this will invalidate test_tweet_2_json
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list,
                                                      attributes=('user.id', 'text'),
                                                      label=''
                                                      )

        target_dataframe = pd.DataFrame({'user.id': [11], 'text': ['Alice Tweet'], 'label': ['']})

        pd.testing.assert_frame_equal(output_dataframe, target_dataframe)

    def test_tweets_to_dataframe_method_invalidtweet_warning_msg(self, tweets_list, caplog):
        parser = ParseTweets(required_attributes=('user.location',))  # this will invalidate test_tweet_2_json
        output_dataframe = parser.tweets_to_dataframe(tweets_input=tweets_list,
                                                      attributes=('user.id', 'text'),
                                                      label=''
                                                      )

        assert caplog.record_tuples == [('root', logging.WARNING, "InvalidTweetError: Missing required attributes: ['user.location'] in Tweet 1: {'id': 2, 'text': 'Bob Tweet', 'user': {'id': 22, 'name': 'Bob'}}")]

    def test_tweets_to_csv_method(self, tweets_list, target_csv, tmpdir):
        tmp_csv_path = tmpdir.join('tmp_output.csv')

        parser = ParseTweets()
        parser.tweets_to_csv(tweets_input=tweets_list, csv_path=tmp_csv_path, attributes=('user.id', 'text'), label='')

        assert tmp_csv_path.read() == target_csv


class TestParseTweetsFromJSONLClass:
    @pytest.fixture
    def tweets_jsonl(self, test_tweet_1_json, test_tweet_2_json):
        return test_tweet_1_json + '\n' + test_tweet_2_json

    def test_jsonl_to_dataframe_method(self, tweets_jsonl, target_dataframe, tmpdir):
        tmp_jsonl_path = tmpdir.join('tmp_source.jsonl')
        tmp_jsonl_path.write(tweets_jsonl)

        parser = ParseTweetsFromJSONL()
        output_dataframe = parser.jsonl_to_dataframe(jsonl_path=tmp_jsonl_path, attributes=('user.id', 'text'), label='')

        pd.testing.assert_frame_equal(output_dataframe, target_dataframe)

    def test_jsonl_to_csv_method(self, tweets_jsonl, target_csv, tmpdir):
        tmp_jsonl_path = tmpdir.join('tmp_source.jsonl')
        tmp_csv_path = tmpdir.join('tmp_output.csv')
        tmp_jsonl_path.write(tweets_jsonl)

        parser = ParseTweetsFromJSONL()
        parser.jsonl_to_csv(jsonl_path=tmp_jsonl_path, csv_path=tmp_csv_path, attributes=('user.id', 'text'), label='')

        assert tmp_csv_path.read() == target_csv
