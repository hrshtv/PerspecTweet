# PerspecTweet  

Analyses tweets according to various criteria (like keywords, hashtags, username, etc) and displays a bar graph having the score of 7 emotions:

- Disgust
-  Surprise 
-  Neutral
-  Anger
- Sad
- Happy
- Fear  

For example, [#ChineseVirus](https://twitter.com/search?q=%23ChineseVirus&src=typeahead_click) was trending on Twitter. The follwing were the results obtained when 5000 tweets were analysed.

<p align="center">
  <img width="460" height="300" src="images/example1.png">
</p>

The program depends heavily on how a weight/score is assigned to each emotion for every word in [emotions](emotions.csv) file, which I obtained from [Kaggle](https://www.kaggle.com/iwilldoit/emotions-sensor-data-set), and thus the results may not always be accurate. 
