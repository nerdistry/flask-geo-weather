# flask-geo-weather

This document provides the necessary steps to set up the project.

## Getting Started

Follow the instructions below to set up the development environment on your local machine.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python
- pip (Python’s package installer)

### Steps

1. **Clone the Repository**

   ```sh
   git https://github.com/nerdistry/flask-geo-weather.git
   ```

2. **Get OpenWeatherMap API Key**

   This project uses the OpenWeatherMap API to get weather data, so you will need an API key. Register and get your free API key [here](https://openweathermap.org/api).

3. **Setup .env File**

   After obtaining your API key, create a `.env` file in your project directory and add the following line, replacing `OPENWEATHER_API_KEY` with your actual key and inputting your `APPSECRET_KEY`:

   ```sh
   OPENWEATHER_API_KEY=YOUR_API_KEY
   APPSECRET_KEY =YOUR_APP_SECRET_KEY
   ```

4. **Setup Virtual Environment**

   ```sh
   python -m venv venv
   ```

5. **Activate Virtual Environment**

   - **On Windows:**

     ```sh
     .\venv\Scripts\activate
     ```

   - **On Unix or MacOS:**

     ```sh
     source venv/bin/activate
     ```

6. **Install Required Packages**

   After activating the virtual environment, run the following command to install the necessary packages:

   ```sh
   pip install Flask requests python-dotenv blinker charset_normalizer
   ```

## Notes

- The `.gitignore` file in this project already excludes `.env`, `venv/`, `.idea/`, and `__pycache__/`, so you don’t have to worry about accidentally pushing sensitive information or unnecessary files to version control.
- If 'pip' is not recognized as a command, ensure that Python and pip are correctly installed, and that your Python Scripts directory is in your system's PATH.

## Running the Application

Navigate to the project directory and run the application with the following command:

```sh
flask run
```

Visit `http://127.0.0.1:5000/` in your web browser to view the application.
