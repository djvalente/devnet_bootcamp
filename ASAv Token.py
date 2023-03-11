import requests
import json

server = "https://10.255.1.101"
username = "admin"
password = "cisco"

# Fucntion that generates 
def create_token(server, username, password):
    api_path = "/api/tokenservices"    # path para tokens
    headers = {'Content-Type': 'application/json'}

    url = server + api_path
    basicauth = (username, password)

    r = requests.post(url, auth=basicauth, headers=headers, verify=False)
    print (r.status_code)
    return r.headers['X-Auth-Token']

# call the function to create an authentication token
token = create_token(server, username, password)
print (token)
