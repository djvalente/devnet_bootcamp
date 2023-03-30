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

# Imprimir a running config em XML
netconf_reply = conn.get_config(source="running")

# Beautify the XML print
beauty_xml = parseString(netconf_reply.xml).toprettyxml()

print(beauty_xml)
