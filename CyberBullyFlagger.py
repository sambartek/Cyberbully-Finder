import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

#twitter config
consumer_key = "IMz6l2MAyxTQtzIaqfEZxKZe5"  # ENTER YOUR API KEY
consumer_secret = "db0AQe0DCTpDw2te8egPBLZ82hsUWrQGz5OD8t2Rmpb2Y2NX23"  # ENTER YOUR API SECRET
access_token = "791676519202430976-lD6f6EWUOZQRhw8Vru8wubcCikJ7lHp"  # ENTER YOUR ACCESS TOKEN"
access_secret = "DPTnmhgxpup8wH1JfmNeW5RrEazFBblWveJrmROsPfgLf"  # ENTER YOUR ACCESS TOKEN SECRET
callback_url = "http://builditsociety.com/"
twitter_api = twitter.Api(consumer_key, consumer_secret, access_token, access_secret)
api = twitter.Api(consumer_key, consumer_secret, access_token, access_secret)

#watson config
nlc_username='f0099645-59b1-4260-83c6-14b4e479c004'
nlc_password='6QYsOarXYuc5'
natural_language_classifier = NaturalLanguageClassifier(username=nlc_username, password=nlc_password)

#menu
print ""
user = raw_input("Enter a Twitter handle: @")
user = "@" + user
print "Checking for " + user + " ..."
account = twitter_api.GetUser(screen_name = user);


# global constants
twt_num = 20
limit = 2

#tweets from user
nasty = 0
statuses = twitter_api.GetUserTimeline(screen_name=user, count=twt_num, include_rts=False)
for status in statuses:
    if (status.lang == 'en'):  # English tweets
        classes = natural_language_classifier.classify('f48968x109-nlc-5062', status.text.encode('utf-8'))
        if (classes["top_class"] == "cyberbully"): # checks user tweets for bullying
            nasty += 1
mean = ((float(nasty) / twt_num) * 100)
#if(nasty >= limit):
print '\033[1m' + account.name
print '\033[0m' + "%.0f%% mean tweets" % mean

# friends
friendlies = twitter_api.GetFriends(screen_name=user)#list of friends
flagged =[]
counter = 0
for friend in friendlies:#loop through friends
    handle = friend.screen_name
    friendStatuses = twitter_api.GetUserTimeline(screen_name=handle, count=twt_num, include_rts=False)
    bad = 0
    for friendStatus in friendStatuses:#loops through tweets for each friend
        if (friendStatus.lang == 'en'):  # English tweets
            classes = natural_language_classifier.classify('f48968x109-nlc-5062', friendStatus.text.encode('utf-8'))
            if (classes["top_class"] == "cyberbully"):
                bad += 1  
    if(bad > limit):
    	percent = ((float(bad) / twt_num) * 100)
        flagged.append(friend.name)
        counter += 1
        print'\033[1m' + friend.name
        print '\033[0m' + "%.0f%% mean tweets" % percent #find out how to make it into percentage
		
print "You are following \033[1m %d \033[0m cyberbullies." % counter	

if counter > 2: # checks if user has bully friends
	print "You might want to reconsider who you are following."	
if mean > 10: # checks if the user is a bully
	print "You have been flagged for cyberbullying."
	print "Think how your tweets might affect others before you post."
print ""
	






