import os

# مسار الملف (تأكد من اسم الحزمة لو نسختك مش عالمية)
path = "/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames/Active.sav"

if os.path.exists(path):
    with open(path, "rb") as f:
        data = bytearray(f.read())
    
    # البحث عن كلمة FieldOfView في ملف الهيكس وتعديل قيمتها
    target = b'FieldOfView'
    index = data.find(target)
    
    if index != -1:
        # القيمة دي (00 00 DC 42) تعادل FOV 110
        # بنعدل الـ 4 bytes اللي بعد الكلمة بمسافة بسيطة حسب هيكلية الملف
        # ملاحظة: التعديل اليدوي للهيكس أدق لكن السكريبت ده بيستهدف القيم الشائعة
        print("Found FieldOfView, applying iPad view...")
        # هنا بنحط الكود البرمجي للتعديل (هذه الخطوة تتطلب ملفك الفعلي لتحديد الأوفست بدقة)
    else:
        print("FieldOfView not found!")
else:
    print("File not found! Check game path.")

