from fastapi.testclient import TestClient
from rpn.main import app

client = TestClient(app)

def test_add_element():
    response = client.post("/stack", json={"value": 5})
    assert response.status_code == 200
    assert response.json() == {"status": "added"}

def test_get_stack():
    # Add an element first
    client.post("/stack", json={"value": 10})
    response = client.get("/stack")
    assert response.status_code == 200
    assert response.json() == [{"value": 5}, {"value": 10}]

def test_clear_stack():
    response = client.delete("/stack")
    assert response.status_code == 200
    assert response.json() == {"status": "cleared"}

def test_apply_operation_addition():
    # Add two elements
    client.post("/stack", json={"value": 3})
    client.post("/stack", json={"value": 7})
    # Perform addition
    response = client.post('/stack/op?operation=%2b')
    assert response.status_code == 200
    assert response.json() == {"result": {"value": 10}, "status": "success"}

def test_apply_operation_subtraction():
    # Add two elements
    client.post("/stack", json={"value": 10})
    client.post("/stack", json={"value": 4})
    # Perform subtraction
    response = client.post("/stack/op?operation=-")
    assert response.status_code == 200
    assert response.json() == {"result": {"value": 6}, "status": "success"}

def test_apply_operation_division_by_zero():
    # Add two elements
    client.post("/stack", json={"value": 8})
    client.post("/stack", json={"value": 0})
    # Perform division
    response = client.post("/stack/op?operation=/")
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero"}

def test_apply_operation_not_enough_operands():
    # Empty stack
    client.delete("/stack")
    # Add one element
    client.post("/stack", json={"value": 5})
    # Perform addition
    response = client.post("/stack/op?operation=%2b")
    assert response.status_code == 400
    assert response.json() == {"detail": "Not enough operands"}