"""
Using RESTCONF - Configure OSPF Process + ID
"""

import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
import json

base_url = "https://10.255.1.101/restconf/data/"
resource_url = "Cisco-IOS-XE-native:native/router"

final_url = base_url + resource_url

headers = {"Content-Type":"application/yang-data+json"}

creds = HTTPBasicAuth(
	username = "admin",
	password = "cisco"
)

ospf_payload = {
	"Cisco-IOS-XE-ospf:ospf": {
        "id":"1",
        "router-id": "1.1.1.1"
    }
}
    


query = requests.post(url = final_url, auth = creds, headers = headers, data = json.dumps(ospf_payload), verify = False)

print (query.status_code)
print (query.text)
