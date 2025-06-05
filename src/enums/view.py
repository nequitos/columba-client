
from enum import StrEnum


class Route(StrEnum):
    INDEX = "/"
    SIGN_IN = "/auth/sign_in"
    SIGN_UP = "/auth/sign_up"
    EMAIL_CODE = "/auth/sign_up/code"
    HOME = "/account"
