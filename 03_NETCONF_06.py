"""
Delete configuration from device
"""

from ncclient import manager
from xml.dom.minidom import parseString
from getpass import getpass

netconf = manager.connect(
	host = "10.255.1.101",
	port = "830",
	username = input ("Enter your Username: "),
	password = getpass ("Enter your Password: "),
	hostkey_verify = False
)
print ("\n NETCONF Connection EST with CSR1")

interface_payload = """
<config>
	<native xmlns = "http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<interface>
			<GigabitEthernet>
				<name>2</name>
				<description operation="delete"></description>
			</GigabitEthernet>
		</interface>
	</native>
</config>
"""

int_config = netconf.edit_config(config = interface_payload, target = "running")
print(int_config)