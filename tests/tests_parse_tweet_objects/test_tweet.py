"""Tests for tweet.py module of parse_tweet_objects package."""

import pytest

from src.data.parse_tweet_objects.tweet import NestedDict, Tweet
from src.data.parse_tweet_objects.utils import InvalidTweetError


class TestNestedDictClass:
    @pytest.fixture
    def nested_dict_example(self):
        """Canonical example with multiple levels of nesting."""
        return NestedDict({'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}})

    @pytest.mark.parametrize('key', ['a', 'b', 'd', 'b.c', 'd.e.f', ['d', 'e', 'f']])
    def test_nested_dict_contains_method_in(self, nested_dict_example, key):
        assert key in nested_dict_example

    @pytest.mark.parametrize('key', ['c', 'e', 'f', 'g', 'b.d', 'g.h', 1])
    def test_nested_dict_contains_method_not_in(self, nested_dict_example, key):
        assert key not in nested_dict_example

    @pytest.mark.parametrize('key, value', [('a', 1),
                                            ('b', {'c': 2}),
                                            ('d', {'e': {'f': 3}}),
                                            ('c', None),
                                            ('e', None),
                                            ('f', None),
                                            ('b.c', 2),
                                            ('d.e', {'f': 3}),
                                            ('d.e.f', 3),
                                            (['d', 'e', 'f'], 3,),
                                            (1, None)
                                            ]
                             )
    def test_nested_dict_get_method(self, nested_dict_example, key, value):
        assert nested_dict_example.get(key) == value

    @pytest.mark.parametrize('key, default, return_value', [('a', 'default_value', 1),
                                                            ('g', 'default_value', 'default_value')
                                                            ]
                             )
    def test_nested_dict_get_method_with_default(self, nested_dict_example, key, default, return_value):
        assert nested_dict_example.get(key, default=default) == return_value

    @pytest.mark.parametrize('key, value', [('a', 1),
                                            ('b', {'c': 2}),
                                            ('d', {'e': {'f': 3}}),
                                            ('b.c', 2),
                                            ('d.e', {'f': 3}),
                                            ('d.e.f', 3),
                                            (['d', 'e', 'f'], 3)
                                            ]
                             )
    def test_nested_dict_getitem_method(self, nested_dict_example, key, value):
        assert nested_dict_example[key] == value

    @pytest.mark.parametrize('key', ['c', 'g', 'a.b', 1])
    def test_nested_dict_getitem_method_keyerror(self, nested_dict_example, key):
        with pytest.raises(KeyError):
            nested_dict_example[key]

    def test_nested_dict_str_method(self, nested_dict_example):
        assert str(nested_dict_example) == "{'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}}"

    def test_nested_dict_repr_method(self, nested_dict_example):
        assert repr(nested_dict_example) == "NestedDict({'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}})"


class TestTweetClass:
    def test_tweet_init_method_success(self, test_tweet_1_json):
        tweet_object = Tweet(test_tweet_1_json,
                             validate=True,
                             required_attributes=('id', 'text', 'user')
                             )
        assert tweet_object.data == {'id': 1, 'text': 'Alice Tweet', 'user': {'id': 11, 'name': 'Alice', 'location': 'Berlin'}}

    def test_tweet_init_method_failure(self, test_tweet_2_json):
        with pytest.raises(InvalidTweetError):
            Tweet(test_tweet_2_json,
                  validate=True,
                  required_attributes=('user.location',),
                  )

    def test_tweet_hash_method(self, test_tweet_1_json):
        tweet = Tweet(test_tweet_1_json, hash_attributes=('text', 'user.id'))
        assert hash(tweet) == hash(tuple(('Alice Tweet', 11)))

    @pytest.mark.parametrize('hash_attributes', [('text',),
                                                 ('text', 'user.id')
                                                 ]
                             )
    def test_tweet_eq_method(self, test_tweet_2_json, test_tweet_3_json, hash_attributes):
        tweet_2 = Tweet(test_tweet_2_json, hash_attributes=hash_attributes)
        tweet_3 = Tweet(test_tweet_3_json, hash_attributes=hash_attributes)

        assert tweet_2 == tweet_3

    @pytest.mark.parametrize('hash_attributes', [('id',)])
    def test_tweet_eq_method_not_eq(self, test_tweet_2_json, test_tweet_3_json, hash_attributes):
        tweet_2 = Tweet(test_tweet_2_json, hash_attributes=hash_attributes)
        tweet_3 = Tweet(test_tweet_3_json, hash_attributes=hash_attributes)

        assert tweet_2 != tweet_3
