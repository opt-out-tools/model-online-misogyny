"""
Module providing tools for parsing collections of Tweet JSON objects
(typically from the Twitter API).

For further information about Tweet JSON objects see:

https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json

Examples
--------
1. The following example parses a JSONL file and produces a CSV with the
columns text and label - the default format for Opt Out Tools Tweet
data.

> from parse_tweet_objects import ParseTweetsFromJSONL

> parser = ParseTweetsFromJSONL()
> parser.jsonl_to_csv(jsonl_loc='/Users/you/your_input_data.jsonl',
                    csv_loc='/Users/you/your_output_data.csv',
                    root_attrs=('text',),
                    label='',
                    )
"""

import json
import warnings

import pandas as pd


class ParseTweets:
    """
    Class for parsing arbitrary collections of Tweet JSON objects.

    This class is intended to be a superclass for any class which parses
    Tweet JSON objects stored in a specific format, e.g. JSONL.

    Methods
    -------
    tweets_to_dataframe
        Parses Tweet JSON objects to a pandas dataframe, in which each
        row corresponds to a Tweet.

    tweets_to_csv
        Parses Tweet JSON objects to a CSV file, in which each row
        corresponds to a Tweet.

    validate_tweet
        Checks that a given JSON object corresponds to a valid Tweet.
    """

    def __init__(self):
        pass

    def tweets_to_dataframe(self, tweets_input, root_attrs=(), user_attrs=(),
                            remove_dupes=True, dupe_attrs=('id',), **new_cols):
        """
        Method for parsing multiple Tweet JSON objects to a dataframe,
        in which each row is a Tweet.

        Parameters
        ----------
        tweets_input : iterable of str
            Any iterable of Tweet JSON objects.
        root_attrs: tuple of str, optional
            'root-level' Tweet attributes to be included as columns in
            the dataframe, e.g. id, created-at, text. Default does not
            include any.
        user_attrs: tuple of str, optional
            Attributes of the Tweet's User JSON object to be included as
            columns in the dataframe. In general, an attribute of the
            form tweet.user.X will appear as a column named user_X.
            Default does not include any.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output.
        dupe_attrs: tuple of str, optional
            Tuple of root-level Tweet attributes used to define
            duplicates. For two Tweets to be considered dupes of one
            another, all dupe_attrs must match. Defaults to Tweet id.
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
                    Tweet.
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.

        TODO
        ----
        The implementation of User attributes is a bit hacky and
        inflexible. Ideally, would come up with a good way to extract
        attributes of arbitrarily nested child objects of the Tweet.
        """

        # For efficiency, we will grow our output as a dict of lists and
        # convert to a dataframe at the end. Each key of res will be a
        # column name, with the corresponding lists being the column
        # values.
        res = {}
        for attr in root_attrs:
            res[attr] = []
        for attr in user_attrs:
            res['user_' + attr] = []

        if remove_dupes:
            processed_tweets = set()

        for tweet_json in tweets_input:
            try:
                tweet = json.loads(tweet_json)
                self.validate_tweet(tweet)

            except json.JSONDecodeError:
                warn_str = 'Caught Exception JSONDecodeError for the ' \
                           'following object: %s' % (str(tweet_json))
                warnings.warn(warn_str)

            except InvalidTweet as InvalidTweetExc:
                missing_reqd_args = InvalidTweetExc.args
                warn_str = 'Caught Exception InvalidTweet - Tweet is missing ' \
                           'the following required attributes: %s \n This is ' \
                           'the invalid tweet: %s ' % (missing_reqd_args,
                                                       tweet_json)
                warnings.warn(warn_str)

            else:
                # If we get here then we have successfully decoded the
                # Tweet JSON and validated it.

                if remove_dupes:
                    # tuple of tweet attrs is hashable
                    dupe_check_tup = tuple(tweet[attr] for attr in dupe_attrs)
                    if dupe_check_tup in processed_tweets:
                        warnings.warn('Skipping dupe: %s' % tweet)
                        continue
                    else:
                        processed_tweets.add(dupe_check_tup)

                # if not a dupe, add it to the result dict.
                for attr in root_attrs:
                    if attr in tweet:
                        res[attr].append(tweet[attr])
                    else:
                        # leave blank if attribute is missing from Tweet
                        res[attr].append('')

                for attr in user_attrs:
                    if attr in tweet['user']:
                        res['user_' + attr].append(tweet['user'][attr])
                    else:
                        res['user_' + attr].append('')

        res_df = pd.DataFrame.from_dict(res)

        # now add new cols with their default values
        for nc in new_cols:
            res_df[nc] = new_cols[nc]

        return res_df

    def tweets_to_csv(self, tweets_input, csv_loc, root_attrs=(), user_attrs=(),
                      remove_dupes=True, dupe_attrs=('id',), **new_cols):
        """
        Method for parsing multiple Tweet JSON objects to a CSV, in
        which each row is a Tweet.

        Parameters
        ----------
        tweets_input : iterable of str
            Any iterable of Tweet JSON objects.
        csv_loc: str
            Output CSV file.
        root_attrs: tuple of str, optional
            'root-level' Tweet attributes to be included as columns in
            the dataframe, e.g. id, created-at, text. Default does not
            include any.
        user_attrs: tuple of str, optional
            Attributes of the Tweet's User JSON object to be included as
            columns in the dataframe. In general, an attribute of the
            form tweet.user.X will appear as a column named user_X.
            Default does not include any.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output.
        dupe_attrs: tuple of str, optional
            Tuple of root-level Tweet attributes used to define
            duplicates. For two Tweets to be considered dupes of one
            another, all dupe_attrs must match. Defaults to Tweet id.
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
                    Tweet.
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.

        TODO
        ----
        The implementation of User attributes is a bit hacky and
        inflexible. Ideally, would come up with a good way to extract
        attributes of arbitrarily nested child objects of the Tweet.
        """

        tweets_df = self.tweets_to_dataframe(tweets_input, root_attrs,
                                             user_attrs, remove_dupes,
                                             dupe_attrs, **new_cols)

        print('Writing CSV with %d Tweets to %s' % (len(tweets_df), csv_loc))
        tweets_df.to_csv(csv_loc, index=False)

    def validate_tweet(self, tweet, reqd_attrs=('id', 'text', 'user')):
        """
        Method for checking whether a given decoded Tweet JSON object
        corresponds to a valid Tweet.

        We define a valid Tweet as one which contains some minimum set
        of fundamental attributes (and which are not null - but this
        could be changed).

        Parameters
        ----------
        tweet: dict
            Decoded Tweet JSON object.
        reqd_attrs: tuple of str
            The attributes which must be present for a Tweet to be
            considered valid.

        Raises
        ------
        InvalidTweet
            If the Tweet is not valid.

        Returns
        -------
        None
        """

        missing_attrs = []
        for attr in reqd_attrs:
            if attr not in tweet or not tweet[attr]:
                missing_attrs.append(attr)

        if missing_attrs:
            raise InvalidTweet(missing_attrs)


