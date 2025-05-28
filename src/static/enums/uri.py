
from enum import StrEnum


class Post(StrEnum):
    INDEX = "/"
    SIGN_UP_URI = "/auth/sign_up"
    SIGN_IN_URI = "/oauth/token"