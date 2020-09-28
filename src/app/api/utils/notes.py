import json
from typing import List, Optional
from fastapi import Query


def title_dict(title_filters: List[str] = Query(default = list())):
    try:
        return list(map(json.loads, title_filters))
    except ValueError:
        return []


def id_dict(id_filters: Optional[List[str]] = Query(default = list())):
    try:
        return list(map(json.loads, id_filters))
    except ValueError:
        return []


def order_by_dict(order_by_filters: Optional[List[str]] = Query(default = list())):
    try:
        return list(map(json.loads, order_by_filters))
    except ValueError:
        return []
