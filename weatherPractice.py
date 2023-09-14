#Jason Shamayev
#Weather App
global appid
#appid = "57a441a265f898f61d53a1e7152c9ca2"
import requests
import config

def getCoords():
    city = input("Enter City: ")
    state = input("Enter State: ")
    #country = input("Enter Country: ")
    base_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state}&limit=1&appid={config.appid}"
    response = requests.get(base_url)
    data = response.json()
    latitude = data[0]["lat"]
    longitude = data[0]["lon"]
    return latitude,longitude

def getWeather(lat,lon):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.appid}&units=imperial"
    response = requests.get(base_url)
    data = response.json()
    temp = data['main']['temp']
    return (temp)
    

def main():
    lat,lon = getCoords()
    temp = getWeather(lat, lon)
    print("Temperature:", temp)


if __name__ == "__main__":
    main()
