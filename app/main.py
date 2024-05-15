import logging.config
import configparser
from fastapi import FastAPI
from app.routers import auth_router, order_router, product_router, log_router
from fastapi.openapi.docs import get_swagger_ui_html

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

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="FastAPI Swagger UI")

# Define a route using a decorator
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
