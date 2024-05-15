from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserLogin, UserSignup
import random
from logging.config import fileConfig
import logging
from custom_json_formatter import CustomJsonFormatter

fileConfig('logging_config.ini')


# Ensure handlers use the custom JSON formatter
def update_handlers_with_custom_formatter(logger_name):
    logger = logging.getLogger(logger_name)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.setFormatter(CustomJsonFormatter())


update_handlers_with_custom_formatter('auth_logger')
update_handlers_with_custom_formatter('order_logger')
update_handlers_with_custom_formatter('product_logger')

# Create an instance of APIRouter
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: UserLogin):
    logger = logging.getLogger('auth_logger')
    success = random.choice([True, False])

    if not success:
        logger.error("Login failed for user: %s", user.username)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login failed")

    logger.info("User '%s' logged in successfully", user.username)
    return {"username": user.username}


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserSignup):
    logger = logging.getLogger('auth_logger')
    success = random.choice([True, False])

    if not success:
        logger.error("Signup failed for user: %s", user.username)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

    logger.info("User '%s' signed up successfully", user.username)
    return {"message": "User signed up successfully", "username": user.username}


@auth_router.post("/getuser/{username}", status_code=status.HTTP_302_FOUND)
async def get_profile(username: str):
    logger = logging.getLogger('auth_logger')
    success = random.choice([True, False])

    if not success:
        logger.error("Failed to get profile for user: %s", username)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    logger.info("Profile retrieved successfully for user: %s", username)
    return {"username": username}
