from src.data.preprocess_text_pipelines import normalize, clean, tokenize


def test_normalize(labeled_tweets):
    assert (
        normalize(labeled_tweets).loc[0, "normalized"]
        == "rt <user> feminists take note <hashtag> "
        "<hashtag> <url>"
    )
    assert (
        normalize(labeled_tweets).loc[1, "normalized"]
        == "rt <user> antis stop treating blocks "
        "trophies soon feminists stop treating "
        "blocks arguments đÿ \uf190 ¸ â ˜ • "
        "<hashtag>"
    )
    assert (
        normalize(labeled_tweets).loc[2, "normalized"]
        == "<user> <user> cue nafalt 3 2 1"
    )
    assert (
        normalize(labeled_tweets).loc[3, "normalized"]
        == "rt <user> lol i surprised 2 accounts "
        "blocked <user> <hashtag> <hashtag> & "
        "<user> <hashtag> <url>"
    )


def test_clean(labeled_tweets):
    assert (
        clean(labeled_tweets).loc[0, "cleaned"]
        == "rt @asredasmyhair feminists take note #femfreefriday #womenagainstfeminism "
        "http://t.co/j2hqzvj8cx"
    )
    assert (
        clean(labeled_tweets).loc[1, "cleaned"]
        == "rt @allstatejackie antis stop treating blocks trophies soon feminists stop "
        "treating blocks arguments đÿ \uf190 ¸ â ˜ • #gamergate"
    )
    assert (
        clean(labeled_tweets).loc[2, "cleaned"]
        == "@mgtowknight @factsvsopinion cue nafalt 3 2 1"
    )
    assert (
        clean(labeled_tweets).loc[3, "cleaned"]
        == "rt @baum_erik lol i surprised 2 accounts blocked @femfreq #feminazi "
        "#gamergate & @momsagainstwwe #paranoidparent http://t.câ€¦"
    )


def test_tokenize(labeled_tweets):
    assert (
        tokenize(labeled_tweets).loc[0, "tokenized"]
        == "rt @asredasmyhair : feminists , take note "
        ""
        ". #femfreefriday #womenagainstfeminism "
        "http://t.co/j2hqzvj8cx"
    )
    assert (
        tokenize(labeled_tweets).loc[1, "tokenized"]
        == "rt @allstatejackie : antis will stop "
        "treating blocks as trophies as soon as "
        "feminists stop treating blocks as "
        "arguments . đÿ \uf190 ¸ â ˜ • #gamergate"
    )
    assert (
        tokenize(labeled_tweets).loc[2, "tokenized"]
        == "@mgtowknight @factsvsopinion . . . cue "
        "the nafalt in 3 . . 2 . . . 1 . . ."
    )
    assert (
        tokenize(labeled_tweets).loc[3, "tokenized"]
        == "rt @baum_erik : lol i am not surprised "
        "these 2 accounts blocked me @femfreq "
        "#feminazi #gamergate & @momsagainstwwe "
        "#paranoidparent http://t.câ€¦"
    )
