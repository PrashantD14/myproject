from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Default Mumbai coordinates
DEFAULT_LAT = 19.0760
DEFAULT_LON = 72.8777

def get_weather(lat, lon):
    url = f"http://www.7timer.info/bin/api.pl?lon={lon}&lat={lat}&product=civil&output=json"
    response = requests.get(url)
    data = response.json()
    return data['dataseries'][:5]  # next 5 time slots

@app.route("/", methods=["GET", "POST"])
def index():
    lat = DEFAULT_LAT
    lon = DEFAULT_LON
    location = "Mumbai"

    if request.method == "POST":
        location = request.form.get("location")

        # Simple mapping (you can extend later)
        if location.lower() == "delhi":
            lat, lon = 28.6139, 77.2090
        elif location.lower() == "bangalore":
            lat, lon = 12.9716, 77.5946
        elif location.lower() == "chennai":
            lat, lon = 13.0827, 80.2707
        else:
            lat, lon = DEFAULT_LAT, DEFAULT_LON

    weather_data = get_weather(lat, lon)

    return render_template("index.html", weather=weather_data, location=location)

if __name__ == "__main__":
    app.run(debug=True)
