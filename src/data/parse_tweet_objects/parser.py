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
> parser.jsonl_to_csv(jsonl_path='/Users/you/your_input_data.jsonl',
                      csv_path='/Users/you/your_output_data.csv',
                      attributes=('text',),
                      label='',
                      )

2. Suppose we wish to do some analysis including the location of the
Twitter user. We can use the required_attributes attribute of the parser
to only include Tweets with a non-null user.location attribute.

Furthermore, we can set the hash_attributes attribute of the parser such
that two Tweets will be considered equivalent only if they have the same
text and user.id. Hence tweets with identical text but from different
users will appear separately in the output, whereas duplicate Tweets
from the same user will be removed (even if they have distinct Tweet
ids).

Note that in this example, since user.id is not a required_attribute, it
could be null even though it's both a hash_attribute and a column in the
output (this isn't necessarily desirable from an analysis point of view,
but simply serves as an illustration).

> parser = ParseTweetsFromJSONL()
> parser.required_attributes = ('text', 'user.location')
> parser.hash_attributes = ('text', 'user.id')
> parser.jsonl_to_csv(jsonl_path='/Users/you/your_input_data.jsonl',
                      csv_path='/Users/you/your_output_data.csv',
                      attributes=('text', 'user.id', 'user.location'),
                      label=''
                      )
