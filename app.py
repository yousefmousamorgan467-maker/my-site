from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# مفتاح الـ API الخاص بيك
API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ"

@app.route('/', methods=['GET', 'POST'])
def index():
    v_id = None
    title = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            try:
                # طلب البحث من يوتيوب
                url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}&maxResults=1"
                res = requests.get(url).json()
                if "items" in res and len(res["items"]) > 0:
                    v_id = res['items'][0]['id']['videoId']
                    title = res['items'][0]['snippet']['title']
            except:
                v_id = "error"
    
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Yousef Studio Pro</title>
            <style>
                body { background: #0b0b0b; color: #1db954; text-align: center; font-family: sans-serif; padding: 20px; }
                .card { border: 2px solid #1db954; display: inline-block; padding: 30px; border-radius: 25px; background: #111; width: 100%; max-width: 400px; margin-top: 40px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
                input { padding: 15px; border-radius: 25px; border: none; width: 85%; margin-bottom: 15px; background: #222; color: #fff; text-align: center; outline: none; }
                button { padding: 12px 25px; background: #1db954; color: #000; font-weight: bold; border: none; border-radius: 25px; cursor: pointer; width: 100%; }
                .dl-link { display: block; margin-top: 20px; background: #fff; color: #000; text-decoration: none; padding: 15px; border-radius: 20px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎸 Yousef Studio</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اسم الأغنية..." required>
                    <button type="submit">بحث وتشغيل 🚀</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:25px;">
                        <h3 style="color:#fff;">🎶 {{ title }}</h3>
                        <iframe width="100%" height="200" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay" style="border-radius:15px;"></iframe>
                        
                        <a href="https://api.vevioz.com/api/button/mp3/{{ v_id }}" target="_blank" class="dl-link">تحميل MP3 للموبايل ⬇️</a>
                    </div>
                {% endif %}
            </div>
            <p style="color:#444; margin-top:40px; font-size:12px;">Yousef - Thanaweya Amma 2026 🎓</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

app = app
