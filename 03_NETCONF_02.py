from ncclient import manager
from xml.dom.minidom import parseString

# Create an SSH Connection on port 830

conn = manager.connect(
    host = "10.255.1.101",
    port = "830",
    username = "admin",
    password = "cisco",
    hostkey_verify = False
)

print ("\n NETCONF Connection Established")

my_filter0 = """
<filter>
    <interfaces-state xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

    </interfaces-state>
</filter>
"""

my_filter = """
<filter>
    <interfaces-state xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name></name>
            <statistics>
                <in-octets></in-octets>
            </statistics>
        </interface>
    </interfaces-state>
</filter>
"""

# Print Operational Data using GET
netconf_reply = conn.get(filter= my_filter)

# Beautify the XML print
beauty_xml = parseString(netconf_reply.xml).toprettyxml()

print(beauty_xml)
