import os
import sqlite3

# حساب المسار التلقائي للملف ليكون في نفس مجلد السكريبت دائماً
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "atm_system.db")

# الاتصال بالمسار الديناميكي
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# إنشاء الجدول
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    user_name TEXT,
    pin INTEGER,
    checking REAL,
    savings REAL
)
""")

# تصفير البيانات القديمة وحقن الحساب الافتراضي
cursor.execute("DELETE FROM accounts")
cursor.execute("""
INSERT INTO accounts (user_name, pin, checking, savings) 
VALUES ('Abdullah', 1234, 10000.0, 5000.0)
""")

connection.commit()
connection.close()

print("تم تأسيس قاعدة البيانات وجدول الحسابات بنجاح بالبيانات الافتراضية!")