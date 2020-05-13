import string
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

text = open('read.txt',encoding='utf-8').read()
lower_text=text.lower()
#print(string.punctuation)
final_text=lower_text.translate(str.maketrans('','',string.punctuation))
#print(final_text)
words = word_tokenize(final_text)
#print(words)
stopWords = set(stopwords.words('english'))
final_words = []

for word in words:
    if word not in stopWords:
        final_words.append(word)

#print(final_words)
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