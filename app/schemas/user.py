from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class UserSignup(BaseModel):
    username: str
    email: str
    password: str


class GetUser(BaseModel):
    username: str
