
from src.client import BaseSession, OAuth2Session
from src.config import API, URI


session = BaseSession(
    scheme=API.SCHEME.value,
    host=API.HOST.value,
    port=API.PORT.value
)
oath2_session = OAuth2Session(
    session=session,
    token_endpoint_uri=URI.TOKEN_ENDPOINT.value,
)

