from fastapi import FastAPI
from router.router_transaction import router_transaction
from router.router_user import router_user

application = FastAPI()

application.include_router(router_transaction)
application.include_router(router_user)
