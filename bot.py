#   bot.py

#   imports
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
import tweepy
import logging

#   logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#loads .env file
load_dotenv('botAttributes.env')

#   twitter keys
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_SECRET')

#   using keys for twitter to allow us to take info
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#   discord key
discord_TOKEN = os.getenv('DISCORD_TOKEN')

#   allows use of discord client
client = discord.Client()

#   global non-static variables that make life easier
mess = {None}

#   stream listener to dynamically take in tweets
class MSL(tweepy.StreamListener, discord.Client):
    #   when a new status is made it will be put into the set
    def on_status(self, status):
        global mess
        #   if someone retweets norio (because she is popular) the retweet will be ignored (to stop spam)
        try:
            #   if statements not optimized for legibility
            if(status.text.startswith("RT ")):
                logging.info("retweet")
            elif(status.is_quote_status):
                logging.info("quote tweet")
            elif(status.in_reply_to_user_id != None):
                logging.info("reply")
            else:
                #   adds to global set
                mess.add(status.id)
                logging.info("This is the status ID taken "+str(status.id))
                
        except:
            logging.error("error")
    
    #   logs error
    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            logging.error(status_code)

#   will post when logged
#   run streamlistener
#   and run loop
@client.event
async def on_ready():
    logging.info('bot has connected to Discord!')   
    logging.info("the program should start showing tweets")
    try:
        StreamListener = MSL()
        MS = tweepy.Stream(auth = api.auth, listener = StreamListener)
        MS.filter(track=['#python'],is_async=True)
        await client.get_channel(INSERT CHANNEL ID HERE).send("bot is online")
        auto_send.start()
    except:
        logging.error("loop cannot start")


#   loop so that the bot does not spam terribly
@tasks.loop(minutes=1)
async def auto_send():
    try:
        if None in mess:
            mess.pop()
            await client.get_channel(INSERT CHANNEL ID HERE).send(":upside_down:")
        await client.get_channel(INSERT CHANNEL ID HERE).send("http://twitter.com/anyuser/status/"+str(mess.pop()))
    except:
        logging.debug("none in set")

#   runs the client
client.run(discord_TOKEN)