class ParseTweetsFromJSONL(ParseTweets):
    """
    Class for parsing JSONL files containing multiple Tweet JSON
    Objects.

    Subclass of ParseTweets, only adding some file I/O for the JSONL
    source file.

    Methods
    -------
    jsonl_to_dataframe
        Parses JSONL of Tweet JSON objects to a pandas dataframe, in
        which each row corresponds to a Tweet.

    jsonl_to_csv
        Parses JSONL of Tweet JSON objects to a CSV file, in which each
        row corresponds to a Tweet.
    """

    def __init__(self):
        ParseTweets.__init__(self)

    def jsonl_to_dataframe(self, jsonl_loc, root_attrs=(), user_attrs=(),
                           remove_dupes=True, dupe_attrs=('id',), **new_cols):
        """
        Method for parsing JSONL file containing multiple Tweet JSON
        objects to a dataframe, in which each row is a Tweet.

        Extends superclass method tweets_to_dataframe.

        Parameters
        ----------
        jsonl_loc : str
            Input JSONL file.
        root_attrs: tuple of str, optional
            'root-level' Tweet attributes to be included as columns in
            the dataframe, e.g. id, created-at, text. Default does not
            include any.
        user_attrs: tuple of str, optional
            Attributes of the Tweet's User JSON object to be included as
            columns in the dataframe. In general, an attribute of the
            form tweet.user.X will appear as a column named user_X.
            Default does not include any.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output.
        dupe_attrs: tuple of str, optional
            Tuple of root-level Tweet attributes used to define
            duplicates. For two Tweets to be considered dupes of one
            another, all dupe_attrs must match. Defaults to Tweet id.
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
                    Tweet.
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.

        TODO
        ----
        The implementation of User attributes is a bit hacky and
        inflexible. Ideally, would come up with a good way to extract
        attributes of arbitrarily nested child objects of the Tweet.
        """

        with open(jsonl_loc, mode='r') as tweets:
            return ParseTweets.tweets_to_dataframe(self, tweets, root_attrs,
                                                   user_attrs, remove_dupes,
                                                   dupe_attrs, **new_cols)

    def jsonl_to_csv(self, jsonl_loc, csv_loc, root_attrs=(), user_attrs=(),
                     remove_dupes=True, dupe_attrs=('id',), **new_cols):
        """
        Method for parsing JSONL file containing multiple Tweet JSON
        objects to a dataframe, in which each row is a Tweet.

        Extends superclass method tweets_to_csv.

        Parameters
        ----------
        jsonl_loc : str
            Input JSONL file.
        csv_loc: str
            Output CSV file.
        root_attrs: tuple of str, optional
            'root-level' Tweet attributes to be included as columns in
            the dataframe, e.g. id, created-at, text. Default does not
            include any.
        user_attrs: tuple of str, optional
            Attributes of the Tweet's User JSON object to be included as
            columns in the dataframe. In general, an attribute of the
            form tweet.user.X will appear as a column named user_X.
            Default does not include any.
        remove_dupes: bool, optional
            Defaults to True, in which case duplicate Tweets are
            included only once in the output.
        dupe_attrs: tuple of str, optional
            Tuple of root-level Tweet attributes used to define
            duplicates. For two Tweets to be considered dupes of one
            another, all dupe_attrs must match. Defaults to Tweet id.
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
                    Tweet.
            The reason for issuing a warning is that we do not want to
            simply ignore bad input data, while at the same time we do
            not want one bad Tweet out of 50,000 to terminate execution.

        TODO
        ----
        The implementation of User attributes is a bit hacky and
        inflexible. Ideally, would come up with a good way to extract
        attributes of arbitrarily nested child objects of the Tweet.
        """

        with open(jsonl_loc, mode='r') as tweets:
            ParseTweets.tweets_to_csv(self, tweets, csv_loc, root_attrs,
                                      user_attrs, remove_dupes, dupe_attrs,
                                      **new_cols)


class InvalidTweet(Exception):
    pass


if __name__ == '__main__':
    parser = ParseTweetsFromJSONL()

    jsonl_loc = '../../tests/parse_tweet_objects_test_data_with_errors.jsonl'
    csv_loc = '../../tests/parse_tweet_objects_test_result.csv'
    parser.jsonl_to_csv(jsonl_loc,
                        csv_loc,
                        root_attrs=('text',),
                        label='',
                        )
