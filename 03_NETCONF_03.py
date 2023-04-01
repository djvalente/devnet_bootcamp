"""
Change configuration on a IOS_XE router usgin NETCONF
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

print ("\n NETCONF Connection OK")

new_config = """
    <config>
        <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet2</name>
                <description>Configured by DV through NETCONF</description>
                <type xmlns:ianaift="urn:ietf:param:xml:ns:yang:iana-if-type>
                    ianaift:ethernetCsmacd
                </type>
                <enabled>true</enabled>
                <ipv4>

                
                </ipv4>
            </interface>
        </interfaces>
    </config>
"""

# Print Operational Data using GET
netconf_reply = conn.edit_config(config = new_config, target = "running")

# Print output
print(netconf_reply)

