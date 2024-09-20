from pydantic import BaseModel
from pydantic.fields import Field


class UserModel(BaseModel):
    username: str
    email: str = Field(default="email@email.com")
    password: str


class UserPublic(UserModel):
    username: str
    emai: str = Field(default="email@email.com")
