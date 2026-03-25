import os
import time

# --- مصفوفة القيم القوية جداً (Ultra Values) ---
def apply_ultra_power():
    print("[+] جاري استدعاء قيم الهيدشوت العميقة...")
    # مسار ملف المحرك (Engine.ini) لزيادة سرعة معالجة الهدف
    engine_path = "/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/Engine.ini"
    
    ultra_settings = [
        "[/Script/Engine.PlayerInput]",
        "bEnableMouseSmoothing=false",
        "r.AimAssist.MaxAngle=180.0", # زيادة زاوية المساعدة لـ 180 درجة
        "r.BulletTrack.Distance=800.0", # تتبع الرصاص لمسافات بعيدة
        "r.ConfineCursorToWindow=True",
        "r.AimAssist.LockOnHead=1" # محاولة قفل الأيم على الرأس
    ]
    
    try:
        if os.path.exists(engine_path):
            with open(engine_path, "w") as f:
                f.write("\n".join(ultra_settings))
            print("[✔] تم تفعيل القوة القصوى للهيدشوت!")
    except Exception as e:
        print(f"[!] خطأ في الوصول للملف: {e}")

# --- نظام الحماية الشامل (Super Antiban) ---
def super_antiban():
    # قائمة الملفات التي تكتشف التعديل
    bad_files = [
        "Logs", "CrashSentinel", "BugReport.zip", "client_log.txt", "TssData"
    ]
    base_path = "/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/"
    
    for folder in bad_files:
        full_path = base_path + folder
        if os.path.exists(full_path):
            os.system(f"rm -rf {full_path}/*")
            # خدعة برمجية: إنشاء ملف فارغ بنفس الاسم لمنع اللعبة من إعادة الكتابة
            os.system(f"touch {full_path}/antiban.log") 
    
    print(f"[{time.strftime('%H:%M:%S')}] حماية نشطة: تم تضليل نظام الحماية")

# --- بدء التشغيل ---
apply_ultra_power()
while True:
    super_antiban()
    time.sleep(10) # مسح السجلات كل 10 ثواني لضمان الأمان

