import subprocess
import optparse

def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option('-i','--interface',dest='interface',help='interface to change its mac address')
    parse.add_option('-m','--mac',dest='new_mac',help='new mac address')
    #option is the option like -i -m etc and arguments is foe examole wlan0 for interface(dest)
    return parse.parse_args() # parse_args return two values

def ChangeMac(interface,option):
    print('[+] Changing Mac for '+ interface+'to' + new_mac)
     
    subprocess.call(['ifconfig',interface,'down'])
    subprocess.call(['ifconfig',interface,'hw','ether',new_mac])
    subprocess.call(['ifconfig',interface,'up'])
    

(option,arguments)=get_arguments()

ChangeMac(option.interface,option.new_mac)

# For windows

# def change_mac_address(interface, new_mac):
#     try:
#         # Disable the network adapter
#         subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=disable"])

#         # Change the MAC address
#         subprocess.call(["netsh", "interface", "set", "interface", interface, "mac=" + new_mac])

#         # Enable the network adapter
#         subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=enable"])

#         print(f"MAC address of {interface} changed to {new_mac}")
#     except Exception as e:
#         print(f"Error: {e}")

# # Replace 'Wi-Fi' with the name of your network adapter and '00:11:22:33:44:55' with the desired MAC address
# change_mac_address("Wi-Fi", "00:11:22:33:44:55")


