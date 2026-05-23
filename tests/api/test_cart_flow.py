import requests
from utils.config import BASE_URL, USERNAME, PASSWORD
from jsonschema import validate

# JSON Schema Validation
cart_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "products": {"type": "array"},
        "total": {"type": "number"}
    },
    "required": ["id", "products", "total"]
}


def test_cart_flow():

    # Login Payload
    login_payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "expiresInMins": 30
    }

    # Login Request
    login_response = requests.post(
        f"{BASE_URL}/auth/login",
        json=login_payload
    )

    # Debug Logs
    print("Login Status Code:", login_response.status_code)
    print("Login Response:", login_response.text)

    # Validate Login Status
    assert login_response.status_code == 200

    # Convert Login Response to JSON
    login_data = login_response.json()

    # Extract Token and User ID
    token = login_data["accessToken"]
    user_id = login_data["id"]

    # Authorization Header
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Fetch User Cart
    cart_response = requests.get(
        f"{BASE_URL}/carts/user/{user_id}",
        headers=headers
    )

    print("Cart Status Code:", cart_response.status_code)

    # Validate Cart API
    assert cart_response.status_code == 200

    # Add Product Payload
    add_cart_payload = {
        "userId": user_id,
        "products": [
            {
                "id": 1,
                "quantity": 2
            }
        ]
    }

    # Add Product to Cart
    add_cart_response = requests.post(
        f"{BASE_URL}/carts/add",
        json=add_cart_payload,
        headers=headers
    )

    print("Add Cart Status Code:", add_cart_response.status_code)
    print("Add Cart Response:", add_cart_response.text)

    # Validate Final Status Code
    assert add_cart_response.status_code in [200, 201]

    # Convert Response to JSON
    response_data = add_cart_response.json()

    # Validate Product Added
    assert response_data["products"][0]["id"] == 1
    assert response_data["products"][0]["quantity"] == 2

    # Validate Total Price Calculation
    product = response_data["products"][0]

    expected_total = product["price"] * product["quantity"]

    assert product["total"] == expected_total

    # Validate JSON Schema
    validate(instance=response_data, schema=cart_schema)

    print("Test Passed Successfully")