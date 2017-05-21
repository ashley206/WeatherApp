import pyowm
import twilio
import requests
import json
from twilio.rest import Client

def formatTextMessage(weather):
    textMsg = ('Tomorrow\'s weather will be {status}.'
              ' The high will be {max}F, and the '
              'low will be {min}F.').format(
        status = str(weatherTomorrow.get_status()).lower(),
        max = str(weatherTomorrow.get_temperature('fahrenheit')['max']),
        min = str(weatherTomorrow.get_temperature('fahrenheit')['min']))
    return textMsg

def getCoordinates():
    send_url = 'http://freegeoip.net/json'
    request = requests.get(send_url)
    jsonReq = json.loads(request.text)
    latitude = jsonReq['latitude']
    longitude = jsonReq['longitude']
    return latitude, longitude


# Your API key from OpenWeatherMap
owm = pyowm.OWM('8e50e1405d725c38f555b537712b5e64')  # You MUST provide a valid API key
# Your Account SID from twilio.com/console
account_sid = "ACc265b80a1301c3cf12f22037554eb1b9"
# Your Auth Token from twilio.com/console
auth_token  = "28d3dd73b0de8f68bf031ddc6cdef641"

# Pull information from your current GPS location
latitude, longitude = getCoordinates()

# Search current weather observations in the surroundings of pulled lat/lon
observation_list = owm.weather_around_coords(latitude, longitude)

# Retrieve forecast for tomorrow
forecaster = owm.daily_forecast_at_coords(latitude, longitude);
tomorrow = pyowm.timeutils.tomorrow()
weatherTomorrow = forecaster.get_weather_at(tomorrow)

print formatTextMessage(weatherTomorrow)

## TESTED, and verified! :)

#client = Client(account_sid, auth_token)

#message = client.messages.create(
#    to="+12066011641", 
#    from_="+12062073802",
#    body="Hello from Python! It me.")

#print(message.sid)
