ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 3389, 8080]


try:
    port_number = int(input("Enter port to scan: "))
except ValueError:
    print("Error: Port must be a number!")
except KeyboardInterrupt:
    print("\nScan cancelled by user.") 
else:
    if port_number in ports:
        print(f"start scanning port {port_number}...")
    else:
        print(f"Port {port_number} is not in the list of common ports.")
finally:
    print("--- Port Scanner Closed ---")        