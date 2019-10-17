from src.data.preprocess_text_helpers import contractions_unpacker
from src.data.preprocess_text_helpers import lowercase
from src.data.preprocess_text_helpers import normalizer
from src.data.preprocess_text_helpers import punctuation_cleaner
from src.data.preprocess_text_helpers import tokenizer


def test_can_unpack_contractions_sentence():
    assert contractions_unpacker("Lol I'm not surprised") == "Lol I am not surprised"
    assert (
        contractions_unpacker("I think it's going to snow.")
        == "I think it is going to snow."
    )


def test_contraction_unpack_case_agnostic():
    assert contractions_unpacker("Ain't") == "am not"
    assert contractions_unpacker("I'm") == "I am"


def test_social_tokenizer():
    tweet1 = "@badwhore Sunday,paul :)tweet? :) whore...?"
    tweet2 = "LIKE 14:40@Reni__Rinse who's f****N"
    tweet3 = ":-3;‑]O_o 3:‑) >.<"

    assert tokenizer(tweet1) == "@badwhore Sunday , paul :) tweet ? :) whore . . . ?"
    assert tokenizer(tweet2) == "LIKE 14:40 @Reni__Rinse who ' s f****N"
    assert tokenizer(tweet3) == ":-3 ;‑] O_o 3:‑) >.<"


def test_punctuation_cleaner_removes_colon():
    tweet1 = "@badwhore Sunday,paul :)tweet? :) whore...?"
    tweet2 = "LIKE 14:40@Reni__Rinse who's f****N"
    tweet3 = ":-3;‑]O_o 3:‑) >.<"

    assert (
        punctuation_cleaner(tokenizer(tweet1))
        == "@badwhore Sunday paul) tweet ?) whore ?"
    )
    assert (
        punctuation_cleaner(tokenizer(tweet2)) == "LIKE 14:40 @Reni__Rinse who s f****N"
    )
    assert punctuation_cleaner(tokenizer(tweet3)) == ":-3 ;‑] O_o 3:‑) >.<"


def test_lowercase():
    assert lowercase("LIKEWISE 14:40 @Reni__Rinse") == "likewise 14:40 @reni__rinse"


def test_normalize():
    assert normalizer(":LIKEWISE 14:40 @Reni__Rinse") == ":LIKEWISE <time> <user>"
