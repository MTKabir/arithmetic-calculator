from fastapi.testclient import TestClient
from arithmetic_calculator.main import app

client = TestClient(app)


def test_addition():
    response = client.post(
        "/api/calculator/addition",
        json={"first_number": 2, "second_number": 3}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_subtraction():
    response = client.post(
        "/api/calculator/subtraction",
        json={"first_number": 5, "second_number": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_multiplication():
    response = client.post(
        "/api/calculator/multiplication",
        json={"first_number": 4, "second_number": 3}
    )

    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_division():
    response = client.post(
        "/api/calculator/division",
        json={"first_number": 10, "second_number": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_history():
    response = client.get("/api/calculator/history")
    assert response.status_code == 200
    assert "history" in response.json()
    assert isinstance(response.json()["history"], list)
