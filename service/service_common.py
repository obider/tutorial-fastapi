from typing_extensions import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from service import service_jwt
from dto.dto_common import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    service_jwt: service_jwt.ServiceJwt = Depends(),
):
    print(token)
    return TokenData.parse_obj(service_jwt.decode_token(token))
