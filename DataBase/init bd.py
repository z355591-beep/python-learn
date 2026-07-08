import sqlite3

# 1. الاتصال بقاعدة البيانات (بايثون سينشئ ملف atm_system.db تلقائياً إذا لم يكن موجوداً)
connection = sqlite3.connect("atm_system.db")
cursor = connection.cursor()

# 2. أمر SQL لإنشاء جدول الحسابات (Accounts) إذا لم يكن موجوداً سابقاً
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    pin INTEGER,
    checking REAL,
    savings REAL
)
""")

# 3. مسح أي بيانات قديمة (تصفير) لكي لا تتكرر البيانات
cursor.execute("DELETE FROM accounts")

# 4. إدخال بيانات حسابك الافتراضية لأول مرة
cursor.execute("""
INSERT INTO accounts (pin, checking, savings) 
VALUES (1234, 10000.0, 5000.0)
""")

# 5. حفظ التغييرات نهائياً في الملف وإغلاق الاتصال
connection.commit()
connection.close()

print("تم تأسيس قاعدة البيانات وجدول الحسابات بنجاح بالبيانات الافتراضية!")
