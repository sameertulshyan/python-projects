import praw #python reddit API wrapper
from PyDictionary import PyDictionary
import enchant

#reddit login
reddit = praw.Reddit(client_id = "q0MhrRBL__hbPw",
						client_secret = "Isq4ljUs3Qviz9n6O2T8nauLcmI",
						username = "definebot123", 
						password = "definebot123",
						user_agent = "definebot by /u/stulshya") 

subreddit = reddit.subreddit("explainlikeimfive")

activate_phrase = "!define"

pydictionary = PyDictionary()
d = enchant.Dict("en_US")

def is_word(word):
	"""Determine if a given word is part of the English Dictionary"""
	return d.check(word)

#look for phrase and reply appropriately
for comment in subreddit.stream.comments(): #search through comments in the eli5 subreddit
	if activate_phrase in comment.body: #look for trigger phrase in each comment
		word = comment.body.replace(activate_phrase, "") #get the comment and remove the trigger phrase for processing
		try:
			if is_word(word): #use our function to check for english words
				words = pydictionary.meaning(word) #get the word's meaning as an object
				reply = [item[0] for item in words.values()] #get the index of a sentence
				comment.reply(word + ": " + reply[0]) #formulate a reply to the parent comment
				print("posted")
			else:
				reply = "This is not a valid word!" #let the parent comment know that the operation cannot be performed
				comment.reply(reply)
				print("posted")
		except:
			print("too frequent usage")