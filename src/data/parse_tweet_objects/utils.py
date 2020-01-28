from typing import Any, Dict, Sequence


class InvalidTweetError(Exception):
    """
    Exception raised when a Tweet instance fails validation.

    Attributes
    ----------
    missing_attrs
        The attributes which caused the Tweet object to fail validation.
    msg:
        Formatted error message.
    doc
        The Tweet which caused the error.
    """

    def __init__(self,
                 missing_attrs: Sequence[str],
                 tweet_dict: Dict[str, Any]
                 ) -> None:
        """Inits InvalidTweetError Exception."""
        Exception.__init__(self)
        self.missing_attrs = missing_attrs
        self.msg = f'Missing required attributes: {missing_attrs}'
        self.doc = str(tweet_dict)


def get_warn_msg(idx, exc) -> str:
    """Returns formatted warning message for certain classes of exceptions."""
    return f'{exc.__class__.__name__}: {exc.msg} in Tweet {idx}: ' \
           f'{exc.doc}'.strip()
