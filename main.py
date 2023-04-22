import logging
import coloredlogs
from constants.api_keys import api_key, api_key_secret
from api.twitter_authenticator import TwitterAuthentication

if __name__ == '__main__':
    # setup logging
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    coloredlogs.install(level=logging.DEBUG, logger=logger)

    logger.info('Starting twitter sentiment Analysis')
    twitter_authenticator = TwitterAuthentication(api_key, api_key_secret, logger)

    auth = twitter_authenticator.authenticate_user()
    logger.info('Twitter Authentication Successful')