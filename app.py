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
            <title>Yousef Music</title>
            <style>
                body { background: #000; color: #fff; text-align: center; font-family: sans-serif; padding: 20px; }
                .card { border: 2px solid #ff0050; display: inline-block; padding: 25px; border-radius: 30px; background: #111; width: 100%; max-width: 450px; }
                h1 { color: #ff0050; margin-bottom: 5px; }
                input { padding: 15px; border-radius: 25px; border: none; width: 85%; margin-bottom: 15px; background: #222; color: #fff; text-align: center; outline: none; }
                .btn-search { padding: 12px 30px; background: #ff0050; color: #fff; font-weight: bold; border: none; border-radius: 25px; cursor: pointer; width: 100%; }
                .download-section { margin-top: 25px; border-top: 1px solid #333; padding-top: 20px; }
                .dl-btn { display: block; background: #fff; color: #000; text-decoration: none; padding: 15px; border-radius: 20px; font-weight: bold; margin-top: 15px; }
                iframe { border-radius: 20px; border: 1px solid #ff0050; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎧 Yousef Music</h1>
                <p style="color:#888;">استمتع وتحميل الأغاني مجاناً</p>
                <form method="POST">
                    <input type="text" name="query" placeholder="ابحث عن أغنيتك المفضلة..." required>
                    <button type="submit" class="btn-search">بحث وتشغيل 🎵</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div class="download-section">
                        <h3 style="color:#ff0050;">🎶 {{ title }}</h3>
                        <iframe width="100%" height="220" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay"></iframe>
                        
                        <a href="https://api.vevioz.com/api/button/mp3/{{ v_id }}" target="_blank" class="dl-btn">
                            📥 اضغط هنا لتحميل MP3
                        </a>
                        <p style="font-size: 11px; color: #555; margin-top: 10px;">لو الصفحة فتحت، استنى 3 ثواني والتحميل هيبدأ لوحده</p>
                    </div>
                {% endif %}
            </div>
            <p style="color:#222; margin-top:40px;">Yousef Music - 3rd Secondary Student 🎓</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

app = app
