"""
Using RESTCONF - Configure OSPF FULL
"""

import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth
import json

base_url = "https://10.255.1.102/restconf/data/"
interface_url = "Cisco-IOS-XE-native:native/interface/GigabitEthernet"
ospf_url = "Cisco-IOS-XE-native:native/router"

headers = {"Content-Type":"application/yang-data+json"}

creds = HTTPBasicAuth(
	username = "admin",
	password = "cisco"
)

def post_ospf():
    ospf_process_url = base_url + ospf_url

    ospf_process_payload = {
        "Cisco-IOS-XE-ospf:ospf": {
            "id":"1",
            "router-id": "2.2.2.2"
        }
    }
    query = requests.post(url = ospf_process_url, auth = creds, headers = headers, data = json.dumps(ospf_process_payload), verify = False)

    print ("OSPF Reply Code: " + str(query.status_code))

def patch_ospf():
    ospf_interface_url = base_url + interface_url

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
    
    print ("OSPF Interface Reply code: " + str(query.text))

post_ospf()
patch_ospf()



final_url = base_url + resource_url



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
