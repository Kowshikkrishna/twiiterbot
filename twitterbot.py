# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:43:45 2020

@author: kowshikkrishna

to use any of this features need to create a developer for twitter
"""
#program to automate some fn's in twitter
import tweepy
import time
#use your own twitter account 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

def limit_error(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(2000)
        
def follow():
    #can follow or unfollow anyone from your followers list
    for follower in limit_error(tweepy.Cursor(api.followers).items()):
        if follower.name == 'followername':
            follower.follow()
            print('found')
    else:
        print('not found')

def like():
#change the tweet object's function for any twitter function
    for tweet in limit_error(tweepy.Cursor(api.search, 'random').items(3)):
        try:
            tweet.favorite()
            print('liked')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
