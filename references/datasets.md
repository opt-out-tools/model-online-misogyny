# Datasets targeting sexism
 
The goal of this page is to provide a survey of existing
datasets targeting sexism in social media, 
along with a summary of the data collection and labeling
mechanism and potential issues.
This should give a good overview of which datasets can
and should be used in research, as well as learnings about how to
improve our own collection and labeling process. 

If you want to add a dataset to this page, please
make sure to include the info bellow: 

- paper/blogpost that accompany the published dataset as title
- description
- data collection process
- labeling mechanism (should include details about annotation schema)
- potential issues
- learnings & comments

### 1. Waseem, Zeerak, and Dirk Hovy. "Hateful symbols or hateful people? predictive features for hate speech detection on twitter." Proceedings of the NAACL student research workshop. 2016.

#### Description
- 16K tweet identifiers annotated as “sexist”, “racist” and “non-hate”

#### Data collection process
...

#### Data set criticism (taken from #4)
- only 1,590 users generate all the data
- 491 generate all the “sexist” tweets
- only 8 users generate all the “racist” ones
- just a few users generate almost all the hateful data
- for the “sexist” label, there is a single user that generates 40% of all tweets
- for “racist” label, there is a single user that generates more that 90% of all tweets
-> *user overfitting* 

#### Labeling mechanism
...

### 2. Anzovino, Maria, Elisabetta Fersini, and Paolo Rosso. "Overview of the Task on Automatic Misogyny"
Identification at IberEval 2018." Proceedings of the Third Workshop on Evaluation of Human Language Technologies for Iberian Languages (IberEval 2018)

Link: http://personales.upv.es/prosso/resources/FersiniEtAl_IberEval18.pdf

#### Description
Data set provided to solve two tasks:
1) Misogyny Identification - discrimination of misogynistic contents from the non-misogynistic ones
2) Misogynistic Behavior and Target Classification - recognition of the targets that can be either specific users or groups of women together with the identification of the type of misogyny against women.

5 different types of misogyny:
- Stereotype & Objectification
- Dominance
- Derailing
- Sexual Harassment & Threats of Violence
- Discredit
For description of types, see paper.

#### Data collection process
*Step 1*:

Three approaches were employed to collect misogynistic text on Twitter:
* Streaming download using a set of representative keywords, e.g. bi\*\*h, w\*\*re, c\*nt
* Monitoring of potential victims accounts, e.g. gamergate victims and public feminist women
* Downloading the history of identified misogynist, i.e. explicitly declared hate against women on their Twitter profiles

Data collection phase:
20th of July 2017 to 30th of November 2017
-> corpus of 83 million tweets for English and 72 millions for Spanish

*Step 2*:  
- Among all the collected texts we selected a subset of tweets querying the database with the co-presence of keywords.
- No further details about this second step are mentioned (e.g. keywords)
- Final data set is created after the labelling phase.

#### Labeling mechanism
The labeling phase involved two steps: 
1) A gold standard was composed and labeled by two annotators, whose cases of disagreement were solved by a third experienced
contributor. 
2) The remaining tweets were labeled through a majority voting approach by external contributors on the CrowdFlower3 platform. The gold standard has been used for the quality control of the judgements throughout the second step.

#### Data set figures

|   | Train  |  Test |
|--:|--:|--:|
| English  | 3251  | 726  |
| Spanish  | 3307  | 831  |

#### Columns
“id”, “text”, “misogynous”, “misogyny category”, “target”

#### Potential issues
1) Keywords that are used to select tweets from originally collected corpus are not known. Makes it hard to judge what potential biases could be in the data set.
2) no user identification possible / no information about number of unique users -> could be that the model learns to distinguish between users not misogynous tweets from non-misogynous tweets.

#### Learnings & Comments
- good start but not really large data set


### 3. Thomas Davidson, Dana Warmsley, Michael W. Macy, and Ingmar Weber. 2017. "Automated Hate Speech Detection and the Problem of Offensive Language." In Proceedings of the Eleventh International Conference on Web and Social Media, ICWSM 2017, Montréal, Québec, Canada, May 15-18, 2017. AAAI Press, 512–515.

Link https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665/14843

#### Description
- define hate speech as language that is used to expresses hatred towards a targeted group or is intended to be derogatory, to humiliate, or to insult the members of the group. 
- 24,802 tweets annotated in three classes: 
1) hate speech
2) offensive but not hate speech
3) neither offensive nor hate speech

