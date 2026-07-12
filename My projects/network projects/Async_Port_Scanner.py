import asyncio
import socket


# 1. دالة فحص منفذ واحد (بشكل غير متزامن)
async def scan_single_port(target_ip, port):
    try:
        # محاولة فتح اتصال TCP بشكل غير متزامن
        # asyncio.open_connection هي البديل الذكي لـ socket.connect_ex
        make_connection = asyncio.open_connection(target_ip, port)

        # وضع عداد الصبر (Timeout) لمدة ثانية واحدة؛ إذا لم يستجب المنفذ يرمي خطأ TimeoutError
        reader, writer = await asyncio.wait_for(make_connection, timeout=1.0)

        # إذا وصلنا هنا بدون أخطاء، فهذا يعني أن المنفذ مفتوح بنجاح!
        print(f"✅ Port {port} is OPEN")

        # إغلاق الاتصال فوراً بسلام لتحرير الشبكة
        writer.close()
        await writer.wait_closed()

    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        # الأخطاء المتوقعة: إما انتهت الثواني، أو السيرفر رفض الاتصال (المنفذ مغلق)
        # نمر بصمت عبر pass مثل كودك السابق تماماً
        pass


# 2. الدالة الرئيسية التي تدير طابور المنافذ
async def main_scanner(target_host, ports_list):
    print(f"\n⚡ Starting Async Scan on: {target_host}")

    try:
        # جلب الـ IP للموقع كما فعلت سابقاً
        target_ip = socket.gethostbyname(target_host)
        print(f"🎯 Target IP resolved: {target_ip}\n")
    except socket.gaierror:
        print(
            "❌ Error: Could not resolve hostname. Check internet or spelling."
        )
        return

    print(f"⌛ Scanning {len(ports_list)} ports simultaneously... Please wait.")

    # [مفهوم Comprehension المتقدم سطر واحد]: نجهز قائمة بمهام الفحص لكل المنافذ
    tasks = [scan_single_port(target_ip, port) for port in ports_list]

    # إطلاق كل المهام في الشبكة دفعة واحدة في نفس اللحظة والانتظار حتى ينتهوا معاً
    await asyncio.gather(*tasks)


# --- البرنامج الرئيسي ---
print("=== Cyber-Async Port Scanner v2.0 ===")
host_to_scan = input(
    "Enter target website or IP (e.g., google.com or 127.0.0.1): "
)

# لتشعر بالسرعة الخارقة، دعنا نفحص أول 1000 منفذ كاملة!
# دالة list(range(1, 1001)) تجهز قائمة بالأرقام من 1 إلى 1000 لتمجيد قوة الـ Async
target_ports = list(range(1, 10001))

# تشغيل محرك بايثون غير المتزامن وإعطاؤه أمر البدء
asyncio.run(main_scanner(host_to_scan, target_ports))