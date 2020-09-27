def test_valid_token(test_app):
    mimetype = 'application/x-www-form-urlencoded'
    headers = {
        'Content-Type': mimetype,
        'Accept': "application/json"
    }
    auth_headers = {
        'Authorization': None,
        'Accept': "application/json"
    }
    test_request_payload = {
        "username": "johndoe", "password": "password"}

    response = test_app.post("/token", data=test_request_payload,
                             headers=headers)

    assert response.status_code == 200
    assert 'access_token' in response.json()
    token = response.json().get('access_token')

    auth_headers['Authorization'] = "Bearer {}".format(token)

    response_me = test_app.get("/users/me", headers=auth_headers)
    assert response_me.status_code == 200


def test_token_invalid(test_app):
    headers = dict(Authorization=None, Accept="application/json")

    headers['Authorization'] = "Bearer {}".format("xxxxxxxxxxxxxxx")

    response_me = test_app.get("/users/me", headers=headers)
    assert response_me.status_code == 401

