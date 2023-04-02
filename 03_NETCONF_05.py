"""
Configure CSR using Native YANG models
"""

from ncclient import manager
from xml.dom.minidom import parseString
from getpass import getpass

# Create an SSH Connection on port 830
conn = manager.connect(
    host = "10.255.1.102",
    port = "830",
    username = "admin",
    password = "cisco",
    hostkey_verify = False
)

print ("\n NETCONF Connection Established")

interface_payload = """
    <config>
        <native xmlns = "http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <GigabitEthernet>
                    <name>3</name>
                    <description>Configuring Using Native Data Model</description>
                    <ip>
                        <address>
                            <primary>
                                <address>8.8.8.8</address>
                                <mask>255.255.255.0</mask>
                            </primary>
                        </address>
                    </ip>
                </GigabitEthernet>
            </interface>        
        </native>
    </config>
"""

# Set Config 
netconf_reply = conn.edit_config(config = interface_payload, target = "running")

print(netconf_reply)

