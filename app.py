from scrapli_netconf import NetconfDriver
import datetime

start_time = datetime.datetime.now()
print ("Current date and time : ")
print (start_time.strftime("%Y-%m-%d %H:%M:%S"))

junos_device = {
    "host": "192.168.41.30",
    "auth_username": "lab",
    "auth_password": "lab123",
    "auth_strict_key": False,
    "port": 22
}

rpc= """
<get-zones-information>
</get-zones-information>
"""

def main():
    conn = NetconfDriver(**junos_device)
    print("We have declared our connection object, but do not have an active SSH session yet")
    conn.open()
    
    result =conn.rpc(filter_= rpc)
    print(result.result)
    print("We have an active SSH connection to our firewall")
    
    conn.close()
    
    finish_time = datetime.datetime.now()
    print ("Current date and time : ")
    print (finish_time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    main()