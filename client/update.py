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
        'Authorization' : f'Token {token}'
    }
    product_id = int(input('Enter product id: '))
    endpoint= f'http://localhost:8000/api/products/{product_id}/update-product/'


    name = input('Enter new prodcut title: ')
    content = input('Enter new prodcut content: ')
    price = float(input('Enter new product price: '))
    data = {
        'title' : name,
        'content' : content,
        'price' : price
    }
    get_response = requests.put(endpoint, json=data, headers=headers)
    print(get_response.json())
