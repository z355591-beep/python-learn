login_attempts = ["192.168.1.5", "10.0.0.2", "192.168.1.5", "192.168.1.5", "10.0.0.2", "192.168.1.5", "172.16.0.8", "192.168.1.5"]
ip_banned = []

for ip in login_attempts:
    print("""
     +----------------------+
     | !Welcome to the      |
     |     IP Blocker!      |
     |                      |
     |                      |
     +----------------------+ 
      """)
    print("please Enter your IP address to check if it is banned or not.")
    ip_address = input("Enter the IP address to check: ")

    if login_attempts.count(ip_address) > 3:
        if ip_address not in ip_banned:
            ip_banned.append(ip_address)
            print(f"IP address {ip_address} has been banned due to multiple failed login attempts.")
        else:
            print(f"IP address {ip_address} is already banned.")
            break
    else:
        print(f"IP address {ip_address} is not banned.")
        break
    








