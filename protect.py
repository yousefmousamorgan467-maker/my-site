import os
import time

# مسارات ملفات السجل الشائعة (تختلف حسب اللعبة)
log_paths = [
    "/sdcard/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Logs",
    "/sdcard/Android/data/com.dts.freefireth/files/report_log.txt"
]

def clear_logs():
    print("[+] يتم الآن تنظيف ملفات السجل للحماية...")
    for path in log_paths:
        if os.path.exists(path):
            try:
                os.system(f"rm -rf {path}/*")
                print(f"[✔] تم تنظيف: {path}")
            except:
                print(f"[!] فشل تنظيف: {path}")
    print("[✔] الحماية نشطة الآن..")

while True:
    clear_logs()
    time.sleep(30) # يقوم بالمسح كل 30 ثانية أثناء اللعب

