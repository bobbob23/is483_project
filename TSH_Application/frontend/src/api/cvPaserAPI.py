import requests

url = 'https://cvparser.ai/api/v3/parse'
headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'af37b7ad9f00a6ef21555c35965e252f'
}
data = {
    'url': 'https://example.com/your_cv_file.pdf'
}

response = requests.post(url, headers=headers, json=data)
print(response.json())