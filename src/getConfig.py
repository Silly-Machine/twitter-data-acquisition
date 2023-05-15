import os
import dotenv

dotenv.load_dotenv(verbose=True)


def get_credentials():
    return {
        "consumer_key": os.getenv("CONSUMER_KEY"),
        "consumer_secret": os.getenv("CONSUMER_SECRET"),
        "access_token": os.getenv("ACCESS_TOKEN"),
        "access_token_secret": os.getenv("ACCESS_TOKEN_SECRET"),
    }
