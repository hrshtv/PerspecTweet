import string
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import GetOldTweets3 as got # 3rd party module for getting old tweets

#Parameters
username ="@"
keyword = input("Enter keyword: ")
total_tweets = int(input("Total tweets you want: "))
start_date = "2018-03-17" # "YY-MM-DD"
end_date = "2019-03-18" # If you want todays tweets too, enter: todays date + 1                                          
lang = "english"
"""
Criterias you can add:
    .setUsername(username)\
    .setSince(start_date)\
    .setUntil(end_date)\
    .setQuerySearch(keyword)\
    .setTopTweets(True)\
    .setMaxTweets(total_tweets)\
    .setLang("english")
    #.setNear("")\
    #.setWithin("")\
"""

tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keyword)\
                                           .setMaxTweets(total_tweets)\
                                           .setLang(lang)\
                                           .setSince("2020-01-01")\
                                           .setUntil("2020-03-15")
                                           #.setNear("")\
                                           #.setWithin("")\
                                           #.setTopTweets(False)\
                                         
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

text_form = str([[tweet.text] for tweet in tweets])
cleaned = text_form.lower().translate(str.maketrans('','',string.punctuation))
tokenized = word_tokenize(cleaned, "english") # The list containing all the tokens, better than "split()" method
final = [i for i in tokenized if i not in stopwords.words("english")] # Removing stopwords

emo = pd.read_csv('emotions.csv', delimiter = ',')

# Emotional Arrays :')
word = np.char.strip(np.asarray(emo["word"], str))
disgust = np.asarray(emo["disgust"], float)
surprise = np.asarray(emo["surprise"], float)
neutral = np.asarray(emo["neutral"], float)
anger = np.asarray(emo["anger"], float)
sadness = np.asarray(emo["sad"], float)
happy = np.asarray(emo["happy"], float)
fear = np.asarray(emo["fear"], float)

emotions = [disgust, surprise, neutral, anger, sadness, happy, fear]

dis = sur = neu = ang = sad = hap = fea = 0 # Present just to enhance readability 

scores = np.asarray([dis, sur, neu, ang, sad, hap, fea], float)

limit = 0.05 # As each word has some non-zero score in each emotion class, over a lot of words, this giets accumulated and contaminates the final data. Thus we set a limit.

for i in final:
    if i in word:
        b = (word == i)
        for j in range(7):
            if (emotions[j])[b] > limit:
                scores[j] += float((emotions[j])[b])
                
emotion_list = ["disgust","surprise","neutral","anger","sad","happy","fear"]
 
fig, ax = plt.subplots()
ax.bar(emotion_list, scores)
fig.autofmt_xdate()
plt.title("Twitter Sentiment Analysis: " + keyword)
plt.xlabel("Emotions")
plt.ylabel("Score")
plt.show()
