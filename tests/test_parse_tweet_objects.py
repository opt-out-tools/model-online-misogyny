"""
Tests for the NestedDict and Tweet classes of the module
parse_tweet_objects.py
"""

from src.data.parse_tweet_objects import (NestedDict,
                                          Tweet,
                                          InvalidTweetError
                                          )


def test_nested_dict_contains_method():
    nested_dict = NestedDict({'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}})

    assert 'a' in nested_dict
    assert 'b' in nested_dict
    assert 'd' in nested_dict

    assert 'c' not in nested_dict
    assert 'e' not in nested_dict
    assert 'f' not in nested_dict

    assert 'b.c' in nested_dict
    assert 'd.e' in nested_dict
    assert 'd.e.f' in nested_dict

    assert ['d', 'e', 'f'] in nested_dict

    assert 1 not in nested_dict


def test_nested_dict_get_method():
    nested_dict = NestedDict({'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}})

    assert nested_dict.get('a') == 1
    assert nested_dict.get('b') == {'c': 2}
    assert nested_dict.get('d') == {'e': {'f': 3}}

    assert nested_dict.get('c') is None
    assert nested_dict.get('e') is None
    assert nested_dict.get('f') is None

    assert nested_dict.get('b.c') == 2
    assert nested_dict.get('d.e') == {'f': 3}
    assert nested_dict.get('d.e.f') == 3

    assert nested_dict.get(['d', 'e', 'f']) == 3

    assert nested_dict.get(1) is None
    assert nested_dict.get(1, default='test_default') == 'test_default'


def test_nested_dict_getitem_method():
    nested_dict = NestedDict({'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}})
    assert nested_dict['a'] == 1
    assert nested_dict['b'] == {'c': 2}
    assert nested_dict['d'] == {'e': {'f': 3}}

    assert nested_dict['b.c'] == 2
    assert nested_dict['d.e'] == {'f': 3}
    assert nested_dict['d.e.f'] == 3

    assert nested_dict[['d', 'e', 'f']] == 3

    try:
        nested_dict['c']
        assert False
    except Exception as exc:
        assert isinstance(exc, KeyError)

    try:
        nested_dict['a.b']
        assert False
    except Exception as exc:
        assert isinstance(exc, KeyError)


def test_nested_dict_str_method():
    nested_dict = NestedDict({'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}})

    assert str(nested_dict) == "{'a': 1, 'b': {'c': 2}, 'd': {'e': {'f': 3}}}"


def test_tweet_init_method():
    twt_json_1 = '{"id": 1, "text": "Tweet 1", "user": {"id": 11, "name": "Alice"}}'
    twt_json_2 = '{"id": 2, "text": "Tweet 2", "user": {"id": 22, "name": "Bob"}}'
    twt_json_3 = '{"id": 3, "text": "Tweet 3"}'

    twt_dict_1 = {'id': 1, 'text': 'Tweet 1', 'user': {'id': 11, 'name': 'Alice'}}
    twt_dict_2 = {'id': 2, 'text': 'Tweet 2', 'user': {'id': 22, 'name': 'Bob'}}
    twt_dict_3 = {'id': 3, 'text': 'Tweet 3'}

    twt_1 = Tweet(twt_json_1)
    assert twt_1.data == twt_dict_1

    twt_2 = Tweet(twt_json_2)
    assert twt_2.data == twt_dict_2

    twt_3 = Tweet(twt_json_3, validate=False)
    assert twt_3.data == twt_dict_3


def test_tweet_validate_method():
    twt_json_1 = '{"id": 1, "text": "Tweet 1", "user": {"id": 11, "name": "Alice"}}'
    twt_json_2 = '{"id": 2, "text": "Tweet 2", "user": {"id": 22, "name": "Bob"}}'
    twt_json_3 = '{"id": 3, "text": "Tweet 3"}'

    try:
        Tweet(twt_json_1,
              validate=True,
              reqd_attrs=('id', 'text', 'user', 'location')
              )
    except Exception as exc:
        assert isinstance(exc, InvalidTweetError)
        assert 'location' in exc.missing_attrs

    try:
        Tweet(twt_json_2,
              validate=True,
              reqd_attrs=('id', 'text', 'user', 'user.id')
              )
    except:
        assert False

    try:
        Tweet(twt_json_3,
              validate=True,
              reqd_attrs=('id', 'text', 'user')
              )
    except Exception as exc:
        assert isinstance(exc, InvalidTweetError)
        assert 'user' in exc.missing_attrs


def test_tweet_hash_method():
    twt_json_1 = '{"id": 1, "text": "Tweet 1", "user": {"id": 11, "name": "Alice"}}'
    twt_json_2 = '{"id": 2, "text": "Tweet 2", "user": {"id": 22, "name": "Bob"}}'
    twt_json_3 = '{"id": 3, "text": "Tweet 3"}'

    twt_1 = Tweet(twt_json_1,
                  hash_attrs=('id',)
                  )
    assert hash(twt_1) == hash((1,))

    twt_2 = Tweet(twt_json_2,
                  hash_attrs=('text', 'user.id')
                  )
    assert hash(twt_2) == hash(('Tweet 2', 22))

    twt_3 = Tweet(twt_json_3,
                  reqd_attrs=('id', 'text'),
                  hash_attrs=('text', 'user.id')
                  )
    assert hash(twt_3) == hash(('Tweet 3', None))


def test_tweet_eq_method():
    twt_json_1 = '{"id": 1, "text": "Same text", "user": {"id": 11, "name": ' \
                 '"Alice"}}'
    twt_json_2 = '{"id": 2, "text": "Same text", "user": {"id": 22, "name": ' \
                 '"Bob"}}'

    twt_1 = Tweet(twt_json_1, hash_attrs=('id',))
    twt_2 = Tweet(twt_json_2, hash_attrs=('id',))
    assert twt_1 != twt_2

    twt_1 = Tweet(twt_json_1, hash_attrs=('text',))
    twt_2 = Tweet(twt_json_2, hash_attrs=('text',))
    assert twt_1 == twt_2

    twt_1 = Tweet(twt_json_1, hash_attrs=('text', 'user.id'))
    twt_2 = Tweet(twt_json_2, hash_attrs=('text', 'user.id'))
    assert twt_1 != twt_2


if __name__ == '__main__':
    test_nested_dict_get_method()
    test_nested_dict_contains_method()
    test_nested_dict_getitem_method()
    test_nested_dict_str_method()

    test_tweet_validate_method()
    test_tweet_hash_method()
    test_tweet_eq_method()
