import requests as req
import time
from dotenv import load_dotenv
import os


# #Get api key.
def fetch_api_key():
    load_dotenv()


#Get some data from open weather
class Weather:
    def __init__(self, city_name, country_code='US', limit=5):   
        self.city_name = city_name
        self.country_code = country_code
        self.limit = limit
        self.temperature_unit = 'imperial'
        self.api_key = None 
        self.geo_data = {
            'lat': '',
            'lon': ''
        }

        #Get user api key. If empty string use api_key in .env file.
        get_api_key = input('Enter your api key: ').strip()
     
        if get_api_key != '':
            self.api_key = get_api_key

        
        #Get Coordinates
        geo_coords = self.convert_to_coordinates(city_name, country_code, get_api_key)
        

        #Error Handling
        if len(geo_coords) == 0: 
            raise("Could not find the weather for the location specified. Please verify the city and country.")
            quit()

        try:
            self.geo_data = {
                'lat': geo_coords[0]['lat'],
                'lon': geo_coords[0]['lon'],
            }
        except:
            print(f'Status Code {geo_coords["cod"]}, {geo_coords["message"]}')
            
            #Use api key in .env file if availale
            use_env_file = input('The api_key you entered is invalid. Would you like to use whats in the default key? (YES/NO)').strip().upper()

            if use_env_file == 'YES':
                self.api_key = os.getenv('api_key')   

                try:
                    geo_data = self.convert_to_coordinates(city_name, country_code, self.api_key )
                    self.geo_data = {
                        'lat': geo_data[0]['lat'],
                        'lon': geo_data[0]['lon'],
                    }
                except:
                    print(f'Status Code {geo_coords["cod"]}, {geo_coords["message"]} - Please verify default api key.')
                    quit()

            else:
                quit()


    
    def convert_to_coordinates(self, city_name, country_code, api_key):    
        #Convert City Names and Countries to Geographical coordinates
        open_weather_geocoding_api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={self.city_name},{self.country_code}&limit={self.limit}&appid={self.api_key}'
        res = req.get(f'{open_weather_geocoding_api_url}').json()
        return res
    


    def get_current_weather(self):
        lat = self.geo_data["lat"]
        lon = self.geo_data["lon"]

        #Fetch Current Weather
        try:
            degrees = '\N{DEGREE SIGN}'
            open_weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}&units={self.temperature_unit}'
            res = req.get(f'{open_weather_url}')

            print('Generating your weather report...\n')
            time.sleep(3)
            current_weather = res.json()

            print(f'Current temperature in {self.city_name.upper()}, {self.country_code.upper()}: {current_weather["main"]["temp"]}{degrees}F')
            time.sleep(.5)
            print(f'Feels like {current_weather["main"]["feels_like"]}{degrees}F')
            time.sleep(.5)
            print(f'Lowest temp for today: {current_weather["main"]["temp_min"]}{degrees}F')
            time.sleep(.5)
            print(f'Highest temp for today: {current_weather["main"]["temp_max"]}{degrees}F')
            time.sleep(.5)
            print(f'Humidity is: {current_weather["main"]["humidity"]}')
            time.sleep(.5)
            print(f'Wind speed is: {current_weather["wind"]["speed"]} miles per hour.')

        except ValueError:
            print(f'Something went wrong.')


if __name__ == "__main__":
    fetch_api_key()
    toronto = Weather('toronto','ca') #ENTER YOUR CITY AND COUNTRY ABREVIATION .
    toronto.get_current_weather()

