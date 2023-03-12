import requests
import json
from getpass import getpass

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
    api_path = "/api/interfaces/physical/GigabitEthernet0_API_SLASH_2"
    headers = {'Content-Type': 'application/json'}

    url = server + api_path
    basicauth = (username, password)

    int_name = input("Enter your interface name: ")
    int_desc = input("Enter your interface description: ")
    int_zone =input("Enter your interface zone name: ")
    int_sec = int(input("Enter your interface security level: "))
    int_ip = input("Enter your interface IP Address: ")
    int_mask = input("Enter your interface Subnet Mask: ")

    asa_payload = {
        "securityLevel": int_sec,
        "kind": "object#GigabitInterface",
        "channelGroupMode": "active",
        "flowcontrolLow": -1,
        "name": int_zone,
        "duplex": "auto",
        "forwardTrafficSFR": False,
        "hardwareID": int_name,
        "mtu": 1500,
        "lacpPriority": -1,
        "flowcontrolHigh": -1,
        "ipAddress": {
            "ip": {
            "kind": "IPv4Address",
            "value": int_ip
            },
            "kind": "StaticIP",
            "netMask": {
            "kind": "IPv4NetMask",
            "value": int_mask
            }
        },
        "flowcontrolOn": False,
        "shutdown": False,
        "interfaceDesc": int_desc,
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

server = "https://10.255.1.101"

#### call the function to get all physical interfaces ####
# username = "admin"
# password = "cisco"
# get_interfaces_physical(server, username, password)

#### call the function to configure g0/1 ####

print("\nWelcome to ASA Automation Script\n")
username = input("What is your username: ")
password = getpass("Please input your password")

if username == "admin" and password == "cisco":
    configure_interface_physical(server, username, password)
else:
    print("\n\nAuthentication Failed\n")
