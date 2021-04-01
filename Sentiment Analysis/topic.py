pip install nltk
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
message_text = '''Like you, I am getting very frustrated with this process. I am genuinely trying to be as reasonable as possible. I am not trying to "hold up" the deal at the last minute. I'm afraid that I am being asked to take a fairly large leap of faith after this company (I don't mean the two of you -- I mean Enron) has screwed me and the people who work for me.'''
scores = sid.polarity_scores(message_text)

for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end="")
##each words
df = pd.read_csv("C:/Users/DCUK/Desktop/isabelle/Krish/Sentiment analysis/td_questions.csv", usecols=["user_id", "question", "content"], index_col="user_id")
df_id = df.loc[205783]

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
import nltk.data
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
str1 = df_id["question"].tolist()
text = ' '.join(str1)
tokens = nltk.word_tokenize(text)
result = []
sid = SentimentIntensityAnalyzer()
for i in tokens:
    print(i)
    scores = sid.polarity_scores(i)
    for key in sorted(scores):
            print('{0}: {1}, '.format(key, scores[key]), end='')
    print()
            result.append(i, '{0}: {1}, '.format(key, scores[key]), end='')


##sentence
df = pd.read_csv("C:/Users/DCUK/Desktop/isabelle/Krish/Sentiment analysis/td_questions.csv", usecols=["user_id", "question", "content"], index_col="user_id")
df_id = df.loc[205783]

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
import nltk.data
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
str1 = df_id["question"].tolist()
text = '.'.join(str1)
sid = SentimentIntensityAnalyzer()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = tokenizer.tokenize(text)

for sentence in sentences:
        print(sentence)
        scores = sid.polarity_scores(sentence)
        for key in sorted(scores):
                print('{0}: {1}, '.format(key, scores[key]), end ='')

        print()



from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer ()
for sentence in hotel_rev:
    print (sentence)
    ss = sid.polarity_scores (sentence)
    for k in ss:
        print (‘{0}: {1}, ‘.format (k, ss[k]), end =’’)
        print ()

import collections
import pandas as pd
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
import nltk.data
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/DCUK/Desktop/isabelle/Krish/Sentiment analysis/td_questions.csv", usecols=["user_id", "question", "content"], index_col="user_id")
df_id = df.loc[205783]
str1 = df_id["question"].tolist()
text = ' '.join(str1)
tokens = nltk.word_tokenize(text)
tokens = ' '.join(tokens)
wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in tokens.lower().split():
    word = word.replace(".", "")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

word_counter = collections.Counter(wordcount)
from collections import Counter
cnts = Counter(wordcount)

df = pd.DataFrame.from_dict(cnts, orient='index').reset_index()
df.columns = ['key', 'cnts']

df.to_excel("id205783_q_count.xlsx")