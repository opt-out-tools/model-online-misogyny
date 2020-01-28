import json
from typing import Any, Dict, Iterable, Optional, Sequence, Union

from src.data.parse_tweet_objects.utils import InvalidTweetError


class NestedDict:
    """
    Class providing some methods for working with nested dictionaries.

    Attributes
    ----------
    data
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
        raises KeyError.
    __str__(self)
        Returns str(self.data)
    __repr__(self)
        Returns 'NestedDict(repr({self.data}))'

    TODO
    ----
    Implement methods for setting keys to values, if they're needed one
    day.
    """

    def __init__(self, input_dict: Dict[str, Any]) -> None:
        """
        Init NestedDict with a dict object.

        All keys must be of type str.

        Parameters
        ----------
        input_dict
            Presumably nested, because why else would you be using this
            class?
        """
        self.data = input_dict

    def get(self,
            key: Union[str, Sequence[str]],
            default: Optional[Any] = None
            ) -> Any:
        """
        Parameters
        ----------
        key
            The key of the value we wish to get. Nested keys must be
            delimited by '.', e.g. 'parent.child', or provided as a
            sequence of keys, e.g. ['parent', 'child'].
        default
            Value to return if key is not in self.data. None by default.
        """
        try:
            return NestedDict.get_helper(self.data, key)
        except KeyError:
            return default

    @staticmethod
    def get_helper(nested_dict: Dict[str, Any],
                   compound_key: Union[str, Sequence[str]]
                   ) -> Any:
        """
        Helper method for getting nested dict values.

        This method attempts to call itself recursively, descending one
        level into the nested dict structure with each call, until it
        gets to the end of the compound key object.

        Parameters
        ----------
        nested_dict
            The dict from which we want to get a value.
        compound_key
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
            raise KeyError  # certain invalid keys raise a TypeError

    def __contains__(self, key: Union[str, Sequence[str]]) -> bool:
        """True if the NestedDict has the specified key, else False."""
        return True if self.get(key) else None

    def __getitem__(self, item: Union[str, Sequence[str]]) -> Any:
        """Implements subscripting for getting items from NestedDict."""
        return NestedDict.get_helper(self.data, item)

    def __str__(self) -> str:
        """Return str of the dict object stored in self.data."""
        return str(self.data)

    def __repr__(self) -> str:
        """Return repr of NestedDict instance."""
        return f'NestedDict({repr(self.data)})'


class Tweet(NestedDict):
    """
    Object for storing and handling Tweet data.

    Subclass of NestedDict.

    Attributes
    ----------
    data
        Tweet data
    required_attributes
        Attributes which must be present for a Tweet to be successfully
        validated.
    hash_attributes
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
                 tweet_json: Union[str, dict],
                 validate: bool = True,
                 required_attributes: Iterable[str] = ('id', 'text', 'user'),
                 hash_attributes: Iterable[str] = ('id',)
                 ) -> None:
        """
        Init Tweet object.

        Parameters
        ----------
        tweet_json
            Tweet JSON object.
        validate
            If True, checks that the given Tweet possesses all of the
            attributes required by required_attributes. Defaults to
            True.
        required_attributes
            Attributes which must be present for a Tweet to be valid.
        hash_attributes
            Attributes used to define the hash of a Tweet. Currently
            defaults to id.
        """
        self.required_attributes = required_attributes
        self.hash_attributes = hash_attributes

        tweet_dict = json.loads(tweet_json)
        NestedDict.__init__(self, tweet_dict)

        if validate:
            self.validate()

    def validate(self) -> None:
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
        for attr in self.required_attributes:
            if attr not in self or not self.get(attr):
                missing_attrs.append(attr)

        if missing_attrs:
            raise InvalidTweetError(missing_attrs, self.data)

    def __hash__(self) -> int:
        """Defines the hash of a Tweet object."""
        hash_tup = tuple(self.get(attr) for attr in self.hash_attributes)
        return hash(hash_tup)

    def __eq__(self, other: 'Tweet') -> bool:
        """Defines equivalence of two Tweet objects."""
        return True if self.__hash__() == other.__hash__() else False
