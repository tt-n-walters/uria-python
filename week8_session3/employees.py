import requests

url = "https://librebor.me/borme/api/v1/empresa/construcciones-uria-alvarez/"
response = requests.get(url)
if response.status_code == 200:
    print(response.text)
