"""
Module providing tools for parsing collections of Tweet JSON objects
(the format received from the Twitter API).

For further information about Tweet JSON objects see:

https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json

Examples
--------
1. This example parses a JSONL file of Tweet JSON objects and produces a
CSV with the columns text and label - the current default format for Opt
Out Tools Tweet data.

> parser = ParseTweetsFromJSONL()
> parser.jsonl_to_csv(jsonl_loc='/Users/you/your_input_data.jsonl',
                      csv_loc='/Users/you/your_output_data.csv',
                      attrs=('text',),
                      label='',
                      )

2. Suppose we wish to do some analysis including the location of the
Twitter user. We can use the reqd_attrs attribute of the parser to only
include Tweets with a non-null user.location attribute.

Furthermore, we can set the hash_attrs attribute of the parser such that
Tweets with identical text but from different users will appear
separately in the output (but duplicate Tweets from the same user will
be removed, even if they have distinct Tweet ids).

Note that in this example, since user.id is not a reqd_attr, it could be
null even though it's both a hash_attr and a column in the output (this
isn't necessarily desirable from an analysis point of view, but simply
serves as an illustration).

> parser = ParseTweetsFromJSONL()
> parser.reqd_attrs = ('text', 'user.location')
> parser.hash_attrs = ('text', 'user.id')
> parser.jsonl_to_csv(jsonl_loc='/Users/you/your_input_data.jsonl',
                      csv_loc='/Users/you/your_output_data.csv',
                      attrs=('text', 'user.id', 'user.location'),
                      label=''
                      )
"""

import json
import warnings

import pandas as pd


class ParseTweets:
    """
    Class for parsing collections of Tweet JSON objects.

    This class is intended to be a superclass for any class which parses
    Tweet JSON objects stored in a specific format, e.g. JSONL.

    Attributes
    ----------
    reqd_attrs: tuple of str
        Only Tweets with non-null values for all reqd_attrs will be
        parsed. Currently defaults to ('id', 'text', 'user') for
        data integrity reasons - if one of these is missing there's
        probably something wrong with the Tweet object - but this could
        be changed to reflect actual usage of the class.
    hash_attrs: tuple of str
        Tweet attributes used to define the hashed value of a Tweet
        object. What this means in practice is that two Tweets are
        considered equivalent if and only if all of their
        respective hash_attrs are the same. Currently defaults to
        ('text',) to reflect current usage for Opt Out Tools.

    Methods
    -------
    tweets_to_dataframe
        Parses Tweet JSON objects to a pandas dataframe.

    tweets_to_csv
        Parses Tweet JSON objects to a CSV.
    """

    def __init__(self, reqd_attrs=('id', 'text', 'user'), hash_attrs=('text',)):
        """
        Init Tweet parser.

        Parameters
        ----------
        reqd_attrs: tuple of str, optional
            Only Tweets with non-null values for all reqd_attrs will be
            parsed.
        hash_attrs: tuple of str, optional
            Tweet attributes used to define the hashed value of a Tweet
            object. Tweets with matching hash_attrs are considered
            equivalent.
        """
        self.reqd_attrs = reqd_attrs
        self.hash_attrs = hash_attrs

    def tweets_to_dataframe(self, tweets_input, attrs, remove_dupes=True,
                            **new_cols):
        """
        Method for parsing multiple Tweet JSON objects to a dataframe.

        Parameters
        ----------
        tweets_input: iterable of str
            Any iterable of Tweet JSON objects.
        attrs: tuple of str
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attrs.
        new_cols: any data type which can be stored in a pd dataframe
            Additional columns and their default values.

        Returns
        -------
        pandas dataframe
            dataframe in which each row corresponds to a Tweet.

        Warns
        -----
        UserWarning
            Issued if
                1. A given Tweet JSON object cannot be decoded, or
                2. A decoded JSON object does not correspond to a valid
                    Tweet (i.e. it is missing at least one of
                    reqd_attrs).
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.
        """
        # For efficiency, we will grow our output as a dict of lists and
        # convert to a dataframe at the end. Each key of res will be a
        # column name, with the corresponding lists being the column
        # values.
        res = {attr: [] for attr in attrs}

        if remove_dupes:
            processed_tweets = set()

        for tweet_json in tweets_input:
            try:
                tweet = Tweet(tweet_json,
                              reqd_attrs=self.reqd_attrs,
                              hash_attrs=self.hash_attrs
                              )

            except (json.JSONDecodeError, InvalidTweetError) as exc:
                warn_msg = get_warn_msg(exc)
                warnings.warn(warn_msg)

            else:
                # If we get here then we have successfully decoded the
                # Tweet JSON object and validated the Tweet object.
                if remove_dupes and tweet in processed_tweets:
                    warnings.warn('Skipping dupe: %s' % tweet)
                else:
                    # add it to the result dict
                    for attr in attrs:
                        res[attr].append(tweet.get(attr, default=''))

                    # and record that we've seen this Tweet.
                    processed_tweets.add(tweet)

        # once we've processed all Tweets, convert res dict to dataframe
        res_df = pd.DataFrame.from_dict(res)

        # now add new cols with their default values
        for nc in new_cols:
            res_df[nc] = new_cols[nc]

        return res_df

    def tweets_to_csv(self, tweets_input, csv_loc, attrs, remove_dupes=True,
                      **new_cols):
        """
        Method for parsing multiple Tweet JSON objects to a CSV.

        Parameters
        ----------
        tweets_input: iterable of str
            Any iterable of Tweet JSON objects.
        csv_loc: str
            Path to output CSV file.
        attrs: tuple of str
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attrs.
        new_cols: any data type which can be stored in a pd dataframe
            Additional columns and their default values.

        Returns
        -------
        None

        Warns
        -----
        UserWarning
            Issued if
                1. A given Tweet JSON object cannot be decoded, or
                2. A decoded JSON object does not correspond to a valid
                    Tweet (i.e. it is missing at least one of
                    reqd_attrs).
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.
        """
        tweets_df = self.tweets_to_dataframe(tweets_input, attrs, remove_dupes,
                                             **new_cols)

        print('Writing CSV with %d Tweets to %s' % (len(tweets_df), csv_loc))
        tweets_df.to_csv(csv_loc, index=False)


