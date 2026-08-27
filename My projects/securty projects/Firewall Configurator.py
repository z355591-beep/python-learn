def configure_firewall(action, port, protocol):
    return f"Firewall Rule: {action} traffic on port {port} via {protocol}"


print(configure_firewall("TCP", 22, "Block"))