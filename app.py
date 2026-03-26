from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ"

@app.route('/', methods=['GET', 'POST'])
def index():
    v_id = None
    title = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            try:
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
            <title>Yousef Music | يوسف ميوزك</title>
            <style>
                body { background: #000; color: #fff; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; }
                .card { border: 2px solid #ff0050; display: inline-block; padding: 30px; border-radius: 30px; background: #111; width: 100%; max-width: 450px; margin-top: 40px; box-shadow: 0 0 20px rgba(255, 0, 80, 0.2); }
                h1 { color: #ff0050; margin-bottom: 5px; }
                input { padding: 15px; border-radius: 30px; border: 1px solid #333; width: 80%; margin-bottom: 15px; background: #222; color: #fff; text-align: center; outline: none; }
                button { padding: 12px 30px; background: #ff0050; color: #fff; font-weight: bold; border: none; border-radius: 30px; cursor: pointer; transition: 0.3s; }
                button:hover { background: #ff2e73; transform: scale(1.05); }
                .download-btn { display: block; margin-top: 25px; background: #fff; color: #000; text-decoration: none; padding: 15px; border-radius: 20px; font-weight: bold; }
                iframe { border-radius: 20px; margin-top: 20px; border: 1px solid #ff0050; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎧 Yousef Music</h1>
                <p style="color:#888; margin-bottom:20px;">استمتع وتحميل الأغاني مجاناً</p>
                <form method="POST">
                    <input type="text" name="query" placeholder="ابحث عن أغنيتك المفضلة..." required>
                    <button type="submit">بحث وتشغيل 🎵</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:20px;">
                        <h3 style="color:#ff0050;">🎶 {{ title }}</h3>
                        <iframe width="100%" height="220" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay"></iframe>
                        <a href="https://api.vevioz.com/api/button/mp3/{{ v_id }}" target="_blank" class="download-link">تحميل MP3 مباشر 📥</a>
                    </div>
                {% endif %}
            </div>
            <p style="color:#333; margin-top:50px; font-size:12px;">Yousef Music - Version 2.0</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

app = app
