import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# حط المفتاح اللي بيبدأ بـ AIza هنا بين القوسين
API_KEY = "AIzaSyBJuy12nBn7rWayQmWmyOpcbX0NKMMSKG4"

@app.route('/', methods=['GET', 'POST'])
def home():
    video_id = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # ده السطر اللي بيستخدم المفتاح بتاعك عشان يجيب الفيديو
            url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}&maxResults=1"
            response = requests.get(url).json()
            if "items" in response and response["items"]:
                video_id = response["items"][0]["id"]["videoId"]

    return render_template_string('''
        <body style="background:#000; color:#fff; text-align:center; font-family:sans-serif; padding:20px;">
            <div style="border:2px solid #1db954; border-radius:20px; padding:20px; max-width:400px; margin:auto; background:#111;">
                <h1 style="color:#1db954;">🎸 Yousef Music Engine</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="بحث عن أغنية..." style="width:100%; padding:12px; border-radius:20px; border:none; margin-bottom:10px; text-align:center;">
                    <button type="submit" style="width:100%; padding:10px; border-radius:20px; background:#1db954; color:#000; font-weight:bold; border:none;">تشغيل</button>
                </form>
                {% if video_id %}
                    <iframe width="100%" height="220" src="https://www.youtube-nocookie.com/embed/{{ video_id }}?autoplay=1" frameborder="0" style="margin-top:20px; border-radius:15px;" allowfullscreen></iframe>
                {% endif %}
            </div>
            <p style="color:#555; font-size:12px; margin-top:15px;">Developed by Yousef 🎓</p>
        </body>
    ''', video_id=video_id)
    
