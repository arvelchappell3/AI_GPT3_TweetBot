
import tweepy
import openai

#Consider moving these keys to .env file and reading in with os.getenv
consumer_key = 'REPLACE_THIS_WITH_YOUR_CONSUMER_KEY'
consumer_secret = 'REPLACE_THIS_WITH_YOUR_CONSUMER_SECRET'
access_token = 'REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN'
access_token_secret = 'REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN_SECRET'

#Set up OpenAi Credentials from env variables
openai.api_key = 'REPLACE_THIS_WITH_OPENAI_APIKEY'

# Set up Twitter OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create GPT3_Tweet
G_prompt = "I am a Cyborg master tweeter. Don't @ me but enjoy my tweets on how Cyborgs will take over."

G_Tweet = openai.Completion.create(
            model="text-davinci-002",                   #Suggest reading openai material to know what these items are
            prompt=G_prompt,
            temperature=0.88,
            max_tokens = 150,
        )

# Write a tweet to push to our Twitter account
tweet = G_Tweet.choices[0].text

api.update_status(status=tweet)