from fastapi import FastAPI

from app.db import engine, database

from app.api.models.models import metadata

from app.api.routes import root
from app.api.routes import notes

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(root.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