"""
from json import JSONDecodeError
from typing import Any, Iterable
import logging

import pandas as pd

from src.data.parse_tweet_objects.tweet import Tweet
from src.data.parse_tweet_objects.utils import InvalidTweetError, get_warn_msg


class ParseTweets:
    """
    Class for parsing collections of Tweet JSON objects.

    This class is intended to be a superclass for any class which parses
    Tweet JSON objects stored in a specific format, e.g. JSONL.

    Attributes
    ----------
    required_attributes
        Only Tweets with non-null values for all required_attributes
        will be parsed. Currently defaults to ('id', 'text', 'user') for
        data integrity reasons - if one of these is missing there's
        probably something wrong with the Tweet object - but this could
        be changed to reflect actual usage of the class.
    hash_attributes
        Tweet attributes used to define the hashed value of a Tweet
        object. What this means in practice is that two Tweets are
        considered equivalent if and only if all of their
        respective hash_attributes are the same. Currently defaults to
        ('text',) to reflect current usage for Opt Out Tools.

    Methods
    -------
    tweets_to_dataframe
        Parses Tweet JSON objects to a pandas dataframe.

    tweets_to_csv
        Parses Tweet JSON objects to a CSV.
    """

    def __init__(self,
                 required_attributes: Iterable[str] = ('id', 'text', 'user'),
                 hash_attributes: Iterable[str] = ('text',)
                 ) -> None:
        """
        Init Tweet parser.

        Parameters
        ----------
        required_attributes
            Only Tweets with non-null values for all required_attributes
            will be parsed.
        hash_attributes
            Tweet attributes used to define the hashed value of a Tweet
            object. Tweets with matching hash_attributes are considered
            equivalent.
        """
        self.required_attributes = required_attributes
        self.hash_attributes = hash_attributes

    def tweets_to_dataframe(self,
                            tweets_input: Iterable[str],
                            attributes: Iterable[str],
                            remove_dupes: bool = True,
                            **new_cols: Any
                            ) -> pd.DataFrame:
        """
        Method for parsing multiple Tweet JSON objects to a dataframe.

        Will log a warning in the event of bad input data, e.g. invalid
        JSON objects or Tweets with missing attributes.

        Parameters
        ----------
        tweets_input
            Any iterable of Tweet JSON objects.
        attributes
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attributes.
        new_cols
            Additional columns and their default values.

        Returns
        -------
        pandas dataframe
            dataframe in which each row corresponds to a Tweet.
        """
        # For efficiency, we will grow our output as a dict of lists and
        # convert to a dataframe at the end. Each key of res will be a
        # column name, with the corresponding lists being the column
        # values.
        res = {attr: [] for attr in attributes}

        if remove_dupes:
            processed_tweets = set()

        for idx, tweet_json in enumerate(tweets_input):
            logging.debug(f'Processing Tweet {idx}: {tweet_json.strip()}')

            try:
                tweet = Tweet(tweet_json,
                              required_attributes=self.required_attributes,
                              hash_attributes=self.hash_attributes
                              )

            except (JSONDecodeError, InvalidTweetError) as exc:
                warn_msg = get_warn_msg(idx, exc)
                logging.warning(warn_msg)

            else:
                # If we get here then we have successfully decoded the
                # Tweet JSON object and validated the Tweet object.
                if remove_dupes and tweet in processed_tweets:
                    logging.warning(f'Skipping dupe: Tweet {idx}: {tweet}')
                else:
                    # add it to the result dict
                    for attr in attributes:
                        tweet_attr = tweet.get(attr, default='')
                        res[attr].append(tweet_attr)

                    if remove_dupes:
                        processed_tweets.add(tweet)

        # once we've processed all Tweets, convert res dict to dataframe
        res_df = pd.DataFrame.from_dict(res)

        # now add new cols with their default values
        for nc in new_cols:
            res_df[nc] = new_cols[nc]

        return res_df

    def tweets_to_csv(self,
                      tweets_input: Iterable[str],
                      csv_path: str,
                      attributes: Iterable[str],
                      remove_dupes: bool = True,
                      **new_cols: Any
                      ) -> None:
        """
        Method for parsing multiple Tweet JSON objects to a CSV.

        Will log a warning in the event of bad input data, e.g. invalid
        JSON objects or Tweets with missing attributes.

        Parameters
        ----------
        tweets_input
            Any iterable of Tweet JSON objects.
        csv_path
            Path to output CSV file.
        attributes
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attributes.
        new_cols
            Additional columns and their default values.

        Returns
        -------
        None
        """
        tweets_df = self.tweets_to_dataframe(tweets_input, attributes,
                                             remove_dupes, **new_cols)

        logging.info(f'Writing CSV with {len(tweets_df)} Tweets to {csv_path}')
        tweets_df.to_csv(csv_path, index=False)


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

    def __init__(self,
                 required_attributes: Iterable[str] = ('id', 'text', 'user'),
                 hash_attributes: Iterable[str] = ('text',)
                 ) -> None:
        ParseTweets.__init__(self, required_attributes, hash_attributes)

    def jsonl_to_dataframe(self,
                           jsonl_path: str,
                           attributes: Iterable[str],
                           remove_dupes: bool = True,
                           **new_cols: Any
                           ) -> pd.DataFrame:
        """
        Method for parsing JSONL file containing multiple Tweet JSON
        objects to a dataframe.

        Will log a warning in the event of bad input data, e.g. invalid
        JSON objects or Tweets with missing attributes.

        Extends superclass method tweets_to_dataframe.

        Parameters
        ----------
        jsonl_path
            Path to input JSONL file.
        attributes
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attributes.
        new_cols
            Additional columns and their default values.

        Returns
        -------
        pandas dataframe
            dataframe in which each row corresponds to a valid Tweet.
        """
        with open(jsonl_path, mode='r') as tweets:
            return ParseTweets.tweets_to_dataframe(self, tweets, attributes,
                                                   remove_dupes, **new_cols)

    def jsonl_to_csv(self,
                     jsonl_path: str,
                     csv_path: str,
                     attributes: Iterable[str],
                     remove_dupes: bool = True,
                     **new_cols: Any
                     ) -> None:
        """
        Method for parsing JSONL file containing multiple Tweet JSON
        objects to a CSV.

        Will log a warning in the event of bad input data, e.g. invalid
        JSON objects or Tweets with missing attributes.

        Extends superclass method tweets_to_csv.

        Parameters
        ----------
        jsonl_path
            Path to input JSONL file.
        csv_path
            Path to output CSV file.
        attributes
            Tweet attributes to be included as columns in the output.
            Nested attributes take the form parent.child, e.g.
            'user.id'. If an attribute is not present in a given Tweet
            it will be null in the output.
        remove_dupes
            Defaults to True, in which case duplicate Tweets are
            included only once in the output. The notion of duplicate
            Tweets is defined by the instance attribute hash_attributes.
        new_cols
            Additional columns and their default values.

        Returns
        -------
        None
        """
        with open(jsonl_path, mode='r') as tweets:
            ParseTweets.tweets_to_csv(self, tweets, csv_path, attributes,
                                      remove_dupes, **new_cols)