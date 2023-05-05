from typing_extensions import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from dto.dto_common import StandardResponse

from dto.dto_user import InputLogin, InputUser, OutputLogin
from service.service_user import ServiceUser

router_user = APIRouter(prefix="/api/v1", tags=["User"])


@router_user.post("/user")
def register_user(input_user: InputUser, service_user: ServiceUser = Depends()):
    service_user.insert_new_user(input_user)
    return StandardResponse(detail="success register user")


@router_user.post("/login", response_model=OutputLogin)
def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    service_user: ServiceUser = Depends(),
):
    jwt_token = service_user.login_user(
        InputLogin(username=form_data.username, password=form_data.password)
    )

    return OutputLogin(access_token=jwt_token)
