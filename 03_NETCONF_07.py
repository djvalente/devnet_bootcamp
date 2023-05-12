"""
Configuring OSPF

Tenho de copiar o XML

"""

from ncclient import manager
from xml.dom.minidom import parseString
from getpass import getpass

# Create an SSH Connection on port 830
conn = manager.connect(
    host = "10.255.1.101",
    port = "830",
    username = "admin",
    password = "cisco",
    hostkey_verify = False
)

print ("\n NETCONF Connection OK")

new_config = """
    <config>
        
    </config>
"""

# Send configuration to the device
netconf_reply = conn.edit_config(config = new_config, target = "running")

# Print netconf response
print(netconf_reply)

