from ncclient import manager
from xml.dom.minidom import parseString
from xmltodict import parse

# Create an SSH Connection on port 830

conn = manager.connect(
    host = "10.255.1.102",
    port = "830",
    username = "admin",
    password = "cisco",
    hostkey_verify = False
)

print ("\n NETCONF Connection Established")

my_filter = """
<filter>
    <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

    </interfaces>
</filter>
"""

# Get Operational Data using GET
netconf_reply = conn.get(filter= my_filter)

# Beautify the XML print
beauty_xml = parseString(netconf_reply.xml).toprettyxml()
# print(beauty_xml)

int_dict = parse(beauty_xml)['rpc-reply']['data']['interfaces']['interface']

print(int_dict)

for interface in int_dict:
    try:
        description = interface['description']
    except:
        description = "Not Configured"
    
    print(f"Your {interface['name']}'s enabled state is {interface['enabled']} and the description is {description}")