#### Data collection process
- We begin with a hate speech lexicon containing words and phrases identified by internet users as hate speech, compiled by Hatebase.org
- Using the Twitter API we searched for tweets containing terms from the lexicon, resulting in a sample of tweets from 33,458 Twitter users
- We extracted the time-line for each user, resulting in a set of 85.4 million tweets
- From this corpus we then took a random sample of 25k tweets containing terms from the lexicon
- we had them manually coded by CrowdFlower (CF) workers

#### Labeling mechanism
- annotation using CrowdFlower workers
- Workers were asked to label each tweet as one of three categories: hate speech, offensive but not hate speech, or neither offensive nor hate speech. 
- They were provided with our definition along with a paragraph explaining it in further detail.
- Users were asked to think not just about the words appearing in a given tweet but about the context in which they were
used. 
-They were instructed that the presence of a particular word, however offensive, did not necessarily indicate a tweet
is hate speech. 
- Each tweet was coded by three or more people. The intercoder-agreement score provided by CF is 92%.
- We use the majority decision for each tweet to assign a label. 
- Some tweets were not assigned labels as there was no majority class. This results in a sample of 24,802 labeled
tweets.

#### Distribution of labels
- Only 5% of tweets were coded as hate speech by the majority of coders and only 1.3% were coded unanimously,
demonstrating the imprecision of the Hatebase lexicon. 
- This is much lower than a comparable study using Twitter, where 11.6% of tweets were flagged as hate speech (Burnap and
Williams 2015), likely because we use a stricter criteria for hate speech. 
- The majority of the tweets were considered to be offensive language (76% at 2/3, 53% at 3/3)
- the remainder were considered to be non-offensive (16.6% at 2/3, 11.8% at 3/3)


### 4. Valerio Basile, Cristina Bosco, Viviana Patti, Manuela Sanguinetti, Elisabetta Fersini, Debora Nozza, Francisco Rangel, and Paolo Rosso. [n.d.]. "Shared Task on Multilingual Detection of Hate. SemEval 2019, Task 5"

Link: https://competitions.codalab.org/competitions/19935#learn_the_details-overview

#### Description 
“Multilingual detection of hate speech against immigrants and women in Twitter” task
hateful vs. non-hateful

#### Data set figures
- 9,000 tweets:
3,783 labelled as hateful 
5,217 as not hateful

### 5. Arango, Aymé, Jorge Peréz, and Barbara Poblete. "Hate Speech Detection is Not as Easy as You May Think:
### A Closer Look at Model Validation"
Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’19), July 21–25, 2019, Paris, France. ACM, New York, NY, USA

Link: https://users.dcc.uchile.cl/~jperez/papers/sigir2019.pdf

Github Repo (Including DATA) https://github.com/aymeam/User_distribution_experiments

#### Description
In this paper current state-of-the-art hate speech detection algorithms are investigated. Their experimental methodology and their generalizability to other datasets are studied closely. The findings evidence methodological issues, as well as an important dataset bias. As a consequence, performance claims of the current state-of-the-art have become significantly overestimated. The detected problems are mostly related to data overfitting and sampling issues. Implications for current research are discussed and experiments are re-conducted to give a more accurate picture of current state-of-the art methods.

#### Data sets used / under scrutiny
1) *Waseem and Hovy’s dataset* (Zeerak Waseem and Dirk Hovy. 2016. Hateful Symbols or Hateful People? Predictive Features for Hate Speech Detection on Twitter. In Proceedings of the Student Research Workshop, see # 1)
-> strong user bias, , 65% of the messages marked as hateful (“sexist” or “racist”) in Waseem and Hovy’s dataset were produced by only 2 users.
-> authors using this dataset have trained on the same sets of users on which they have later evaluated their models, involuntarily inducing a *user-overfitting effect*

2) Davidson et al. (see #3)

3) SemEval dataset (see #4) - used to test models on unseen data

#### Data set to mitigate above issues
*Step 1:*
- re-sample the data in the Waseem and Hovy dataset by placing a limit of at most 250 tweets per class for each user
- intermediate data set: 5,576 tweets, of which 1,490 are labelled as hateful 
-> hateful tweets are still underrepresented

*Step 2:*
- further enrich dataset with new users for hateful class
- added all of the hateful tweets from the Davidson et al. dataset (preserving the limit of at most 250 hateful messages per user)

*Final dataset*
7,006 examples
2,920 of which corresponded to the “hateful” class

-> shown to better generalize to previously unseen data

#### Potential issues
- If the tweets in the datasets are generated by only a small number of different users, then one could potentially reduce the hate-speech detection problem to a user-identification problem.

#### Learnings & Comments
- No overlap of users between training and test set -> user overfitting
- tweets need to stem from a considerable number of distinct users in each class
- produce datasets that do not contain important user bias!

NOTE: Due to data protection reasons, user information was not readily available in the datasets but was obtained by contacting the authors.
