import os
import shutil

# مسار فولدر التحميلات عندك
path = "/sdcard/Download"

# قائمة بأنواع الملفات وفولدراتها
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:].lower() # بنجيب الامتداد من غير النقطة

    if extension in ["jpg", "jpeg", "png", "gif"]:
        folder = "Images"
    elif extension in ["mp4", "mkv", "mov"]:
        folder = "Videos"
    elif extension in ["pdf", "docx", "txt", "pptx"]:
        folder = "Study_Materials"
    elif extension in ["mp3", "wav", "m4a"]:
        folder = "Audio"

    else:
        continue

    # إنشاء الفولدر لو مش موجود
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

    # نقل الملف
    shutil.move(os.path.join(path, file), os.path.join(path, folder, file))
    print(f"Moved {file} to {folder}")

print("تم تنظيف فولدر التحميلات بنجاح! 😎")

