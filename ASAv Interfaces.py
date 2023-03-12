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
        obj = json.loads(r.content)
        print (json.dumps(obj,indent=4))  # Using loads/dumps just to print python indented
    else:
        print ("ERROR Calling the API with code: " + str(r.status_code))
    

def configure_interface_physical(server, username, password):
    api_path = "/api/interfaces/physical/GigabitEthernet0_API_SLASH_1"
    headers = {'Content-Type': 'application/json'}

    url = server + api_path
    basicauth = (username, password)

    asa_payload = {
        "securityLevel": 100,
        "kind": "object#GigabitInterface",
        "channelGroupMode": "active",
        "flowcontrolLow": -1,
        "name": "DMZ",
        "duplex": "auto",
        "forwardTrafficSFR": False,
        "hardwareID": "GigabitEthernet0/1",
        "mtu": 1500,
        "lacpPriority": -1,
        "flowcontrolHigh": -1,
        "ipAddress": {
            "ip": {
            "kind": "IPv4Address",
            "value": "192.168.1.1"
            },
            "kind": "StaticIP",
            "netMask": {
            "kind": "IPv4NetMask",
            "value": "255.255.255.0"
            }
        },
        "flowcontrolOn": False,
        "shutdown": False,
        "interfaceDesc": "DMZ ZONE (Configured by Python)",
        "managementOnly": False,
        "channelGroupID": "",
        "speed": "auto",
        "forwardTrafficCX": False,
        "flowcontrolPeriod": -1
    }

    r = requests.put(url, auth=basicauth, headers=headers, verify=False, data=json.dumps(asa_payload))

    if r.status_code == 204:
        print("Your interface as been configured successfully...")
    else:
        print("Your interface was not configure\nSee below error message for details")
        print("Status code: " + str(r.status_code))
        print(r.content)


#### call the function to get all physical interfaces ####
# get_interfaces_physical(server, username, password)

#### call the function to configure g0/1 ####
configure_interface_physical(server, username, password)

