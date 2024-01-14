from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class PostBase(
    BaseModel
):  # All the things we require the user to provide during post creation
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):  # what we send as response when user creates account
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(
    PostBase
):  # change the keys here to specify which keys you want to send back to the user as response
    # Post inherit from PostBase the title, content and published
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(PostBase):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


# ----------------------------------------------------------------------------------
# class UserBase(BaseModel): #user must provide this during registration
#     email: EmailStr
#     password: str
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# class UserCreate(UserBase):
#     pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]
    username: str | None = None


# Optional [str]


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
