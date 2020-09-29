from app.db import database
from app.api.schemas.note import NoteSchema
from app.api.models.models import notes
from app.api.utils.notes import build_query_form_params


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title,
                                  description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)


async def get_all(
        page: int, page_size: int, title: str, id: list, order_by: list):
    offset = (page - 1) * page_size
    query = build_query_form_params(title, id, order_by)
    query = query.limit(page_size).offset(offset)
    return await database.fetch_all(query=query)


async def put(id: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)
