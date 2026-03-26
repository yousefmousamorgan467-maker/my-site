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
            <title>Yousef Music | Pro Edition</title>
            <style>
                body { 
                    margin: 0; height: 100vh; display: flex; align-items: center; justify-content: center;
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
                    background-size: 400% 400%; animation: gradient 10s ease infinite; color: #fff;
                }
                @keyframes gradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }

                .player-card {
                    background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);
                    padding: 35px; border-radius: 50px; width: 85%; max-width: 400px;
                    text-align: center; border: 1px solid rgba(255, 255, 255, 0.1);
                    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
                }

                input[type="text"] { 
                    width: 85%; padding: 15px; border-radius: 30px; border: none; 
                    background: rgba(0,0,0,0.3); color: #fff; margin-bottom: 20px;
                    text-align: center; border: 1px solid rgba(255,255,255,0.1);
                }

                .btn-search { 
                    width: 95%; padding: 12px; background: #ff0050; color: #fff; 
                    border: none; border-radius: 30px; font-weight: bold; cursor: pointer;
                    box-shadow: 0 5px 15px rgba(255, 0, 80, 0.4);
                }

                /* زر التشغيل الدائري */
                .ctrl-btn {
                    width: 70px; height: 70px; background: #fff; color: #000;
                    border-radius: 50%; display: flex; align-items: center; justify-content: center;
                    margin: 25px auto; cursor: pointer; font-size: 30px; transition: 0.3s;
                    box-shadow: 0 0 20px rgba(255,255,255,0.3);
                }
                .ctrl-btn:active { transform: scale(0.9); }

                /* شريط التقديم الأنيق */
                .seek-container { margin-top: 20px; }
                input[type="range"] {
                    -webkit-appearance: none; width: 100%; background: rgba(255,255,255,0.1);
                    height: 6px; border-radius: 5px; outline: none;
                }
                input[type="range"]::-webkit-slider-thumb {
                    -webkit-appearance: none; width: 15px; height: 15px;
                    background: #ff0050; border-radius: 50%; cursor: pointer;
                    box-shadow: 0 0 10px #ff0050;
                }

                .time-box { display: flex; justify-content: space-between; font-size: 11px; margin-top: 8px; color: #bbb; }
                .track-title { font-size: 16px; margin: 15px 0; color: #0f0; text-shadow: 0 0 5px #0f0; }
                #yt-player { display: none; }
            </style>
        </head>
        <body>
            <div class="player-card">
                <h2 style="letter-spacing: 2px;">YOUSEF MUSIC</h2>
                <form method="POST">
                    <input type="text" name="query" placeholder="ابحث عن تراك أو أغنية..." required>
                    <button type="submit" class="btn-search">تشغيل الآن ⚡</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div class="track-title">{{ title }}</div>
                    <div id="yt-player"></div>

                    <div class="ctrl-btn" id="playBtn" onclick="togglePlay()">⏸</div>

                    <div class="seek-container">
                        <input type="range" id="seek-bar" value="0" step="1">
                        <div class="time-box">
                            <span id="curr-time">0:00</span>
                            <span id="dur-time">0:00</span>
                        </div>
                    </div>

                    <script>
                        var tag = document.createElement('script');
                        tag.src = "https://www.youtube.com/iframe_api";
                        var firstScriptTag = document.getElementsByTagName('script')[0];
                        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

                        var player;
                        var sBar = document.getElementById('seek-bar');

                        function onYouTubeIframeAPIReady() {
                            player = new YT.Player('yt-player', {
                                height: '0', width: '0', videoId: '{{ v_id }}',
                                playerVars: { 'autoplay': 1, 'controls': 0 },
                                events: { 'onReady': onPlayerReady }
                            });
                        }

                        function onPlayerReady() {
                            setInterval(syncPlayer, 1000);
                        }

                        function togglePlay() {
                            if (player.getPlayerState() == 1) {
                                player.pauseVideo();
                                document.getElementById('playBtn').innerHTML = "▶";
                            } else {
                                player.playVideo();
                                document.getElementById('playBtn').innerHTML = "⏸";
                            }
                        }

                        function syncPlayer() {
                            if (player && player.getCurrentTime) {
                                var c = player.getCurrentTime();
                                var d = player.getDuration();
                                sBar.max = d;
                                sBar.value = c;
                                document.getElementById('curr-time').innerHTML = fmt(c);
                                document.getElementById('dur-time').innerHTML = fmt(d);
                            }
                        }

                        sBar.oninput = function() { player.seekTo(sBar.value); };

                        function fmt(s) {
                            var m = Math.floor(s / 60);
                            var sc = Math.floor(s % 60);
                            return m + ":" + (sc < 10 ? '0' : '') + sc;
                        }
                    </script>
                {% endif %}
            </div>
        </body>
        </html>
    ''', v_id=v_id, title=title)

if __name__ == '__main__':
    app.run()
    
