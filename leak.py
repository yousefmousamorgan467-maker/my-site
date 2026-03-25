import requests

# تعريف المتغيرات
artist = "Essam Sasa"
query = "عصام صاصا تسريبات"

# لينكات البحث في أهم المنصات اللي بينزل عليها تسريبات
sc_url = f"https://soundcloud.com/search/sounds?q={query}"
yt_url = f"https://www.youtube.com/results?search_query={query}+2026"

print(f"\n--- ⚡ Searching for {artist} Unreleased Tracks ⚡ ---\n")
print(f"1. Check SoundCloud Leaks:\n   {sc_url}\n")
print(f"2. Check YouTube Recent Uploads:\n   {yt_url}\n")

# تجربة الاتصال بالسيرفر
try:
    check = requests.get("https://soundcloud.com", timeout=5)
    if check.status_code == 200:
        print("✅ Connection to servers is stable. Happy hunting!")
except:
    print("❌ Check your internet connection.")

