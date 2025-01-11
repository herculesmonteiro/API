from behave import given, when, then
import requests
import random
import allure

BASE_URL = "https://demoqa.com"

@given('I create a new user')
def step_create_user(context):
    url = f"{BASE_URL}/Account/v1/User"
    payload = {
        "userName": f"testuser_{random.randint(1000, 9999)}",
        "password": "P@ssw0rd123!"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    context.user_id = response.json()['userID']
    context.username = payload['userName']
    context.password = payload['password']
    
    allure.attach(f"User created: {context.username}", name="Created User", attachment_type=allure.attachment_type.TEXT)

@when('I generate a token for the user')
def step_generate_token(context):
    url = f"{BASE_URL}/Account/v1/GenerateToken"
    payload = {
        "userName": context.username,
        "password": context.password
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    context.token = response.json()['token']
    
    allure.attach(f"Token generated: {context.token}", name="Generated Token", attachment_type=allure.attachment_type.TEXT)

@then('I confirm the user is authorized')
def step_confirm_authorization(context):
    url = f"{BASE_URL}/Account/v1/Authorized"
    payload = {
        "userName": context.username,
        "password": context.password
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json() == True
    
    allure.attach("User is authorized", name="Authorization Status", attachment_type=allure.attachment_type.TEXT)

@then('I list available books')
def step_list_books(context):
    url = f"{BASE_URL}/BookStore/v1/Books"
    headers = {"Authorization": f"Bearer {context.token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    context.books = response.json()['books']
    
    allure.attach(f"Available books: {len(context.books)}", name="Book List", attachment_type=allure.attachment_type.TEXT)

@then('I rent two random books')
def step_rent_books(context):
    url = f"{BASE_URL}/BookStore/v1/Books"
    headers = {
        "Authorization": f"Bearer {context.token}",
        "Content-Type": "application/json"
    }
    context.rented_books = random.sample(context.books, 2)
    payload = {
        "userId": context.user_id,
        "collectionOfIsbns": [{"isbn": book['isbn']} for book in context.rented_books]
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 201
    
    allure.attach(f"Rented books: {[book['title'] for book in context.rented_books]}", name="Rented Books", attachment_type=allure.attachment_type.TEXT)

@then('I verify the user details with rented books')
def step_verify_user_details(context):
    url = f"{BASE_URL}/Account/v1/User/{context.user_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    user_books = response.json()['books']
    assert len(user_books) == 2
    for book in user_books:
        assert any(rented_book['isbn'] == book['isbn'] for rented_book in context.rented_books)
    
    allure.attach(f"User details: {response.json()}", name="User Details", attachment_type=allure.attachment_type.JSON)
