import requests

API_KEY = "f0f393d64e6262712a1a039cc75038c1"

def get_weather():
    URL = "https://openweathermap.org"

    req_headers = {
        "accept":"application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(url=URL, header=req_headers)
    weather = response.json()

    # 1
    head = ["atributeStyleMap"]
    print(head)