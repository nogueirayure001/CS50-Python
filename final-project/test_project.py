from bs4 import BeautifulSoup
from project import get_current_temp, get_conditions, get_weather_type_and_location


with open("test_page.html") as html_file:
    page = html_file.read()

soup = BeautifulSoup(page, "html.parser")
main_container = soup.find("div", id="wob_wc")

def test_get_current_temp():
    assert get_current_temp(main_container) == {
        "celsius":"27",
        "fahrenheit":"81"
    }


def test_get_conditions():
    assert get_conditions(main_container) == {
        "rain": "2%", 
        "humidity": "80%",
        "speed_km": "21 km/h",
        "speed_mi": "13 mph"
    }


def test_get_weather_type_and_location():
    assert get_weather_type_and_location(main_container) == {
        "location": "Aracati, State of Ceará",
        "weather_type": "Clear"
    }
