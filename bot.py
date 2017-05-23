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
class StreamListener(tweepy.StreamListener):

    def on_status(self, s):
        print(s.text)
        tweet = s.text[16:]
        userHandle = "@" + s.user.screen_name
        if s.favorite_count == 0:
            print "Current tweet: \"%(tweet)s\" by user %(userHandle)\n" % {'tweet': tweet, 'userHandle' : userHandle}
            m = scramble(s)
            api.update_with_media("spongebobicon.jpg", m, in_reply_to_status_id = s.id_str)
            print "Meme given. \n"
            time.sleep(1)
        else:
            print "Current tweet: \"%(tweet)s\" by user %(userHandle)\n" % {'tweet': tweet, 'userHandle' : userHandle}
            print "Meme already given, skipping over this tweet.\n"
            time.sleep(1)

    def on_error(self, status_code):
        if status_code == 420:
            return False

def scramble(tweet):

    tweetText = tweet.text[16:]
    userHandle = "@" + tweet.user.screen_name
    newtext = userHandle + " "
    for iter in range(0, len(tweetText)):
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

print "Bot started up.\n"
stream_listener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=stream_listener)
stream.filter(track=['@clapbacksponge'])
