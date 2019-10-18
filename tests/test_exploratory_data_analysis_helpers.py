from src.features.exploratory_data_analysis_helpers import (
    density_of_curse_words_in_sentence,
)


def test_all_top_20_curse_words_in_sentence():
    tweet = (
        "fuck shit ass bitch nigga hell whore dick piss pussy slut puta tit damn "
        "fag cunt cum cock blowjob"
    )
    assert all(density_of_curse_words_in_sentence(tweet))


def test_calculate_density_of_curse_words_with_puncuation():
    tweet = "fuck!! fuck, fuck. "
    assert density_of_curse_words_in_sentence(tweet)["fuck"] == 0


def test_calculates_density_of_curse_words_with_plurals():
    tweet = "fucks fucks fucks fuck"
    assert density_of_curse_words_in_sentence(tweet)["fuck"] == 1.0
