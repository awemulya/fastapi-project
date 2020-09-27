def test_login_success(test_app):
    mimetype = 'application/x-www-form-urlencoded'
    headers = {
        'Content-Type': mimetype,
        'Accept': "application/json"
    }
    test_request_payload = {
        "username": "johndoe", "password": "password"}

    response = test_app.post("/token", data=test_request_payload,
                             headers=headers)

    assert response.status_code == 200
    assert 'access_token' in response.json()
    assert response.json().get('token_type') == 'bearer'


def test_login_invalid(test_app):
    mimetype = 'application/x-www-form-urlencoded'
    headers = {
        'Content-Type': mimetype,
        'Accept': "application/json"
    }
    test_request_payload = {
        "username": "johndoe", "password": "badpwd"}

    incorrect_response = {
        "detail": "Incorrect username or password"
    }

    response = test_app.post("/token", data=test_request_payload,
                             headers=headers)

    assert response.status_code == 401
    assert response.json() == incorrect_response

