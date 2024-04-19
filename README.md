WARNING!!!

After Elon Musk made changes to the API of twitter the program no longer works, this project WAS complete years ago as of now i cannot in good faith have this ran today



# DiscordTwitterBot
Author: Pedro Arredondo
Date: 9-21-21
Description:  Posts tweets under the python hashtag onto a discord server

.env file not included. please use your discord and twitter api keys and tokens APP WILL NOT RUN UNLESS YOU GET YOUR OWN API KEYS

After getting the keys for python and discord the bot runs the StreamListener and the loop to post tweets

The stream listener can post from both authors and hashtags
To do this fine this line MS.filter(track=['#python'],is_async=True), and add a comma after the brackets with follow=['Twitter user id']
should look something like this
MS.filter(track=['#hashtag', '#hashtag2'],follow=['insert twitter id', 'insert second twitter id'],is_async=True)

All the elif's should be merged into 1 if statement, but the only reason I did not was because it was more legible

One issue that was found when testing was that the stream listener would add more than 1 of the same tweet, so I had to use a set to stop duplicates

REPLACE 'INSERT CHANNEL ID HERE' WITH YOUR OWN CHANNEL ID

To get a channel id, turn on developer mode on discord and right click a specific channel on your server, then select 'Copy ID'

BOT WILL NOT RUN AND WILL HAVE AN ERROR WITHOUT THIS
