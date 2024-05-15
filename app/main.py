import logging.config
import configparser
from fastapi import FastAPI
from app.routers import auth_router, order_router, product_router, log_router

# Read logging configuration from INI file
config = configparser.ConfigParser()
config.read('./app/logging_config.ini')

# Apply logging configuration
logging.config.fileConfig('./app/logging_config.ini')

# Initialize the FastAPI application
app = FastAPI()

# Include the auth router
app.include_router(auth_router)
app.include_router(order_router)
app.include_router(product_router)
app.include_router(log_router)


# Define a route using a decorator
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!!!"}
