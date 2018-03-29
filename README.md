# Twitter Banner Planner

## Description

One man's journey throughout the week. This updates your Twitter background based on the current progression of the week. Each day, the background is updated with the next progression in the 'Ascent of Man' image. Pictures better viewed for mobile Twitter application.

## Getting Started

First, install [Tweepy](http://www.tweepy.org/), a wrapper for the Twitter API. 
```
pip install tweepy
```

Next, set up a Cron Job. This will allow the program to run every day at midnight. To schedule a Cron Job, enter ```crontab -e``` into terminal. Then, copy in the job found in [cron.txt](cron.txt). Save and close. 

## Note

- Cron Jobs only run when the computer is awake, but will run programs upon waking if your computer is not awake at midnight. 
- This is run using Python 2.7. Make sure the path you specify in Crontab reflects that. 

## Credit

Hat tip to dave's [tweet](https://twitter.com/dontsave/status/976495944224165888) for the inspiration. 

Twitter: [@dontsave](https://twitter.com/dontsave?lang=en) 

Website: dontsave.com