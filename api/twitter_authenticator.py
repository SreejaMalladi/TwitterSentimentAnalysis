import tweepy
import logging


class TwitterAuthentication:
    api_key = ""
    api_secret_key = ""
    logger = logging.getLogger(__name__)

    def __init__(self, api_key, api_secret_key, logger):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.logger = logger

    def authenticate_user(self):
        auth = ""
        if self.api_key is None or self.api_secret_key is None:
            self.logger.error("API key or secret key is not present")
            return
        self.logger.info("Authenticating user")
        try:
            auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)

        except TypeError:
            self.logger.error("Error in authenticating user")
            return
        return auth
