import requests
url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
try:
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        print(data['explanation'])
        print(data['url'])
    else: print("Ошибка")
except Exception as e:
    print(f"Произошла ошибка: {e}")