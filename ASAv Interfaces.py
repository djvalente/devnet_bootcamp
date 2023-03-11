import requests
import json

server = "https://10.255.1.101"
username = "admin"
password = "cisco"

# GET physical Interfaces
def get_interfaces_physical(server, username, password):
    api_path = "/api/interfaces/physical"
    headers = {'Accept': 'application/json'}

    url = server + api_path
    basicauth = (username, password)

    r = requests.get(url, auth=basicauth, headers=headers, verify=False)
    print (r.status_code)
    return r.content

# call the function to create an authentication token
int_list = get_interfaces_physical(server, username, password)
print (int_list)
