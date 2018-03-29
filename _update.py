"""
author:   Brandon Toups
email:    bmt0015@auburn.edu
credits:  @dontsave
"""

from __future__ import absolute_import, print_function
from datetime import date
import calendar
import tweepy
import os.path

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

# Finding images in subdirectory 'images'
my_path = os.path.abspath(os.path.dirname(__file__))
filename = str("images/" + day_of_week + ".jpg")
# Relative path
path = os.path.join(my_path, filename)

# Update the authenticating user's banner.
# Valid formats: GIF, JPG, or PNG
api.update_profile_banner(path)
