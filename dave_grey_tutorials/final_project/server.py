from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
from pprint import pprint 


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/weather')
def get_weather():
	city = request.args.get('city')

	# Check for edge cases 
	if not bool(city.strip()):
		city = "Atlanta"

	weather_data = get_current_weather(city)

	# City is not found 
	if not weather_data['cod'] == 200:
		return render_template('city-not-found.html')

	return render_template(
		"weather.html",
		title=weather_data["name"],
		status=weather_data["weather"][0]["description"].capitalize(),
		temp=f"{weather_data['main']['temp']:.1f}",
		feels_like=f"{weather_data['main']['feels_like']:.1f}"
	)

if __name__ == "__main__":
	serve(app, host="0.0.0.0", port=8000)