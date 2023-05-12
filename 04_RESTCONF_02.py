"""
Using RESTCONF - Creating/Updating/Deleting Loopback
"""

import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
import json

base_url = "https://10.255.1.101/restconf/data/"

# resource_url = "Cisco-IOS-XE-native:native/interface/" # Para criar é sem Loopback e com POST
# resource_url = "Cisco-IOS-XE-native:native/interface/Loopback=" # Para atualizar é com PATCH e com o Loopback no uri
resource_url = "Cisco-IOS-XE-native:native/interface/Loopback=20" # Para apagar é com DELETE e com o Loopback=Nr/Nome no uri


final_url = base_url + resource_url

headers = {"Content-Type":"application/yang-data+json"}

creds = HTTPBasicAuth(
	username = "admin",
	password = "cisco"
)

interface_payload = {
	"Cisco-IOS-XE-native:Loopback":
    {
        "name": "101",
        "description": "Configured by GOD using RESTCONF",
        "ip": {
            "address": {
                "primary": {
                    "address": "10.255.3.1",
                    "mask":"255.255.255.0"
                }
            }
        }
    }
}

query = requests.delete(url = final_url, auth = creds, headers = headers, data = json.dumps(interface_payload), verify = False)

print (query.status_code)
print (query.text)
