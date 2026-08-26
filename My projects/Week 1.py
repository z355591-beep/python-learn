# --- البيانات القادمة من النظام ---
target_user = "ADMIN"
attacker_ip = "10.0.0.1"

# --- قاعدة بياناتك الحالية ---
attack_counts = {"192.168.1.5": 2, "10.0.0.1": 4} # قاموس يحسب عدد الهجمات لكل IP
blocked_ips = ["172.16.0.8"] # قائمة الآيبيهات المحظورة

target_user = target_user.lower()  # تحويل اسم المستخدم إلى أحرف صغيرة
attack_counts[attacker_ip] += 1  # زيادة عدد الهجمات للآيبي المهاجم

if attack_counts[attacker_ip] == 5:
    blocked_ips.append(attacker_ip)  

for IP , Total_Attacks in attack_counts.items():
    print(f"IP: {IP}, Total Attacks: {Total_Attacks}")

print(f"Blocked IPs: {blocked_ips}")