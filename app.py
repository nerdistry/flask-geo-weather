from flask import Flask, session, render_template, redirect, url_for
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask setup
app = Flask(__name__)
app.secret_key = os.getenv('APPSECRET_KEY')

# OpenWeatherMap API Key
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')


@app.route('/')
def index():
    response = requests.get('http://ip-api.com/json/')

    if response.status_code != 200:
        return 'Could not get location information.'

    location_data = response.json()
    session['location'] = location_data

    lat = location_data.get('lat')
    lon = location_data.get('lon')

#fetching weather data.
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric'
    response = requests.get(weather_url)

    if response.status_code != 200:
        return 'Could not get weather information.'

    weather_data = response.json()
    print(weather_data)  # Print out the data to understand the structure

  #fetching soil data.
    AMBEEDATA_API_KEY=os.getenv('AMBEEDATA_API_KEY')
    soil_url = f'https://api.ambeedata.com/latest/by-lat-lng?lat={lat}&lng={lon}'
    headers = {"x-api-key": AMBEEDATA_API_KEY}
    response = requests.get(soil_url, headers=headers)
    print("Soil API Response: ", response.text)  # Add this line to print the response.

    if response.status_code != 200:
        return 'Could not get soil information.'
    else:
        soil_data = response.json()
        print(soil_data )

    return render_template('display.html', weather_data=weather_data, soil_data=soil_data)

if __name__ == '__main__':
    app.run(debug=True)
