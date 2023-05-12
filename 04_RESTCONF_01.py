"""
Using RESTCONF - Getting Configs
"""

import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

base_url = "https://10.255.1.101/restconf/data/"
resource_url = "Cisco-IOS-XE-native:native/interface/"

# Exemplo mas com ietf (nao native)
# my_url ="https://10.255.1.101:443/restconf/data/ietf-interfaces:interfaces"

final_url = base_url + resource_url

headers = {"Accept":"application/yang-data+json"}

creds = HTTPBasicAuth(
	username = "admin",
	password = "cisco"
)

query = requests.get(url = final_url, auth = creds, headers = headers, verify = False)

# print (query)
# print (dir(query)) # list as chaves
# print (query.headers) # response headers
print (query.status_code) # expected 200
print (query.text) # output

