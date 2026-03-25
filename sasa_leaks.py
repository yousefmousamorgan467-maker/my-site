import requests

# استخدمنا الفرانكو والاسم الإنجليزي عشان اللينك ما يبوظش في الـ Terminal
artist_name = "Essam+Sasa"
leak_keyword = "Unreleased+2026"

# اللينك ده هيدور في جوجل مباشرة على الفيديوهات والملفات الصوتية
google_search = f"https://www.google.com/search?q={artist_name}+{leak_keyword}"
# لينك يوتيوب مباشر (فلتر بآخر فيديوهات نزلت)
yt_search = f"https://www.youtube.com/results?search_query={artist_name}+جديد+2026&sp=CAI%253D"

print("\n--- ⚡ Essam Sasa Leaks Finder ⚡ ---\n")
print(f"1. Open this link for Google results:\n{google_search}\n")
print(f"2. Open this link for Newest YouTube videos:\n{yt_search}\n")

print("💡 Tip: Copy the link and paste it in Chrome carefully.")

