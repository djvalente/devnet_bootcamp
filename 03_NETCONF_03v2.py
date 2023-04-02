"""
Change configuration on a IOS_XE router usgin NETCONF
"""

from ncclient import manager
from xml.dom.minidom import parseString
from getpass import getpass

print ("\n Welcome to IOS XE NETCONF Utility, please authenticate yoursel: ")
rt_user = input("Enter your username: ")
rt_pass = getpass("Please enter your password")

if rt_user == "admin" and rt_pass == "cisco":
    
    # Create an SSH Connection on port 830
    conn = manager.connect(
        host = "10.255.1.102",
        port = "830",
        username = "admin",
        password = "cisco",
        hostkey_verify = False
    )

    print ("\n NETCONF Connection OK\nInput your data please:\n")

    user_choice = int(input("1. For physical interface\n2. For Loopback Interfaces\Make a chooice (1/2): "))

    if user_choice == 1:
        int_type = 'ethernetCsmacd'
    elif user_choice == 2:
        int_type = 'softwareLoopback'
    else:
        print("Invalid Input Detected")
        quit()

    int_name = input("Enter an interface name: ")
    int_desc = input("Enter an interface description: ")
    int_ip = input("Enter an interface IP address: ")
    int_mask = input("Enter an interface Mask: ")

    new_config = f"""
        <config>
            <interfaces xmlns = "urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>{int_name}</name>
                    <description>{int_desc}</description>
                    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                        ianaift:{int_type}
                    </type>
                    <enabled>true</enabled>
                    <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                        <address>
                                <ip>{int_ip}</ip>
                                <netmask>{int_mask}</netmask>
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

else:
    print ("Invalid credentials")