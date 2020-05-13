import string
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

text = open('read.txt',encoding='utf-8').read()
lower_text=text.lower()
final_text=lower_text.translate(str.maketrans('','',string.punctuation))
words = word_tokenize(final_text)

stopWords = set(stopwords.words('english'))
final_words = []

for word in words:
    if word not in stopWords:
        final_words.append(word)


emotion_list = []
with open('emotions.txt',"r") as file:
    for line in file:
        clear_line=line.replace("\n",'').replace(",",'').replace("'",'').strip()
        vword , emotion = clear_line.split(':')

        if vword in final_words:
            emotion_list.append(emotion)


w=Counter(emotion_list)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)

    if score['neg'] > score['pos']:
        print("Negative Sentiments")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentiment_analyse(final_text)
fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('emotion_graph.png')
plt.show()