import json
from json.decoder import JSONDecodeError
from typing import List, Optional
from fastapi import Query, HTTPException
from app.api.models.models import notes

from app.api.utils.common import list_to_dict


def title_dict(title_filters: List[str] = Query(default=list())):
    try:
        return list(map(json.loads, title_filters))
    except JSONDecodeError:
        raise HTTPException(
            status_code=404,
            detail='Title dict invalid format; '
                   'example format {key:value}')


def id_dict(id_filters: Optional[List[str]] = Query(default=list())):
    try:
        return list(map(json.loads, id_filters))
    except JSONDecodeError:
        raise HTTPException(
            status_code=404,
            detail='id filter dict invalid format; '
                   'example format {key:value}')


def order_by_dict(order_by_filters: Optional[List[str]] = Query(default=list())):
    try:
        return list(map(json.loads, order_by_filters))
    except JSONDecodeError:
        raise HTTPException(
            status_code=404,
            detail='order by dict invalid format; '
                   'example format {key:value}')


def build_query_form_params(title: str, id: list, order_by: list):
    query = notes.select()
    if title:
        query = query.where(notes.c.title.ilike("%{}%".format(title)))
    if id:
        id_filters_dict = list_to_dict(id)
        if 'in' in id_filters_dict:
            ids = id_filters_dict['in'].split(",")
            ids = [int(id) for id in ids]
            query = query.where(notes.c.id.in_(ids))
        if 'eq' in id_filters_dict:
            id_equal = int(id_filters_dict['eq'])
            query = query.where(notes.c.id == id_equal)
        if 'lte' in id_filters_dict:
            id_lte = int(id_filters_dict['lte'])
            query = query.where(notes.c.id <= id_lte)
        if 'gte' in id_filters_dict:
            id_lte = int(id_filters_dict['gte'])
            query = query.where(notes.c.id >= id_lte)
    if order_by:
        oder_filters_dict = list_to_dict(order_by)
        if 'desc' in oder_filters_dict:
            desc_columns = oder_filters_dict['desc'].split(",")
            for col in desc_columns:
                if 'id' == col:
                    query = query.order_by(notes.c.id.desc())
                elif 'title' == col:
                    query = query.order_by(notes.c.title.desc())
        if 'asc' in oder_filters_dict:
            desc_columns = oder_filters_dict['asc'].split(",")
            for col in desc_columns:
                if 'id' == col:
                    query = query.order_by(notes.c.id)
                elif 'title' == col:
                    query = query.order_by(notes.c.title)
    return query
