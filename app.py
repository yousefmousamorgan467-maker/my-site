from flask import Flask, render_template_string, request, redirect
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
                body { background: #0b0b0b; color: #1db954; text-align: center; font-family: sans-serif; padding: 20px; }
                .card { border: 2px solid #1db954; display: inline-block; padding: 30px; border-radius: 25px; background: #111; box-shadow: 0 0 20px rgba(29, 185, 84, 0.3); width: 100%; max-width: 400px; margin-top: 40px; }
                input { padding: 15px; border-radius: 25px; border: none; width: 85%; margin-bottom: 15px; background: #222; color: #fff; text-align: center; outline: none; }
                button { padding: 12px 25px; background: #1db954; color: #000; font-weight: bold; border: none; border-radius: 25px; cursor: pointer; width: 100%; transition: 0.3s; }
                .download-link { display: block; margin-top: 20px; color: #000; text-decoration: none; background: #fff; padding: 10px; border-radius: 15px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎸 Yousef Studio</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية..." required>
                    <button type="submit">تشغيل وتحميل 🚀</button>
                </form>
                {% if v_id and v_id != "error" %}
                    <div style="margin-top:25px;">
                        <h3 style="color:#fff;">🎶 {{ title }}</h3>
                        <iframe width="1" height="1" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay"></iframe>
                        <p style="font-size:12px; color:#888;">✅ شغالة في الخلفية</p>
                        <a href="/download/{{ v_id }}" target="_blank" class="download-link">تحميل MP3 مباشر ⬇️</a>
                    </div>
                {% endif %}
            </div>
            <p style="color:#444; margin-top:40px; font-size:12px;">Yousef - 3rd Secondary Student 🎓</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

@app.route('/download/<v_id>')
def download(v_id):
    return redirect(f"https://x2mate.com/en/download?url=https://www.youtube.com/watch?v={v_id}")

app = app
                
