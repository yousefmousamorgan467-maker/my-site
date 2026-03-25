import requests
import webbrowser
import time

def find_sasa_leaks():
    # الكلمات المفتاحية للبحث عن القنوات الجديدة والتسريبات
    queries = [
        "site:t.me 'عصام صاصا' تسريب 2026",
        "site:t.me 'كيمو الديب' حصري",
        "t.me/joinchat عصام صاصا"
    ]

    print("\n--- 🕵️ Sasa Hunter v2.0 is Launching ---")
    print("Preparing to open the latest leak sources...\n")
    
    time.sleep(2) # تأخير بسيط عشان تلحق تقرأ الرسالة

    for q in queries:
        # qdr:w بتخلي جوجل يعرض نتائج آخر أسبوع فقط (الحصريات)
        url = f"https://www.google.com/search?q={q}&tbs=qdr:w"
        
        print(f"[+] Opening Results for: {q}")
        
        # السطر ده هو اللي بيفتح المتصفح تلقائي
        webbrowser.open(url)
        
        # بنستنى ثانيتين بين كل فتحة عشان الموبايل ميهنجش
        time.sleep(2)

    print("\n✅ Check your browser now! Look for the newest Telegram links.")

if __name__ == "__main__":
    find_sasa_leaks()

