import requests
from twilio.rest import Client
from your_data import API_KEY, LAT, LONG, ACCOUNT_SID, AUTH_TOKEN, VIRTUAL_PHONE_NUMBER, YOUR_PHONE_NUMBER


params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_=VIRTUAL_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER)
    print(message.sid)
