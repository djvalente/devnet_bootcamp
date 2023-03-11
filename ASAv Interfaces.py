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
    
    if (r.status_code == 200):
        return r.content
    else:
        print ("ERROS Calling the API with code: " + str(r.status_code))

# call the function to get all physical interfaces
int_list = get_interfaces_physical(server, username, password)

if (int_list): # Only prints if the response as content
    obj = json.loads(int_list)
    print (json.dumps(obj,indent=4))  # Using loads/dumps just to print python indented

