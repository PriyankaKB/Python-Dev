# http_requests.py
# Examples and explanations for HTTP requests

import requests

response = requests.get('https://httpbin.org/get')
print('GET Response:', response.json())

payload = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=payload)
print('POST Response:', response.json())
