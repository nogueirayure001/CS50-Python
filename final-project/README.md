# FLASK WEATHER API

#### Video Demo: https://www.youtube.com/watch?v=SO3kpv3WisM

#### Description:

This API serves information about a specified location and in a specified language, defaulting to english. It uses a web scraper to search for the weather information based on the parameters entered by the client. The web scraper will search and retrieve the information from the web and give it back to the client in object format.
Firstly, it needs the chromedriver installed in the system for selenium to work. It will simulate a web browser, render the page and javascript on the page and return the document.
Then, the document will be used by beautiful soup to scrape the page and find the needed information based on certain structure on the page.
The .env file includes all environment variables needed for the app to work, including the base url to scrape from and the chromedriver path.
requirements.txt has all the packages used in the project that will hava to be install beforehand.
test_page is an html page that will be used in the unit tests
test_project contain the testing of the project functions.

#### Routes

```yml
    GET /
    - Route to get weather data from location
    - Query parameters:
        - location: any location by name (required)
        - lang: ISO 639-1 language codes (optional), defaults to 'EN'
    - Response example:
        {
            "message": "success",
            "data": {
                "celsius": "26",
                "fahrenheit": "78",
                "humidity": "86%",
                "location": "Aracati, CE",
                "rain": "3%",
                "speed_km": "14 km/h",
                "speed_mi": "9 mph",
                "weather_type": "Partially cloudy"
            }
        }
```

---

#### How it works.

##### Pre-requisites

Before you begin, you will need to have [Python](https://www.python.org/) and ChromeDriver installed on your machine.

##### Running the server

```bash

# Clone this repository
$ git clone https://github.com/nogueirayure001/flask-weather-api.git

# Access the project folder in your terminal
$ cd flask-weather-api

# Make a virtual enviroment
$ python3 -m venv venv

# Activate the virtual enviroment
$ . venv/bin/activate

# Install the dependencies
$ pip install -r requirements.txt

# Set enviroment variables
# In .env file set DRIVER_PATH to the chromedriver location in your system

# Run the application in development mode
$ flask run

# The application will open on the port: 5000 - go to http://localhost:5000

```

---
