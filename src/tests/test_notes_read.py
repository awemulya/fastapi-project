import json

from app.api.cruds import notes


def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"title": "something", "description": "something else", "id": 1},
        {"title": "someone", "description": "someone else", "id": 2},
    ]

    async def mock_get_all(
            page: int, page_size: int, title: list, id: list, asending: bool):
        return test_data

    monkeypatch.setattr(notes, "get_all", mock_get_all)
    params = dict(page=1,
                  per_page=10,
                  title_filters=json.dumps({"title": "aa"}),
                  id_filters=json.dumps({"id": 1}),
                  order_by_filters=json.dumps({"title": "ascending"}),
                  )
    response = test_app.get("/notes/", params=params)
    assert response.status_code == 200
    assert response.json() == test_data
