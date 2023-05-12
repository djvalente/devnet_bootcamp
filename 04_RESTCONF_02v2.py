"""
Using RESTCONF - Configure physical interface
"""

import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
import json

base_url = "https://10.255.1.101/restconf/data/"

# Interfaces fisicos
resource_url = "Cisco-IOS-XE-native:native/interface/GigabitEthernet"

final_url = base_url + resource_url

headers = {"Content-Type":"application/yang-data+json"}

creds = HTTPBasicAuth(
	username = "admin",
	password = "cisco"
)

interface_payload = {
	"Cisco-IOS-XE-native:GigabitEthernet": [
        {
            "name":"3",
            "ip": {
                "address": {
                    "primary": {
                        "address": "10.1.1.1",
                        "mask":"255.255.255.0"
                    }
                }
            }
        }
    ]
}    

query = requests.patch(url = final_url, auth = creds, headers = headers, data = json.dumps(interface_payload), verify = False)

print (query.status_code)
print (query.text)