class ParseTweetsFromJSONL(ParseTweets):
    """
    Class for parsing JSONL files containing multiple Tweet JSON
    Objects.

    Subclass of ParseTweets, only adding some file I/O for the JSONL
    source file.

    Methods
    -------
    jsonl_to_dataframe
        Parses JSONL of Tweet JSON objects to a pandas dataframe.

    jsonl_to_csv
        Parses JSONL of Tweet JSON objects to a CSV.
    """

    def __init__(self):
        ParseTweets.__init__(self)

    def jsonl_to_dataframe(self, jsonl_loc, attrs, remove_dupes=True,
                           **new_cols):
        """
        Method for parsing JSONL file containing multiple Tweet JSON
        objects to a dataframe.

        Extends superclass method tweets_to_dataframe.

        Parameters
        ----------
        jsonl_loc : str
            Path to input JSONL file.
        attrs: tuple of str
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attrs.
        new_cols: any data type which can be stored in a pd dataframe
            Additional columns and their default values.

        Returns
        -------
        pandas dataframe
            dataframe in which each row corresponds to a valid Tweet.

        Warns
        -----
        UserWarning
            Issued if
                1. A given Tweet JSON object cannot be decoded, or
                2. A decoded JSON object does not correspond to a valid
                    Tweet (i.e. it is missing at least one of
                    reqd_attrs).
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.
        """
        with open(jsonl_loc, mode='r') as tweets:
            return ParseTweets.tweets_to_dataframe(self, tweets, attrs,
                                                   remove_dupes, **new_cols)

    def jsonl_to_csv(self, jsonl_loc, csv_loc, attrs, remove_dupes=True,
                     **new_cols):
        """
        Method for parsing JSONL file containing multiple Tweet JSON
        objects to a dataframe.

        Extends superclass method tweets_to_csv.

        Parameters
        ----------
        jsonl_loc : str
            Path to input JSONL file.
        csv_loc: str
            Path to output CSV file.
        attrs: tuple of str
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attrs.
        new_cols: any data type which can be stored in a pd dataframe
            Additional columns and their default values.

        Returns
        -------
        None

        Warns
        -----
        UserWarning
            Issued if
                1. A given Tweet JSON object cannot be decoded, or
                2. A decoded JSON object does not correspond to a valid
                    Tweet (i.e. it is missing at least one of
                    reqd_attrs).
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.
        """
        with open(jsonl_loc, mode='r') as tweets:
            ParseTweets.tweets_to_csv(self, tweets, csv_loc, attrs,
                                      remove_dupes, **new_cols)


