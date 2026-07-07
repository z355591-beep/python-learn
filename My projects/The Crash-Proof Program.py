while True:
    try:
        # 1. اطلب من المستخدم إدخال رقم وقم بتحويله إلى int هنا
        number = int(input("Enter a number: "))
        # 2. إذا نجح التحويل بدون مشاكل، اطبع رسالة نجاح واخرج بـ break
        print("Number entered successfully!")
        break
    except ValueError:
        # 3. هنا يركض الكمبيوتر فوراً إذا أدخل المستخدم حروفاً تسببت في خطأ
        # اطبع رسالة تنبيهية للمستخدم هنا
        print("Invalid input. Please enter a valid number.")
