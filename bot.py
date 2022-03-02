import os
from twitter_bot_class import TwitterBot
import json
import config

########## EDIT THESE LINES AS NEEDED ###################
#Tweet ID, (get it from the URL of the tweet)
tweet_id = "1498719341147262983"
#1498751283326590983, 1498698889288986630, 1498318615279550471
#If you need to leave a comment, set this to True and change the text and tags for what you want.
tagging=True
textandtags = "Yeah @bjow5" #"@bjow5 @geneverse_ @wisey_9 check out this NFT"

#If you need to retweet the post, set to True
retweeting=True

#If you need to retweet the post, set to True
following=True

#Your Twitter ID, get it from here: https://tweeterid.com/
user_id = "1265067462359314432"
#########################################################

#Compiling payloads based on above
payloadpost = {"text": textandtags, "reply": {"in_reply_to_tweet_id": tweet_id}}
payloadretweet = {"tweet_id": tweet_id }
tweetparams={"ids": tweet_id, "expansions":"entities.mentions.username", "user.fields":"entities"}

#bearer_token = config.BEARER_TOKEN
consumer_key = config.API_KEY
consumer_secret = config.API_KEY_SECRET
username = config.username
password = config.password
email = config.email

#########################################################

#Checks API call was successful
def responder(response,code=201,hype="GOOD"):         
    if response.status_code != code:
              raise Exception(
                  "Request returned an error: {} {}".format(response.status_code, response.text)
              )

    print(hype+" code: {}".format(response.status_code))
    #json_response = response.json()
    #print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":

    #Initialise the Bot
    pj = TwitterBot(email, password, username)
    
    #Authorize the bot
    oauth=pj.authorize(username,password,consumer_key,consumer_secret)
      
    #######
    # Get tweet  https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id
    response = oauth.get(
        "https://api.twitter.com/2/tweets", params=tweetparams
    )
    responder(response,200,"GOOD TWEET")
    
    #Get list of @mentions which we can use to follow
    json_response = response.json()
    try:
      follows=[i["id"] for i in json_response["includes"]["users"]]
    except:
      print("Could not follow, no tags in tweet probably.")
      following=False
    ##########

    ##########
    #Follow all users mentioned https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following
    if following:
        for f in follows:
          payloadfollow = {"target_user_id": f}
          response = oauth.post(
              "https://api.twitter.com/2/users/{}/following".format(user_id), json=payloadfollow
              )  
          responder(response,200,"GOOD FOLLOW")

        
    ##########

    ##########
    #Comment and Tag friends
    #use in_reply_to_tweet_id https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets
    if tagging:
      response = oauth.post(
          "https://api.twitter.com/2/tweets", json=payloadpost
      )
      responder(response,201,"GOOD TAG and COMMENT")
    ##########
    
    ##########
    #Retweet https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/post-users-id-retweets
    if retweeting:
      response = oauth.post(
          "https://api.twitter.com/2/users/{}/retweets/".format(user_id), json=payloadretweet
          )
      responder(response,200,"GOOD RETWEET")
    ##########
        
