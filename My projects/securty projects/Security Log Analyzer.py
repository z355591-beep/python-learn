raw_logs = [
    "192.168.1.15|80|SUCCESS",
    "10.0.0.2|22|FAILED",
    "172.16.0.8-443-SUCCESS", # تنبيه: هذا السجل مكتوب بصيغة خاطئة (-) بدلاً من (|)
    "10.0.0.2|22|FAILED",
    "MALICIOUS_PACKET_DROP",  # تنبيه: هذا السجل تالف تماماً
    "192.168.1.20|8080|FAILED",
    "10.0.0.2|22|FAILED"
]

threat_db = {} # قاموس لجمع الآيبيهات التي فشلت في الدخول وعدد مرات الفشل
blocked_ips = [] # قائمة الآيبيهات التي سيتم حظرها

for log in raw_logs:
    try:
        ip, port, status = log.split('|')
        port = int(port)

    except ValueError:
            print("Corrupted log detected and skipped.")
    else:
        if status == "FAILED":
            threat_db[ip] = threat_db.get(ip, 0) + 1
            if threat_db[ip] >= 3:
                blocked_ips.append(ip)
                print("you have been blocked") 

print("Threat Database:", threat_db)
print("Blocked IPs:", blocked_ips)                      