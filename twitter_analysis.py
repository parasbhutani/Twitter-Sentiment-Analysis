import string
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona vrus')\
        .setSince("2020-02-01")\
        .setUntil("2020-04-30")\
        .setMaxTweets(100)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)  
    all_tweets=[]
    for tweet in tweets:
        all_tweets.append(tweet.text)
    return(all_tweets)

text_tweet = get_tweets()
length=len(text_tweet)
text = ""

for i in range(0,length):
    text = text_tweet[i] + " " + text



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
        #print("Word:" + vword + " " + "Emotion :" + emotion)

        if vword in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('emotion_graph.png')
plt.show()