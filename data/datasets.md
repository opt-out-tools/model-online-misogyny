# Datasets targeting sexism
 
The goal of this page is to provide a survey of existing datasets targeting sexism in social media, 
along with a summary of the data collection and labeling mechanism and potential issues. This should give 
a good overview of which datasets can and should be used in research, as well as learnings about how to
improve our own collection and labeling process. 

If you want to add a dataset to this page, please make sure to include the info bellow: 

- paper/blogpost that accompany the published dataset as title
- description
- data collection process
- labeling mechanism (should include details about annotation schema)
- potential issues
- learnings & comments

### 1. Waseem, Zeerak, and Dirk Hovy. "Hateful symbols or hateful people? predictive features for hate speech detection on twitter." Proceedings of the NAACL student research workshop. 2016.

#### Description
...

#### Data collection process
...

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


### 3. Arango, Aymé, Jorge Peréz, and Barbara Poblete. "Hate Speech Detection is Not as Easy as You May Think:
### A Closer Look at Model Validation"
Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’19), July 21–25, 2019, Paris, France. ACM, New York, NY, USA

Link: https://users.dcc.uchile.cl/~jperez/papers/sigir2019.pdf

#### Description
...

#### Data collection process
...

#### Labeling mechanism
...

#### Potential issues
...

#### Learnings & Comments

... 
