import tweepy

# Enter your API keys and tokens here
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate the app
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing the keywords "web3" and "remote job"
tweets = api.search_tweets(q="web3 remote job", lang="en", count=100)

# Print the text of each tweet
for tweet in tweets:
    print(tweet.text)
