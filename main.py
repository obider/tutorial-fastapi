from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from router.router_transaction import router_transaction
from router.router_user import router_user

application = FastAPI()


@application.exception_handler(HTTPException)
def standard_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "message": exc.detail},
    )


application.include_router(router_transaction)
application.include_router(router_user)
