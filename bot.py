#!/usr/bin/env python
import tweepy, time, sys, datetime, string, random
#from our keys module (keys.py), import the keys dictionary
from keys import keys

#argfile = str(sys.argv[1])

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#^^ all this stuff is for authenticating

def scramble(tweet):
    tweetText = tweet.text
    userHandle = "@" + tweet.user.screen_name
    newtext = userHandle + " "
    for iter in range(len(userHandle) + 2, len(tweetText)):
        char = tweetText[iter]
        if(char.isalpha()):
            randNum = random.randint(0, 9)
            if randNum > 4:
                newtext = newtext + char.upper()
            else:
                newtext = newtext + char.lower()
        else:
            newtext = newtext + char
    return newtext

while True:
    print "Searching for new tweet..."
    time.sleep(1)
    twts = api.search(q="@clapbacksponge")
    if len(twts) > 0:
        for s in twts:
            tweet = s.text[16:]
            if s.favorite_count == 0:
                print "Current tweet: %(tweet)s" % {'tweet': tweet}
                print "Favorited yet: No, needs a meme\n"
                m = scramble(s)
                api.update_with_media("spongebobicon.jpg", m, s.id)
                api.create_favorite(s.id_str)
                time.sleep(1)
            else:
                print "Favorited yet: Yes, meme has already been given"
                print "Current tweet: %(tweet)s\n\n" % {'tweet': tweet}
                time.sleep(1)
