from app.auth.schemas import UserCredentials


class AuthService:
    async def sign_in(credentials: UserCredentials):
        pass


auth_service = AuthService()
