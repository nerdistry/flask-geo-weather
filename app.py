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

# Your OpenAI API token
openai_token = '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'

base_url = "https://api.openai.com/v1/"
url = 'https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2'

class DallEImage:
    def get_image_from_dalle(self, prompt, size):
 
        data = {
            "prompt": prompt,
            "size": size,
            # Fill in this line, (prompt)
            # Fill in this line, (size)
            'response_format': 'b64_json',
        }

        # download and transform the image
        response = requests.post(
            base_url + '/images/generations',
            headers={'Authorization': f'Bearer {openai_token}'},
            json=data
        )
        b64_image_data = response.json().get('data', [])[0].get('b64_json', '')

        decoded_image = base64.b64decode(b64_image_data)
        image = Image.open(BytesIO(decoded_image))

        return image  # fill in this line
    
def generate_image(api_key, text):
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {api_key}"}

    data = {"inputs": text}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        # Check if the response contains image data
        if 'image' in response.headers.get('Content-Type', '').lower():
            return response.content
    except Exception as e:
        print("Error occurred:", e)

    return None


# Route for the home page
@app.route('/openai', methods=['GET', 'POST'])
def dalle():
    image_data = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        size = request.form.get('size')
        image = DallEImage().get_image_from_dalle(prompt, size)
        
        # Convert the image to bytes and encode it in base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return render_template('openai.html', image_data=image_data) 


hf_api_key = "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"

@app.route('/huggingface', methods=['GET', 'POST'])
def huggingface():
    image_data = None
    if request.method == 'POST':
        text = request.form.get('text')
        image_bytes = generate_image(hf_api_key, text)

        if image_bytes:
            # Convert the image bytes to base64
            image_data = base64.b64encode(image_bytes).decode('utf-8')

    return render_template('huggingface.html', image_data=Markup(image_data))

if __name__ == '__main__':
    app.run(debug=True)
