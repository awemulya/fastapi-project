from functools import lru_cache

from fastapi import FastAPI

from app.db import engine, database
from app.api.models.models import metadata
from app.api.routes import root
from app.api.routes import notes
from app.api.routes import auth

from app import config

metadata.create_all(engine)


app = FastAPI()


@lru_cache()
def get_settings():
    return config.Settings()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(auth.router)
app.include_router(root.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
