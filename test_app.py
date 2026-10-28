from app import app

def test_addition():
    client = app.test_client()
    response = client.post("/", data={
        "a": "10",
        "b": "5",
        "operation": "add"
    })
    assert b"15.0" in response.data

def test_subtraction():
    client = app.test_client()
    response = client.post("/", data={
        "a": "10",
        "b": "5",
        "operation": "subtract"
    })
    assert b"5.0" in response.data