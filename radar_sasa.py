import requests
import time

def check():
    # بنعمل بحث عن اسم صاصا بلس كلمة تسريب
    url = "https://www.google.com/search?q=عصام+صاصا+تسريب+2026"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    print(f"📡 [{time.strftime('%H:%M:%S')}] Scanning for leaks...")
    
    try:
        r = requests.get(url, headers=headers)
        if "عصام صاصا" in r.text:
            print("🔥 Found something! Check manually: " + url)
        else:
            print("zzz.. Nothing yet.")
    except:
        print("Check internet!")

# بيكرر البحث كل دقيقتين عشان نلحق التسريب أول ما ينزل
while True:
    check()
    time.sleep(120)

