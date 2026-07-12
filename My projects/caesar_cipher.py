message = input("Enter your message to encrypt: ")
key = int(input("Enter key number: "))

# صندوق نصي فارغ لتجميع الحروف المشفرة داخله
encrypted_message = "" 

# حلقة تدور على الرسالة وتسحبها حرفاً حرفاً وتضعه في المتغير char
for char in message:
    
    # --- تحديك هنا ---
    # 1. حول الحرف (char) إلى رقم واجمع معه المفتاح (key) وخزنه في متغير (مثلاً: num)
    num = ord(char) + key
    # 2. حول الرقم الجديد (num) إلى حرف مشفر وخزنه في متغير (مثلاً: new_char)
    new_char = chr(num)
    # 3. أضف الحرف المشفر للصندوق: 
    # encrypted_message += new_char
    encrypted_message += new_char

# في النهاية نطبع الصندوق بعد أن امتلأ بالرسالة المشفرة
print(f"Your encrypted message is: {encrypted_message}")