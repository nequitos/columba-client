
from src.client import *
from src.config import API, URI


# --- session initialize --- #
oath2 = OAuth2(
    scheme=API.SCHEME.value,
    host=API.HOST.value,
    port=API.PORT.value,
    token_endpoint_uri=URI.TOKEN_ENDPOINT.value,
    scopes=["me", "items"]
)
base_session = BaseSession(
    scheme=API.SCHEME.value,
    host=API.HOST.value,
    port=API.PORT.value,
    auth=oath2
)

session = Session(session=base_session)
