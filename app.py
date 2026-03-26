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
            <title>Yousef Music | Remix Edition</title>
            <style>
                body { background: #000; color: #fff; text-align: center; font-family: sans-serif; padding: 10px; }
                .container { max-width: 500px; margin: auto; background: #111; padding: 20px; border-radius: 25px; border: 1px solid #ff0050; }
                h1 { color: #ff0050; text-shadow: 0 0 10px #ff0050; }
                input { width: 80%; padding: 12px; border-radius: 20px; border: none; background: #222; color: #fff; margin-bottom: 10px; text-align: center; }
                .btn-main { width: 90%; padding: 12px; background: #ff0050; color: #fff; border: none; border-radius: 20px; font-weight: bold; cursor: pointer; }
                
                /* أزرار الريمكس الجانبية */
                .remix-panel { margin-top: 15px; display: flex; justify-content: center; gap: 10px; }
                .side-btn { background: #333; color: #0f0; border: 1px solid #0f0; padding: 8px 15px; border-radius: 15px; font-size: 12px; cursor: pointer; }
                .side-btn.active { background: #0f0; color: #000; }
                
                iframe { border-radius: 15px; margin-top: 15px; filter: grayscale(100%) invert(100%); display: none; } /* مخفي عشان نتحكم في الصوت */
                .custom-player { background: #222; padding: 15px; border-radius: 15px; margin-top: 15px; }
                .play-pause { font-size: 30px; cursor: pointer; color: #ff0050; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎧 Yousef Music</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اسم الأغنية اللي عايز تعملها ريمكس..." required>
                    <button type="submit" class="btn-main">بحث وتحويل 🚀</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div class="custom-player">
                        <h3 id="trackTitle">{{ title }}</h3>
                        
                        <div id="youtube-audio"></div>

                        <div class="play-pause" id="ctrlIcon" onclick="togglePlay()">▶️</div>
                        
                        <div class="remix-panel">
                            <button class="side-btn" onclick="applyEffect('speed')">⚡ ريمكس سريع</button>
                            <button class="side-btn" onclick="applyEffect('bass')">🔊 دبة عالية</button>
                            <button class="side-btn" onclick="applyEffect('normal')">🔄 طبيعي</button>
                        </div>

                        <a href="https://loader.to/api/button/?url=https://www.youtube.com/watch?v={{ v_id }}&f=mp3" target="_blank" style="display:block; margin-top:15px; color:#aaa; text-decoration:none; font-size:12px;">تحميل النسخة الأصلية 📥</a>
                    </div>

                    <script>
                        var tag = document.createElement('script');
                        tag.src = "https://www.youtube.com/iframe_api";
                        var firstScriptTag = document.getElementsByTagName('script')[0];
                        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

                        var player;
                        function onYouTubeIframeAPIReady() {
                            player = new YT.Player('youtube-audio', {
                                height: '0',
                                width: '0',
                                videoId: '{{ v_id }}',
                                playerVars: { 'autoplay': 1, 'loop': 1 },
                                events: { 'onReady': onPlayerReady }
                            });
                        }

                        function onPlayerReady(event) { event.target.playVideo(); document.getElementById('ctrlIcon').innerHTML = "⏸️"; }

                        function togglePlay() {
                            if (player.getPlayerState() == 1) {
                                player.pauseVideo();
                                document.getElementById('ctrlIcon').innerHTML = "▶️";
                            } else {
                                player.playVideo();
                                document.getElementById('ctrlIcon').innerHTML = "⏸️";
                            }
                        }

                        function applyEffect(type) {
                            if (type == 'speed') {
                                player.setPlaybackRate(1.25); // تسريع الأغنية للريمكس
                                alert("تم تفعيل وضع الريمكس السريع ⚡");
                            } else if (type == 'bass') {
                                // اليوتيوب لا يدعم Bass Boost مباشر برمجياً، فنقوم بتعلية الصوت لأقصى درجة
                                player.setVolume(100);
                                alert("تم تفعيل وضع الدبة (تأكد من رفع صوت سماعاتك) 🔊");
                            } else {
                                player.setPlaybackRate(1);
                                alert("العودة للوضع الطبيعي 🔄");
                            }
                        }
                    </script>
                {% endif %}
            </div>
            <p style="color:#333; font-size:10px; margin-top:20px;">حصرياً: أول موقع ريمكس فوري لـ يوسف</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

app = app
    
