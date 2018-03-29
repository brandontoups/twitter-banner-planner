from __future__ import absolute_import, print_function
from datetime import date
import calendar
import tweepy
import os

# OAuth Authentication
# Consumer keys can be found on your application's 'Keys and Access Tokens'
# page located at https://dev.twitter.com/apps (
consumer_key=""
consumer_secret=""

# Access tokens can be found on your application's 'Keys and Access Tokens'
# page located at https://dev.twitter.com/apps
access_token=""
access_token_secret=""

# Using Tweepy's OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# what day it is 
date = date.today()
day_of_week = calendar.day_name[date.weekday()]

# Setting file_name to the day_of_week.jpg
file_name = str(day_of_week + '.jpg')

api = tweepy.API(auth)

# Update the authenticating user's profile image. 
# Valid formats: GIF, JPG, or PNG
api.update_profile_banner(file_name)
