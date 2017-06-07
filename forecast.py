import urllib.request, json 

def measure():
	global temp,hum

	with urllib.request.urlopen("http://api.wunderground.com/api/9a5c856d82019a72/conditions/q/AM/Erebuni.json") as url:
		data = json.loads(url.read().decode())
	data = data.get("current_observation")

	temp = data.get("temp_c")
	hum = data.get("relative_humidity")

#---Forecast---#
def weather_forecast():
	global low, high
	with urllib.request.urlopen("http://api.wunderground.com/api/9a5c856d82019a72/forecast/q/AM/Erebuni.json") as url:
		data = json.loads(url.read().decode())

	data = data.get("forecast").get("simpleforecast").get("forecastday").pop(1)

	low = int(data["low"].get("celsius"))
	high = int(data["high"].get("celsius"))
