from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import post, user, auth, vote
from . import models
from .database import engine
from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Social Media API",
    summary="A sample backend API.",
)

# use origins = ["*"] to make all websites able to talk to the api
origins = [
    "http://www.manuelofosu.site",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # []
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
