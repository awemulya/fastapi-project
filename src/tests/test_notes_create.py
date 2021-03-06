import json

from app.api.cruds import notes


def test_create_note(test_app, monkeypatch):
    test_request_payload = {
        "title": "something", "description": "something else"}
    test_response_payload = {
        "id": 1, "title": "something", "description": "something else"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(notes, "post", mock_post)

    response = test_app.post("/notes/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/notes/", data=json.dumps({"title": "something"}))
    assert response.status_code == 422

    response = test_app.post("/notes/", data=json.dumps(
        {"title": "1", "description": "2"}))
    assert response.status_code == 422
