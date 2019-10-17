import pandas as pd


class Pipeline:
    @classmethod
    def create_tweets_dataframe_with_labels(cls):
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
                "label": pd.Series(
                    [1 if number % 2 == 0 else 0 for number in range(0, 4)]
                ),
            }
        )

    def preprocess_pipeline(self, pipeline_name):

        if pipeline_name == "normalize":
            return self._preprocess_normalize()

        if pipeline_name == "tokenize":
            return self._preprocess_tokenize()

        return self._preprocess_clean()

    @classmethod
    def _preprocess_normalize(cls):
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
        return cls(pd.DataFrame({"normalized": tweets}))

    @classmethod
    def _preprocess_tokenize(cls):
        tweets = [
            "rt @asredasmyhair : feminists , take note . #femfreefriday "
            "#womenagainstfeminism http://t.co/j2hqzvj8cx",
            "rt @allstatejackie : antis will stop treating blocks as trophies as soon "
            "as feminists stop treating blocks as arguments . đÿ \uf190 ¸ â ˜ • "
            "#gamergate",
            "@mgtowknight @factsvsopinion . . . cue the nafalt in 3 . . 2 . . . 1 . . "
            ".",
            "rt @baum_erik : lol i am not surprised these 2 accounts blocked me "
            "@femfreq #feminazi #gamergate & @momsagainstwwe #paranoidparent "
            "http://t.câ€¦",
        ]
        return cls(pd.DataFrame({"tokenized": tweets}))

    @classmethod
    def _preprocess_clean(cls):
        tweets = [
            "rt @asredasmyhair feminists take note #femfreefriday "
            "#womenagainstfeminism http://t.co/j2hqzvj8cx",
            "rt @allstatejackie antis stop treating blocks trophies soon feminists "
            "stop treating blocks arguments đÿ \uf190 ¸ â ˜ • #gamergate'"
            "@mgtowknight @factsvsopinion cue nafalt 3 2 1",
            "rt @baum_erik lol i surprised 2 accounts blocked @femfreq #feminazi "
            "#gamergate & @momsagainstwwe #paranoidparent http://t.câ€¦",
        ]
        return cls(pd.DataFrame({"cleaned": tweets}))
