import requests

# endpoint = 'https://httpbin.org/anything'

endpoint= ' http://127.0.0.1:8000/api/'

get_response = requests.post(endpoint, params={'id': 123} ,json={'title':'hello world'})
print(get_response.json())



# print(get_response.status_code)
# print(get_response.text)

"""
HTTP Requests -> HTML
REST API REQUEST -> JSON()
"""
