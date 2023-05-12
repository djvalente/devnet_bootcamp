"""
Using RESTCONF - Configure OSPF Interface
"""

import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
import json

base_url = "https://10.255.1.101/restconf/data/"
resource_url = "Cisco-IOS-XE-native:native/interface/GigabitEthernet"

final_url = base_url + resource_url

headers = {"Content-Type":"application/yang-data+json"}

creds = HTTPBasicAuth(
	username = "admin",
	password = "cisco"
)

ospf_payload = {
	"Cisco-IOS-XE-native:GigabitEthernet": [
        {
            "name":"1",
            "ip": {
                "Cisco-IOS-XE-ospf:ospf": [
                        {
                        "process-id": {
                            "id":"1",
                            "area":"0",
                        },
                        "network":"point-to-point"
                    }
                ]
            }

        }
    ]
}
    


query = requests.patch(url = final_url, auth = creds, headers = headers, data = json.dumps(ospf_payload), verify = False)

print (query.status_code)
print (query.text)
