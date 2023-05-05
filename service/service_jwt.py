from datetime import datetime, timedelta
from typing import Union
from fastapi import Depends, HTTPException
from jose import JWTError, jwt

from config.config import Config


class ServiceJwt:
    def __init__(self, config: Config = Depends()) -> None:
        self.SECRET_KEY = config.JWT_SECRET
        self.ALGORITHM = config.JWT_ALGORITHM
        self.ACCESS_TOKEN_EXPIRE_MINUTES = config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(
        self, data: dict, expires_delta: Union[timedelta, None] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except JWTError as err:
            print(err)
            raise HTTPException(401, "invalid credential")
