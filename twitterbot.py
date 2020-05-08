# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:43:45 2020

@author: kowsh

to use any of this features need to create a developer for twitter
"""
#program to follow a random follower
import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

api = tweepy.API(auth)
def limit_error(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(2000)
def follow():
    for follower in limit_error(tweepy.Cursor(api.followers).items()):
        if follower.name == 'popclick':
            follower.follow()
            print('found')
    else:
        print('not found')

def like():
#can change to like rt etc
    for tweet in limit_error(tweepy.Cursor(api.search, 'poi').items(3)):
        try:
            tweet.favorite()
            print('liked')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break