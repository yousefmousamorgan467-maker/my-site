from flask import Flask, render_template_string, request, redirect
import requests
import yt_dlp

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
            <title>Yousef Music Pro</title>
            <style>
                body { background: #000; color: #1db954; text-align: center; font-family: sans-serif; padding: 20px; }
                .card { border: 2px solid #1db954; display: inline-block; padding: 30px; border-radius: 25px; background: #111; box-shadow: 0 0 20px #1db954; width: 90%; max-width: 400px; }
                input { padding: 15px; border-radius: 25px; border: none; width: 80%; margin-bottom: 10px; background: #222; color: #fff; text-align: center; }
                button { padding: 12px 25px; background: #1db954; color: #000; font-weight: bold; border: none; border-radius: 25px; cursor: pointer; margin: 5px; }
                .download-btn { background: #fff; color: #000; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎸 Yousef Studio</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="ابحث عن أغنيتك...">
                    <br>
                    <button type="submit">بحث وتشغيل 🔍</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:20px;">
                        <h3>جاري تشغيل: {{ title }}</h3>
                        
                        <iframe id="player" width="1" height="1" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay"></iframe>
                        
                        <div style="margin-top:20px;">
                            <p>✅ شغال في الخلفية الآن</p>
                            <a href="/download/{{ v_id }}" target="_blank">
                                <button class="download-btn">تحميل MP3 ⬇️</button>
                            </a>
                        </div>
                    </div>
                {% endif %}
            </div>
            <p style="color:#444; margin-top:30px;">تطوير يوسف - مبرمج تالتة ثانوي 🎓</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

@app.route('/download/<v_id>')
def download(v_id):
    # حيلة بسيطة للتحميل باستخدام موقع وسيط عشان سيرفر Vercel ميهنجش
    return redirect(f"https://www.youtubepp.com/watch?v={v_id}")

app = app
    
