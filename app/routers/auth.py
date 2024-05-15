from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import UserLogin, UserSignup
import random
from app.logger_config import get_logger

# Create an instance of APIRouter
auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: UserLogin):
    auth_logger = get_logger("auth_logger")
    success = random.choice([True, False])

    if not success:
        auth_logger.error("Login failed for user: %s", user.username)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login failed")

    auth_logger.info("User '%s' logged in successfully", user.username)
    return {"username": user.username}


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserSignup):
    logger = get_logger('auth_logger')
    success = random.choice([True, False])

    if not success:
        logger.error("Signup failed for user: %s", user.username)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists")

    logger.info("User '%s' signed up successfully", user.username)
    return {"message": "User signed up successfully", "username": user.username}


@auth_router.post("/getuser/{username}", status_code=status.HTTP_302_FOUND)
async def get_profile(username: str):
    logger = get_logger('auth_logger')
    success = random.choice([True, False])

    if not success:
        logger.error("Failed to get profile for user: %s", username)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    logger.info("Profile retrieved successfully for user: %s", username)
    return {"username": username}
