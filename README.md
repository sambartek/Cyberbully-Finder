## Inspiration
Cyberbullying is becoming an increasing problem on social media and it is hard to make people change their online behavior.  Individuals feel as if they are actually hurting anyone with the content that they post on social media sites, but in reality it can have a major impact on cyberbully victims.
## What it does
Our program searches the tweets of the user and the users friends to find if they have aggressive or negative language patterns that insinuate cyberbullying patterns, then it flags those users and returns their names at the end with a percentage of how many of their tweets are considered mean. 
## How We built it
We used the Twitter API and the Watson Natural Language Classifier API to gather and filter through the Twitter information. Using the Watson API, we were able to scan through the tweets to find cyberbullying patterns in the tweets.  Before scanning the tweets,  we had to "train" the Watson API to recognize cyberbullying behavior.  If cyberbullying patterns were found, we flagged the friend and when the program finished we returned a list of the users friends that were considered cyberbullies and the percentage of mean tweets from that friend.
## Challenges We ran into
We had trouble figuring how to get the Twitter data, and how to properly train the Watson Natural Language Classifier API.
## Accomplishments that We're proud of
We are proud that we have a working model, and that the Cyberbullying Finder solves a real issue and can make a true impact on individuals.
## What We learned
How to use API's in python, how to query Twitter data using their API, machine learning techniques, and how to use the Watson API.
## What's next for Cyberbully Flagger
Next we want to make it scaleable for a website, so that anyone around the world can use it.  Also to make it useable for other platforms besides Twitter.
