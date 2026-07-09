import socket

def scan_ports(target_host, ports_list):
    print(f"\n⚡ Starting scan on: {target_host}")
    
    try:
        # تحويل اسم النطاق (مثل google.com) إلى عنوان IP حقيقي
        target_ip = socket.gethostbyname(target_host)
        print(f"🎯 Target IP resolved: {target_ip}\n")
    except socket.gaierror:
        print("❌ Error: Could not resolve hostname. Check your internet or spelling.")
        return

    # الدوران على قائمة المنافذ وفحصها واحداً تلو الآخر
    for port in ports_list:
        # إنشاء كائن الاتصال (AF_INET تعني IPv4، و SOCK_STREAM تعني بروتوكول TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # وضع حد أقصى للانتظار (Timeout) ثانية واحدة لكل منفذ عشان ما يعلق البرنامج
        s.settimeout(1.0)
        
        # محاولة الاتصال (تأخذ الهدف والمنفذ داخل قوسين كـ Tuple)
        result = s.connect_ex((target_ip, port))
        
        # --- تحديك هنا ---   
        # إذا كانت النتيجة (result) تساوي 0، فهذا يعني أن المنفذ مفتوح! 
        # اطبع رسالة نجاح توضح أن المنفذ مفتوح. وإلا (else) يمكنك تجاهله أو طباعة أنه مغلق.
        if result == 0:
            print(f"✅ Port {port} is OPEN")
        else:
            pass
            
        # إغلاق كائن الاتصال فوراً بعد الفحص لتحرير موارد الشبكة (مهم جداً أمنياً!)
        s.close()

# --- البرنامج الرئيسي ---
print("=== Cyber-Port Scanner v1.0 ===")
host_to_scan = input("Enter target website or IP (e.g., google.com or 127.0.0.1): ")

# قائمة بأشهر المنافذ الأمنية الحساسة لفحصها
target_ports = [21, 22, 23, 80, 443, 8080]

# استدعاء الدالة
scan_ports(host_to_scan, target_ports)