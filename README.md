# Twitter Banner Planner

![](ascent-of-man.jpg?raw=true "")

## Description 
This updates your Twitter background based on the current progression of the week. Each day, the background is updated with the next progression in the 'Ascent of Man' image. Pictures better viewed for mobile Twitter application.

## Getting Started

First, set up a Twitter app at https://apps.twitter.com. This will generate an API Key, API Secret, Access Token, and Access Token Secret needed for OAuth.

ssh into your Raspberry Pi and get a clone of this repo on it.

Next, install [Tweepy](http://www.tweepy.org/), a wrapper for the Twitter API with ```pip install tweepy ```

To run the program at set intervals, set up a Cron Job. This allows the program to run every day at midnight. To schedule a Cron Job, enter ```crontab -e``` into Terminal. Then, copy in the job found in [cron.txt](cron.txt). Save and close. 

## Note

- Cron Jobs only run when the computer is awake, but will run programs upon waking if your computer is not awake at midnight. 
- Run using Python 2.7. Make sure the path you specify in Crontab reflects that. 

## Credit

Hat tip to dave's [tweet](https://twitter.com/dontsave/status/976495944224165888) for the inspiration. 

Twitter: [@dontsave](https://twitter.com/dontsave?lang=en) 

Website: www.dontsave.com

## Twitter
If you would like to see this in action, it is currently running on my Twitter [@brandonmtoups](https://twitter.com/brandonmtoups). Viewing on mobile is recommended, as the resolution of the images is low.
