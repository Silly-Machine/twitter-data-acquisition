import tweepy
import time


class tools:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = self.authenticate()
        self.api = self.connect()

    def authenticate(self):
        try:
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            auth.set_access_token(self.access_token, self.access_token_secret)
            return auth
        except Exception as e:
            return e.message
            
    def connect(self):
        return tweepy.API(self.auth, wait_on_rate_limit=True)

    def get_tweets(self, query="", retweets=False, lang="pt-br", tweet_mode="extended", count=10):
        query = query if retweets else query + " -filter:retweets"
        try:
            return self.api.search_tweets(q=query, count=count, lang=lang, tweet_mode=tweet_mode,)
        except Exception as e:
            return e.message
          
    def get_user_timeline(self, screen_name, count=10):
        return self.api.user_timeline(screen_name=screen_name, count=count)

    def get_user_info(self, screen_name):
        return self.api.get_user(screen_name=screen_name)

    def get_user_followers(self, screen_name):
        return self.api.followers(screen_name=screen_name)

    def get_user_following(self, screen_name):
        return self.api.friends(screen_name=screen_name)

    def get_user_favorites(self, screen_name):
        return self.api.favorites(screen_name=screen_name)

    def get_user_lists(self, screen_name):
        return self.api.lists_all(screen_name=screen_name)

    def get_user_list_memberships(self, screen_name):
        return self.api.lists_memberships(screen_name=screen_name)

    def get_user_list_subscriptions(self, screen_name):
        return self.api.lists_subscriptions(screen_name=screen_name)
