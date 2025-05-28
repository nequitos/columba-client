
from enum import Enum
from environs import Env


env = Env()
env.read_env()


class API(Enum):
    HOST = env.str("API_HOST")
    PORT = env.int("API_PORT")

