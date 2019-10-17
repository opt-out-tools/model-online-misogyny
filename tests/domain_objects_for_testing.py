import pandas as pd


def preprocess_normalize():
    tweets = [
        "rt <user> feminists take note <hashtag> <hashtag> <url>",
        "rt <user> antis stop treating blocks trophies soon feminists stop "
        "treating "
        "blocks arguments đÿ \uf190 ¸ â ˜ • "
        "<hashtag>",
        "<user> <user> cue nafalt 3 2 1",
        "rt <user> lol i surprised 2 accounts blocked <user> <hashtag> <hashtag> & "
        "<user> <hashtag> <url>",
    ]
    return pd.DataFrame({"normalized": tweets})


def preprocess_tokenize():
    tweets = [
        "rt @asredasmyhair : feminists , take note . #femfreefriday "
        "#womenagainstfeminism http://t.co/j2hqzvj8cx",
        "rt @allstatejackie : antis will stop treating blocks as trophies as soon "
        "as feminists stop treating blocks as arguments . đÿ \uf190 ¸ â ˜ • "
        "#gamergate",
        "@mgtowknight @factsvsopinion . . . cue the nafalt in 3 . . 2 . . . 1 . . .",
        "rt @baum_erik : lol i am not surprised these 2 accounts blocked me "
        "@femfreq #feminazi #gamergate & @momsagainstwwe #paranoidparent "
        "http://t.câ€¦",
    ]
    return pd.DataFrame({"tokenized": tweets})


def preprocess_clean():
    tweets = [
        "rt @asredasmyhair feminists take note #femfreefriday "
        "#womenagainstfeminism http://t.co/j2hqzvj8cx",
        "rt @allstatejackie antis stop treating blocks trophies soon feminists "
        "stop treating blocks arguments đÿ \uf190 ¸ â ˜ • #gamergate'"
        "@mgtowknight @factsvsopinion cue nafalt 3 2 1",
        "rt @baum_erik lol i surprised 2 accounts blocked @femfreq #feminazi "
        "#gamergate & @momsagainstwwe #paranoidparent http://t.câ€¦",
    ]
    return pd.DataFrame({"cleaned": tweets})


def create_pipeline_data(pipeline_name: str) -> pd.DataFrame:
    """ Returns data processed according to the pipeline chosen.

    Args:
        pipeline_name (str): name of preprcoessing pipeline.

    Returns:
        dataframe (pandas df):
    """
    pipeline = {
        "normalize": preprocess_normalize(),
        "tokenize": preprocess_tokenize(),
        "clean": preprocess_clean(),
    }
    return pipeline[pipeline_name]


def create_dataframe_of_labeled_tweets():
    tweets = [
        "RT @asredasmyhair: Feminists, take note. #FemFreeFriday "
        "#WomenAgainstFeminism http://t.co/J2HqzVJ8Cx",
        "RT @AllstateJackie: Antis will stop treating blocks as trophies as "
        "soon as feminists stop treating blocks as arguments. đŸ¸â˜• "
        "#GamerGate",
        "@MGTOWKnight @FactsVsOpinion ...cue the NAFALT in 3..2...1...",
        "RT @baum_erik: Lol I'm not surprised these 2 accounts blocked me "
        "@femfreq #FemiNazi #Gamergate &amp; @MomsAgainstWWE #ParanoidParent "
        "http://t.câ€¦",
    ]
    return pd.DataFrame(
        {
            "text": tweets,
            "label": pd.Series([1 if number % 2 == 0 else 0 for number in range(0, 4)]),
        }
    )
