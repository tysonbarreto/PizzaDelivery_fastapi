from fastapi import FastAPI
from src.pd.auth_routes import auth_router
from src.pd.order_routes import order_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)