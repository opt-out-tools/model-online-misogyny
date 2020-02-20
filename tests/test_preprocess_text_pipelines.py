from src.text.pipelines import clean, normalize, tokenize


def test_normalize(labeled_tweets):
    normalized = normalize(labeled_tweets)
    assert (
        normalized.loc[0, "normalized"] == "rt <user> feminists take note <hashtag> "
        "<hashtag> <url>"
    )
    assert (
        normalized.loc[1, "normalized"] == "rt <user> antis stop treating blocks "
        "trophies soon feminists stop treating "
        "blocks arguments đÿ \uf190 ¸ â ˜ • "
        "<hashtag>"
    )
    assert normalized.loc[2, "normalized"] == "<user> <user> cue nafalt 3 2 1"
    assert (
        normalized.loc[3, "normalized"] == "rt <user> lol i surprised 2 accounts "
        "blocked <user> <hashtag> <hashtag> & "
        "<user> <hashtag> <url>"
    )


def test_clean(labeled_tweets):
    cleaned = clean(labeled_tweets)
    assert (
        cleaned.loc[0, "cleaned"]
        == "rt @asredasmyhair feminists take note #femfreefriday #womenagainstfeminism "
        "http://t.co/j2hqzvj8cx"
    )
    assert (
        cleaned.loc[1, "cleaned"]
        == "rt @allstatejackie antis stop treating blocks trophies soon feminists stop "
        "treating blocks arguments đÿ \uf190 ¸ â ˜ • #gamergate"
    )
    assert cleaned.loc[2, "cleaned"] == "@mgtowknight @factsvsopinion cue nafalt 3 2 1"
    assert (
        cleaned.loc[3, "cleaned"]
        == "rt @baum_erik lol i surprised 2 accounts blocked @femfreq #feminazi "
        "#gamergate & @momsagainstwwe #paranoidparent http://t.câ€¦"
    )


def test_tokenize(labeled_tweets):
    tokenized = tokenize(labeled_tweets)
    assert (
        tokenized.loc[0, "tokenized"] == "rt @asredasmyhair : feminists , take note "
        ""
        ". #femfreefriday #womenagainstfeminism "
        "http://t.co/j2hqzvj8cx"
    )
    assert (
        tokenized.loc[1, "tokenized"] == "rt @allstatejackie : antis will stop "
        "treating blocks as trophies as soon as "
        "feminists stop treating blocks as "
        "arguments . đÿ \uf190 ¸ â ˜ • #gamergate"
    )
    assert (
        tokenized.loc[2, "tokenized"] == "@mgtowknight @factsvsopinion . . . cue "
        "the nafalt in 3 . . 2 . . . 1 . . ."
    )
    assert (
        tokenized.loc[3, "tokenized"] == "rt @baum_erik : lol i am not surprised "
        "these 2 accounts blocked me @femfreq "
        "#feminazi #gamergate & @momsagainstwwe "
        "#paranoidparent http://t.câ€¦"
    )
