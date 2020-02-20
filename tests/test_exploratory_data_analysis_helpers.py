from src.text.utils import (
    density_of_curse_words_in_sentence,
    density_of_curse_words_in_corpus,
    create_ngrams,
    count_top_10_most_common_ngrams,
)


def test_all_top_20_curse_words_in_sentence():
    tweet = (
        "fuck shit ass bitch nigga hell whore dick piss pussy slut puta tit damn "
        "fag cunt cum cock blowjob"
    )
    assert all(density_of_curse_words_in_sentence(tweet))


def test_calculates_density_of_curse_words_with_punctuation():
    tweet = "fuck!! fuck, fuck. "
    assert density_of_curse_words_in_sentence(tweet)["fuck"] == 0


def test_calculates_density_of_curse_words_with_plurals():
    tweet = "fucks fucks fucks fuck"
    assert density_of_curse_words_in_sentence(tweet)["fuck"] == 1.0


def test_calculates_density_of_curse_words_in_corpus(labeled_tweets):
    assert sum(density_of_curse_words_in_corpus(labeled_tweets).values()) == 0.0


def test_create_ngrams(labeled_tweets):
    unigrams = create_ngrams(labeled_tweets.loc[0, "text"], 1)
    bigrams = create_ngrams(labeled_tweets.loc[0, "text"], 2)
    trigrams = create_ngrams(labeled_tweets.loc[0, "text"], 3)

    assert len(unigrams) == 11
    assert len(bigrams) == 10
    assert len(trigrams) == 9


def test_can_count_most_common_ngrams():
    bigrams = ["big cat", "cat sat", "sat mat", "big cat"]

    assert count_top_10_most_common_ngrams(bigrams) == [
        ("big cat", 2),
        ("cat sat", 1),
        ("sat mat", 1),
    ]
