# DiscordTwitterBot
Author: Pedro Arredondo
Date: 9-21-21
Description:  Posts tweets under the python hashtag onto a discord server

.env file not included. please use your discord and twitter api keys and tokens

After getting the keys for python and discord the bot runs the StreamListener and the loop to post tweets

The stream listener can post from both authors and hashtags
To do this fine this line MS.filter(track=['#python'],is_async=True), and add a comma after the brackets with follow=['Twitter user id']
should look something like this
MS.filter(track=['#hashtag', '#hashtag2'],follow=['insert twitter id', 'insert second twitter id'],is_async=True)

All the elif's should be merged into 1 if statement, but the only reason I did not was because it was more legible

One issue that was found when testing was that the stream listener would add more than 1 of the same tweet, so I had to use a set to stop duplicates
