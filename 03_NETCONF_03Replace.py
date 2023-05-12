"""
Change configuration on a IOS_XE router usgin NETCONF
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
        <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet2</name>
                <description>Configured by GOD through NETCONF</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                    ianaift:ethernetCsmacd
                </type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip" operation = 'replace'>
                    <address>
                            <ip>10.255.3.1</ip>
                            <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>
"""

# Send configuration to the device
netconf_reply = conn.edit_config(config = new_config, target = "running")

# Print netconf response
print(netconf_reply)

