from flask import Flask, render_template_string, request, Response
import requests
import yt_dlp
import os

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
        <body style="background:#000; color:#1db954; text-align:center; font-family:sans-serif; padding-top:50px;">
            <div style="border:2px solid #1db954; display:inline-block; padding:30px; border-radius:25px; background:#111;">
                <h1>🎸 Yousef Studio</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اسم الأغنية..." style="padding:10px; border-radius:15px;">
                    <button type="submit" style="padding:10px; background:#1db954; border-radius:15px; cursor:pointer;">بحث</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:20px;">
                        <h3>🎶 {{ title }}</h3>
                        <iframe width="1" height="1" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay"></iframe>
                        <p>✅ شغال في الخلفية</p>
                        <form action="/download_file" method="get">
                            <input type="hidden" name="id" value="{{ v_id }}">
                            <button type="submit" style="background:#fff; color:#000; margin-top:10px;">تحميل MP3 مباشر (تجريبي) ⬇️</button>
                        </form>
                    </div>
                {% endif %}
            </div>
        </body>
    ''', v_id=v_id, title=title)

@app.route('/download_file')
def download_file():
    v_id = request.args.get('id')
    yt_url = f"https://www.youtube.com/watch?v={v_id}"
    
    # إعدادات التحميل المباشر (صوت فقط)
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(yt_url, download=False)
            audio_url = info['url']
            
            # بنسحب الملف من يوتيوب ونبعته للمتصفح كأنه ملف للتحميل
            response = requests.get(audio_url, stream=True)
            return Response(
                response.iter_content(chunk_size=1024),
                content_type='audio/mpeg',
                headers={"Content-Disposition": f"attachment; filename=yousef_music.mp3"}
            )
    except Exception as e:
        return f"خطأ في التحميل: {str(e)}"

app = app
