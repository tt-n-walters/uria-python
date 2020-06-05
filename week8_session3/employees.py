import requests
import json

def get_all_info(company_name):
    url = "https://librebor.me/borme/api/v1/empresa/xxx-xxx-xxx/".replace("xxx-xxx-xxx", company_name)
    response = requests.get(url)
    if response.status_code == 200:
        converted = json.loads(response.text)
        return converted


def search_company(name):
    url = "https://libreborme.net/borme/api/v1/empresa/search/?q=xxx&page=1".replace("xxx", name)
    response = requests.get(url)
    if response.status_code == 200:
        converted = json.loads(response.text)
        return converted

get_all_info("uria-industrial")