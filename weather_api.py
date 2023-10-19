# weather programm
import json 
from requests import get
def weather(city):
    API_KEY = "2067b3f8738ba4c96867b5672b99a945"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    req = get(url).json()
    dic = {
        'description': req['weather'][0]['description'],
        'temp': req['main']['temp'],
        'humidity': req['main']['humidity'],
        'wind': req['wind']['speed']
    }
    
    return dic
