#getPosts

import numpy as np
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

file_loc=r"Experts.csv"
df=pd.read_csv(file_loc)

from flask import Flask
from flask_ask import Ask, statement
import tweepy 
from tweepy import OAuthHandler

app = Flask(__name__)
ask = Ask(app, '/')

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret =''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def getTweetsForkeyword(Keyword):
    results = api.user_timeline(screen_name=Keyword,tweet_mode="extended",count=100)
    tweets=[]

    for tw in results:
        temp1 = tw.full_text
        temp2 = tw._json["entities"]["urls"]
        temp3 = tw._json["entities"]["user_mentions"]
        temp4 = tw._json["entities"]["hashtags"]

        if len(temp2) !=0:
            temp2=temp2[0]["expanded_url"]
        else:
            temp2=""
        
        temp=[]
        if len(temp3) !=0:
            for i in range(len(temp3)):
                temp.append(temp3[i]["screen_name"])
        else:
            temp=""
        
        tempp=[]
        if len(temp4) !=0:
            for i in range(len(temp4)):
                tempp.append(temp4[i]["text"])
        else:
            tempp=""
        
        tweets.append((temp1,temp2,temp,tempp))
    
    return tweets 

posts_all={}
writer = pd.ExcelWriter('Posts.xlsx', engine='xlsxwriter')

for i in df["TwitterName"]:
    posts=getTweetsForkeyword(i)
    df_twitter = pd.DataFrame(data = posts)
    df_twitter.to_excel(writer, sheet_name=i,index=False,header=["Post","URL","Names","Hashtag"])

writer.save()

'''
for i in df["TwitterName"]:
    posts=getTweetsForkeyword(i)
    posts_all[i]=posts

df_twitter = pd.DataFrame(data = posts_all)
df_twitter.to_csv("Posts.csv",index=False,header=True)
'''
