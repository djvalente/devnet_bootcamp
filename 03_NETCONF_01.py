from ncclient import manager
from xml.dom.minidom import parseString

# Create an SSH Connection on port 830

conn = manager.connect(
    host = "10.255.1.102",
    port = "830",
    username = "admin",
    password = "cisco",
    hostkey_verify = False
)

print ("\n NETCONF Connection Established")

# Filter to use on the Running Config
my_filter1 = """
<filter>
    <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">

    </interfaces>
</filter>
"""

my_filter2 = """
<filter>
    <routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
        <routing-instance>
            <routing-protocols></routing-protocols>
        </routing-instance>
    </routing>
</filter>
"""

# Imprimir a running config em XML - GET_CONFIG gets configuration Data

# netconf_reply = conn.get_config(source="running") # Full config
netconf_reply = conn.get_config(source="running", filter = my_filter1) # Full config


# Beautify the XML print
beauty_xml = parseString(netconf_reply.xml).toprettyxml()

print(beauty_xml)
