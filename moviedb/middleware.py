from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    SimpleUser,
    UnauthenticatedUser,
    AuthCredentials,
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
import base64
import binascii
from .movie.models import User
from .movie.utils import verify_password


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "basic":
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decoded.partition(":")
        user = await User.query.where(User.email == username).gino.first()
        if not user or not verify_password(user.password, password):
            raise AuthenticationError("Invalid basic auth credentials")

        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)


middleware = [
    Middleware(AuthenticationMiddleware, options={"backend": BasicAuthBackend()})
]
