from typing import List, Optional
from fastapi import APIRouter, HTTPException, Path, Depends

from app.api.cruds import notes

from app.api.schemas.note import NoteDB, NoteSchema

from app.api.utils.notes import title_dict, id_dict, order_by_dict

router = APIRouter()


@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await notes.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.get("/{id}/", response_model=NoteDB)
async def read_note(id: int = Path(..., gt = 0),):
    note = await notes.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/", response_model=List[NoteDB])
async def read_all_notes(
        page: int = 0,
        page_size: int = 10,
        title: Optional[list] = Depends(title_dict),
        id: Optional[list] = Depends(id_dict),
        order_by: Optional[list] = Depends(order_by_dict)):
    return await notes.get_all(page, page_size, title, id, order_by)


@router.put("/{id}/", response_model=NoteDB)
async def update_note(payload: NoteSchema, id: int = Path(..., gt = 0),):
    note = await notes.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note_id = await notes.put(id, payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id: int = Path(..., gt = 0)):
    note = await notes.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    await notes.delete(id)

    return note
