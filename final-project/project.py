from dotenv import load_dotenv
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
import os

load_dotenv()

BASE_URL = os.environ["BASE_URL"]
DRIVER_PATH = os.environ["DRIVER_PATH"]

driver = webdriver.Chrome(DRIVER_PATH)
app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False


@app.get("/")
def index():
    location = request.args.get("location")
    lang = request.args.get("lang")

    if not location:
        return jsonify({"message": "invalid location"}), 400

    if not lang:
        data = scrape(location)
    else:
        data = scrape(location, lang)

    if not data:
        return jsonify({"message": "No results for the params submitted"}), 404

    return jsonify({"message": "success", "data": data}), 200


def scrape(location, lang_code="en"):
    url = create_url(location, lang_code)
    driver.get(url)
    page = driver.page_source.encode("utf8")

    soup = BeautifulSoup(page, "html.parser")
    main_container = soup.find("div", id="wob_wc")
    if not main_container:
        return None

    return {
        **get_current_temp(main_container),
        **get_conditions(main_container),
        **get_weather_type_and_location(main_container),
    }


def create_url(location, lang_code):
    return f"{BASE_URL}?q=weather+{location}&hl={lang_code}"


def get_current_temp(container):
    celsius = container.find("span", id="wob_tm")
    fahrenheit = container.find("span", id="wob_ttm")

    return {"celsius": celsius.text.strip(), "fahrenheit": fahrenheit.text.strip()}


def get_conditions(container):
    rain = container.find("span", id="wob_pp")
    humidity = container.find("span", id="wob_hm")
    speed_km = container.find("span", id="wob_ws")
    speed_mi = container.find("span", id="wob_tws")

    return {
        "rain": rain.text.strip(),
        "humidity": humidity.text.strip(),
        "speed_km": speed_km.text.strip(),
        "speed_mi": speed_mi.text.strip(),
    }


def get_weather_type_and_location(container):
    location = container.find("div", id="wob_loc")
    weather_type = container.find("span", id="wob_dc")

    return {
        "location": location.text.strip(),
        "weather_type": weather_type.text.strip(),
    }
