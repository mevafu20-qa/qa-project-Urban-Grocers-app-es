import sender_stand_request
import data

def get_auth_token():
    response = sender_stand_request.post_new_user()
    return response.json()["authToken"]

#CASO 1:

def test_kit_1():
    auth_token = get_auth_token()

    kit_body = {
        "name": "a"
    }

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == "a"

# CASO 2
def test_caracteres_511():
    auth_token = get_auth_token()

    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 201

#CASO 3
def test_vacio():
    auth_token = get_auth_token()

    kit_body = {
        "name": ""
    }

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 400

#CASO 4
def test_caracteres_512():
    auth_token = get_auth_token()

    kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 400

#CASO 5
def test_caracteres_especiales():
    auth_token = get_auth_token()

    kit_body = {
        "name": "№%@"
    }

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 201

#CASO 6
def test_con_espacio():
    auth_token = get_auth_token()

    kit_body = {
        "name": "A Aaa"
    }

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 201

#CASO 7
def test_con_numeros():
    auth_token = get_auth_token()

    kit_body = {
        "name": "123"
    }

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 201

# CASO 8
def test_no_parametro():
    auth_token = get_auth_token()
    kit_body = {}

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 400

# CASO 9
def test_parametro_numero():
    auth_token = get_auth_token()
    kit_body = {"name": 123}

    response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert response.status_code == 400