
from src.models import SignInModel
from src.session import OAuth2
from src.session.schemes import auth as auth_schemes


class SingInController:
    def __init__(
        self,
        model: SignInModel,
        oauth: OAuth2
    ) -> None:
        self.__model = model
        self.__oauth = oauth

    async def on_sign_in(self, scheme: auth_schemes.AuthRequest) -> bool:
        self.__oauth.set_credentials(
            username=scheme.username,
            password=scheme.password,
            scopes=["me", "items"]
        )
        response = await self.__oauth.authorize_account()

        if response:
            return True
        else:
            return False