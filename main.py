import requests
import geocoder

def send_location_to_webhook():
    webhook_url = 'https://webhook.site/c1102c25-1570-48f6-90c2-095d83eea189'
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    data = {
        'latitude': latitude,
        'longitude': longitude
    }
    response = requests.post(webhook_url, json=data)
    print(response.text)

send_location_to_webhook()