class NestedDict:
    """
    Class providing some methods for working with nested dictionaries.

    Attributes
    ----------
    data: dict
        The nested dict we wish to work with.

    Methods
    -------
    get(self, key, default=None)
        Generalisation of dict get method to deal with nested dicts.
    __contains__(self, key)
        Returns True if the nested dict contains the specified key, else
        False.
    __getitem__(self, item)
        Returns the value for item if item is in the nested dict, else
        KeyError.
    __str__(self)
        Returns str(self.data)

    TODO
    ----
    Implement methods for setting keys to values, if they're needed one
    day.
    """

    def __init__(self, input_dict):
        """
        Init NestedDict with a dict object.

        Parameters
        ----------
        input_dict: dict
            Presumably nested, because why else would you be using this
            class?
        """
        self.data = input_dict

    def get(self, key, default=None):
        """
        Parameters
        ----------
        key: str or list of str
            The key of the value we wish to get. Nested keys must be
            delimited by '.', e.g. 'parent.child', or provided as a
            list of keys, e.g. ['parent', 'child'].
        default: any type, optional
            Value to return if key is not in self.data. None by default.
        """
        try:
            return NestedDict.get_helper(self.data, key)
        except KeyError:
            return default

    @staticmethod
    def get_helper(nested_dict, compound_key):
        """
        Helper method for getting nested dict values.

        This method attempts to call itself recursively, descending one
        level into the nested dict structure with each call, until it
        gets to the end of the compound key object.

        Parameters
        ----------
        nested_dict: dict
            The dict from which we want to get a value.
        compound_key: str or list of str
            The key of the value we wish to get. Nested keys must be
            delimited by '.', e.g. 'parent.child', or provided as a
            list of keys, e.g. ['parent', 'child']

        Raises
        ------
        KeyError
            If the requested key does not exist in the dict.
        """
        if isinstance(compound_key, str):
            compound_key = compound_key.split('.')

        try:
            if len(compound_key) == 1:
                return nested_dict[compound_key[0]]
            else:
                return NestedDict.get_helper(nested_dict[compound_key[0]],
                                             compound_key[1:])
        except (KeyError, TypeError):
            raise KeyError

    def __contains__(self, key):
        """True if the NestedDict has the specified key, else False."""
        return True if self.get(key) else None

    def __getitem__(self, item):
        """Implements subscripting for getting items from NestedDict."""
        return NestedDict.get_helper(self.data, item)

    def __str__(self):
        """Return str of the dict object stored in self.data."""
        return str(self.data)


class Tweet(NestedDict):
    """
    Object for storing and handling Tweet data.

    Subclass of NestedDict.

    Attributes
    ----------
    data: dict
        Tweet data
    reqd_attrs: tuple of str
        Attributes which must be present for a Tweet to be successfully
        validated.
    hash_attrs: tuple of str
        Tweet attributes used to hash a Tweet object.

    Methods
    -------
    validate
        For checking that a given dict corresponds to a valid Tweet.
    __hash__
        Defines the hashed value of a Tweet object.
    __eq__
        Returns True if hash(self) == hash(other).
    """

    def __init__(self,
                 tweet_json,
                 validate=True,
                 reqd_attrs=('id', 'text', 'user'),
                 hash_attrs=('id',)
                 ):
        """
        Init Tweet object.

        Parameters
        ----------
        tweet_json: str
            Tweet JSON object.
        validate: bool, optional
            If True, checks that the given Tweet possesses all of the
            attributes required by reqd_attrs. Defaults to True.
        reqd_attrs: tuple of str
            Attributes which must be present for a Tweet to be valid.
        hash_attrs: tuple of str
            Attributes used to define the hash of a Tweet. Currently
            defaults to id.
        """
        self.reqd_attrs = reqd_attrs
        self.hash_attrs = hash_attrs

        tweet_dict = json.loads(tweet_json)
        NestedDict.__init__(self, tweet_dict)

        if validate:
            self.validate()

    def validate(self):
        """
        Validate Tweet objects.

        We define a valid Tweet object as one which contains non-null
        values for certain required attributes.

        Raises
        ------
        InvalidTweetError
            If a required attribute is missing or is null.

        Returns
        -------
        None
            If the Tweet is valid
        """
        missing_attrs = []
        for attr in self.reqd_attrs:
            if attr not in self or not self.get(attr):
                missing_attrs.append(attr)

        if missing_attrs:
            raise InvalidTweetError(missing_attrs, self.data)

    def __hash__(self):
        """Defines the hash of a Tweet object."""
        hash_tup = tuple(self.get(attr) for attr in self.hash_attrs)
        return hash(hash_tup)

    def __eq__(self, other):
        """Defines equivalence of two Tweet objects."""
        return True if self.__hash__() == other.__hash__() else False


class InvalidTweetError(Exception):
    """
    Exception raised when a Tweet instance fails validation.

    Attributes
    ----------
    missing_attrs: list of str
        The attributes which caused the Tweet object to fail validation.
    msg: str
        Formatted error message.
    doc: str
        The Tweet which caused the error.
    """

    def __init__(self, missing_attrs, tweet_dict):
        """Inits InvalidTweetError Exception."""
        Exception.__init__(self)
        self.missing_attrs = missing_attrs
        self.msg = 'Missing required attributes: ' + str(missing_attrs)
        self.doc = str(tweet_dict)


def get_warn_msg(exc):
    """
    Returns formatted warning message for certain classes of exceptions.
    """

    return "%s: %s in: %s" % (exc.__class__.__name__, exc.msg, exc.doc)


if __name__ == '__main__':
    jsonl_loc = '../../tests/parse_tweet_objects_test_data.jsonl'
    csv_loc = '../../tests/parse_tweet_objects_test_result.csv'

    parser = ParseTweetsFromJSONL()
    parser.jsonl_to_csv(jsonl_loc,
                        csv_loc,
                        attrs=('text',),
                        label='',
                        )
