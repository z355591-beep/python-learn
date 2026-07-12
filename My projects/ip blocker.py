login_attempts = ["192.168.1.5", "10.0.0.2", "192.168.1.5", "192.168.1.5", "10.0.0.2", "192.168.1.5", "172.16.0.8", "192.168.1.5"]
ip_banned = []

for ip in login_attempts:
    
    
    if login_attempts.count(ip) > 3:
        if ip not in ip_banned:
            ip_banned.append(ip)
        else:
            print(f"{ip} is already banned.")

print("""
     +----------------------+
     | !Welcome to the      |
     |     IP Blocker!      |
     |                      |
     |                      |
     +----------------------+ 
      """)
print(f"Banned IPs: {ip_banned}")
