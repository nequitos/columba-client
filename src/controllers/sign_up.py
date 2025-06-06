
from src.models import SignUpModel
from src.session import BaseSession, OAuth2

from src.session.schemes import (
    auth as auth_schemes
)



class SignUpController:
    def __init__(
        self,
        model: SignUpModel,
        session: BaseSession,
        oauth: OAuth2
    ) -> None:
        self.__model = model
        self.__session = session
        self.__oauth = oauth

    async def on_sign_up(self, scheme: auth_schemes.SignUpRequest) -> bool:
        response = await self.__session.post("/auth/sign_up", json=scheme.model_dump())

        print(response)
        if response:
            print("YES")
            self.__model.email = scheme.email
            return True
        else:
            return False

    async def verify_code(self, scheme: auth_schemes.VerifyEmailCodeRequest) -> bool:
        response = await self.__session.post("/auth/sign_up/verify_code", json=scheme.model_dump())

        if response:
            access_token = response["access_token"]
            auth_response = await self.__oauth.authorize_account(token=access_token)

            if auth_response:
                return True
            else:
                return False
        else:
            return False