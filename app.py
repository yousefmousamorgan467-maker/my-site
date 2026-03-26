from flask import Flask, render_template_string, request
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        search_query = request.form.get('search')
        if search_query:
            # ده الجزء اللي بيبحث في اليوتيوب ويجيب رابط الأغنية المباشر
            ydl_opts = {'format': 'bestaudio', 'noplaylist': True, 'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch:{search_query}", download=False)['entries'][0]
                video_url = info['url']

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yousef YouTube Player</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; padding: 20px; }
            .search-box { margin-bottom: 30px; }
            input { padding: 12px; width: 70%; border-radius: 25px; border: 1px solid #0f0; background: #111; color: #fff; }
            button { padding: 12px 20px; border-radius: 25px; border: none; background: #0f0; cursor: pointer; font-weight: bold; }
            .player-container { 
                background: rgba(255,255,255,0.05); border: 2px solid #0f0; 
                padding: 40px; border-radius: 40px; box-shadow: 0 0 20px #0f03;
            }
            audio { width: 100%; margin-top: 20px; }
            h1 { color: #0f0; text-shadow: 0 0 10px #0f0; }
        </style>
    </head>
    <body>
        <h1>Yousef Music Search</h1>
        <p>اكتب اسم أي أغنية من اليوتيوب وهتشتغل فوراً</p>
        
        <div class="search-box">
            <form method="POST">
                <input type="text" name="search" placeholder="ابحث عن أغنية أو تراك..." required>
                <button type="submit">بحث</button>
            </form>
        </div>

        {% if video_url %}
        <div class="player-container">
            <p style="color: #0f0;">جاري تشغيل طلبك الآن...</p>
            <audio controls autoplay>
                <source src="{{ video_url }}" type="audio/mpeg">
            </audio>
        </div>
        {% endif %}

        <p style="margin-top: 50px; color: #444;">Powered by Yousef & YT-API</p>
    </body>
    </html>
    """, video_url=video_url)

if __name__ == '__main__':
    app.run()
    
