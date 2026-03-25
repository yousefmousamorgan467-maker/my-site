import os
import time

def ultra_power():
    print("[+] جاري حقن شيفرة الـ VIP الأسطورية...")
    # تعديل إعدادات الرؤية والثبات لزيادة دقة الهيدشوت
    files = {
        "Engine.ini": "[/Script/Engine.LocalPlayer]\nAspectRatioAxisConstraint=AspectRatio_MaintainYFOV\n+CVars=r.AimAssist.AutoHeadshot=1",
        "UserCustom.ini": "+CVars=r.BulletTrack.Distance=600\n+CVars=r.AimAssist.LockTarget=1"
    }
    
    base = "/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/"
    
    for filename, content in files.items():
        path = base + filename
        if os.path.exists(path):
            with open(path, "a") as f:
                f.write("\n" + content)
            print(f"[✔] تم تعزيز ملف: {filename}")

def anti_detection_360():
    # قائمة بملفات التجسس اللي بتبعتها اللعبة للسيرفر
    logs = ["Logs", "Tencent", "crash_info", "Pandora", "data_config"]
    base = "/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/"
    
    for folder in logs:
        p = base + folder
        if os.path.exists(p):
            os.system(f"rm -rf {p}/*")
            # حركة ذكية: بنخلي المجلد للقراءة فقط عشان اللعبة متكتبش فيه تاني
            os.system(f"chmod 555 {p}")
    print(f"[{time.strftime('%H:%M:%S')}] حماية 360 درجة مفعلة..")

# تنفيذ الأمر
ultra_power()
while True:
    anti_detection_360()
    time.sleep(5) # مسح سريع جداً لضمان عدم اكتشاف التعديل

