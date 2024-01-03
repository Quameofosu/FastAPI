from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class PostBase(BaseModel): # All the things we require the user to provide during post creation
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase): #change the keys here to specify which keys you want to send back to the user as response
    # Post inherit from PostBase the title, content and published
    id: int
    created_at: datetime
    

    class Config:
        orm_mode = True
#----------------------------------------------------------------------------------
# class UserBase(BaseModel): #user must provide this during registration
#     email: EmailStr
#     password: str
class UserCreate(BaseModel):
     email: EmailStr
     password: str
# class UserCreate(UserBase):
#     pass
class UserOut(BaseModel): #what we send as response when user creates account
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional [str]
    username: str | None = None

# Optional [str]