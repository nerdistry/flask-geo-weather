@app.route('/show_weather')
def show_weather():
    location_data = session.get('location')
    if not location_data:
        return 'Could not get location information.'

    lat = location_data['lat']
    lon = location_data['lon']

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}'
    response = requests.get(weather_url)
    weather_data = response.json()

    if response.status_code == 200:
        return render_template('weather.html', weather_data=weather_data)
    else:
        return 'Could not get weather information.'
