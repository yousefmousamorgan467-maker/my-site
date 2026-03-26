from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# مفتاح الـ API اللي تعبنا فيه
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
                .container { max-width: 500px; margin: auto; background: #111; padding: 20px; border-radius: 25px; border: 1px solid #ff0050; box-shadow: 0 0 20px rgba(255, 0, 80, 0.2); }
                h1 { color: #ff0050; text-shadow: 0 0 10px #ff0050; }
                input { width: 85%; padding: 12px; border-radius: 20px; border: none; background: #222; color: #fff; margin-bottom: 15px; text-align: center; font-size: 16px; border: 1px solid #333; }
                .btn-main { width: 95%; padding: 12px; background: #ff0050; color: #fff; border: none; border-radius: 20px; font-weight: bold; cursor: pointer; font-size: 16px; }
                
                /* صندوق المشغل وشريط التقديم */
                .custom-player { background: #1a1a1a; padding: 15px; border-radius: 20px; margin-top: 20px; border: 1px solid #333; }
                #yt-wrapper { margin-top: 10px; border-radius: 15px; overflow: hidden; background: #000; }
                
                .remix-panel { margin-top: 20px; display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
                .side-btn { background: #222; color: #0f0; border: 1px solid #0f0; padding: 10px 15px; border-radius: 15px; font-size: 13px; cursor: pointer; flex: 1; min-width: 100px; }
                .play-pause { font-size: 40px; cursor: pointer; color: #ff0050; margin: 15px 0; }
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
                        <h3 id="trackTitle" style="font-size: 16px; color: #eee;">{{ title }}</h3>
                        
                        <div id="yt-wrapper">
                            <div id="youtube-audio"></div>
                        </div>

                        <div class="play-pause" id="ctrlIcon" onclick="togglePlay()">⏸️</div>
                        
                        <div class="remix-panel">
                            <button class="side-btn" onclick="applyEffect('speed')">⚡ ريمكس سريع</button>
                            <button class="side-btn" onclick="applyEffect('bass')">🔊 دبة عالية</button>
                            <button class="side-btn" onclick="applyEffect('normal')">🔄 طبيعي</button>
                        </div>

                        <a href="https://loader.to/api/button/?url=https://www.youtube.com/watch?v={{ v_id }}&f=mp3" target="_blank" style="display:block; margin-top:20px; color:#666; text-decoration:none; font-size:12px;">تحميل النسخة الأصلية 📥</a>
                    </div>

                    <script>
                        var tag = document.createElement('script');
                        tag.src = "https://www.youtube.com/iframe_api";
                        var firstScriptTag = document.getElementsByTagName('script')[0];
                        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

                        var player;
                        function onYouTubeIframeAPIReady() {
                            player = new YT.Player('youtube-audio', {
                                height: '60', // كدة الشريط هيظهر
                                width: '100%',
                                videoId: '{{ v_id }}',
                                playerVars: { 'autoplay': 1, 'controls': 1, 'modestbranding': 1 },
                                events: { 'onReady': onPlayerReady }
                            });
                        }

                        function onPlayerReady(event) { event.target.playVideo(); }

                        function togglePlay() {
                            var state = player.getPlayerState();
                            if (state == 1) {
                                player.pauseVideo();
                                document.getElementById('ctrlIcon').innerHTML = "▶️";
                            } else {
                                player.playVideo();
                                document.getElementById('ctrlIcon').innerHTML = "⏸️";
                            }
                        }

                        function applyEffect(type) {
                            if (type == 'speed') {
                                player.setPlaybackRate(1.25);
                                alert("وضع الريمكس السريع شغال ⚡");
                            } else if (type == 'bass') {
                                player.setVolume(100);
                                alert("تم رفع الصوت للأقصى (وضع الدبة) 🔊");
                            } else {
                                player.setPlaybackRate(1);
                                alert("رجعت طبيعي 🔄");
                            }
                        }
                    </script>
                {% endif %}
            </div>
            <p style="color:#222; font-size:10px; margin-top:20px;">حصرياً لـ يوسف - مبرمج المستقبل</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

if __name__ == '__main__':
    app.run()
                    
