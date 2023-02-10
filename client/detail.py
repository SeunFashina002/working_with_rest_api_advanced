import requests
from getpass import getpass

auth_endpoint= 'http://localhost:8000/api/auth/'


username = input('Enter your username:\n')
password = getpass('Enter your password:\n')


auth_response = requests.post(auth_endpoint, json={"username":username, "password":password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization' : f"Token {token}"
    }
    product_id = int(input('Enter product id: '))
    endpoint= f'http://localhost:8000/api/products/{product_id}/'

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
