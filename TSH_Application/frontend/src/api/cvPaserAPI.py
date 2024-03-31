import requests

url = 'https://cvparser.ai/api/v3/parse'
headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'af37b7ad9f00a6ef21555c35965e252f'
}
data = {
    'url': 'https://candidate-uploaded-files.s3.amazonaws.com/resume/deborahhow_resume.docx?AWSAccessKeyId=AKIA226XEIT37IAV5OPR&Signature=uipdr%2FsDKZo0SacVbRTz4RgkSZY%3D&Expires=1711800575'
}

response = requests.post(url, headers=headers, json=data)
print(response.json())