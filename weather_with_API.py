from posixpath import sep
import requests

try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=35.6762&lon=139.6503&appid=2e6957b8cdf4dd84f04bc272e1f79d06")

   # print(response.json())
except:
    print("An error occurred while fetching the weather data.")
    # You can also log the error or handle it in a way that suits your application.

response_json = response.json()

temp = response_json['main']['temp']
temp_min = response_json['main']['temp_min']
temp_max = response_json['main']['temp_max']

#print(f"Current temperature in Tokyo is: {temp}°C")
#print(f"Minimum temperature in Tokyo is: {temp_min}°C")
#print(f"Maximum temperature in Tokyo is: {temp_max}°C")

class City:
    def __init__(self, name, lat, lon, units='metric'):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=2e6957b8cdf4dd84f04bc272e1f79d06")
        except:
            print(f"An error occurred")
  
        
        response_json = response.json()
        self.temp = response_json['main']['temp']
        self.temp_min = response_json['main']['temp_min']
        self.temp_max = response_json['main']['temp_max']

    def temp_print(self):
        units_symbol ="C"
        if self.units == 'imperial':
            units_symbol = "F"
        print(f"Current temperature in {self.name} is: {self.temp}°{units_symbol}")
        print(f"Minimum temperature in {self.name} is: {self.temp_min}°{units_symbol}")
        print(f"Maximum temperature in {self.name} is: {self.temp_max}°{units_symbol}")

my_city = City("Istanbul", 41.0082, 28.9784)
my_city.temp_print()