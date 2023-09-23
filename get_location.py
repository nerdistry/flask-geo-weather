import requests

@app.route('/get_location')
def get_location():
    response = requests.get('http://ip-api.com/json/')
    location_data = response.json()

    if response.status_code == 200:
        session['location'] = location_data
        return redirect(url_for('show_weather'))
    else:
        return 'Could not get location information.'
from dotenv import load_dotenv
import os

load_dotenv()

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
