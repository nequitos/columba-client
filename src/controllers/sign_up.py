
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

    async def on_sign_up(self, email: str) -> bool:
        await self.__session.post("/auth/sign_up", json={"email": email})
        return True

    async def verify_code(
        self,
        email: str,
        username: str,
        code: str,
        password: str
    ) -> bool:
        response = await self.__session.post(
            "/auth/verify_code", json={
                "email": email,
                "username": username,
                "code": code,
                "password": password,
                "scope": "me items"
            }
        )

        if response:
            access_token = response["access_token"]
            auth_response = await self.__oauth.authorize_account(token=access_token)

            if auth_response:
                return True
            else:
                return False
        else:
            return False