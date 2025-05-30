
from enum import Enum
from environs import Env


env = Env()
env.read_env()


class API(Enum):
    HOST = env.str("API_HOST")
    PORT = env.int("API_PORT")
    SCHEME = env.str("API_SCHEME")


class URI(Enum):
    TOKEN_ENDPOINT = env.str("TOKEN_ENDPOINT_URI")
    ACCOUNT_CREATE_URI = env.str("ACCOUNT_CREATE_URI")

