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
            <title>Yousef Music | Animated Edition</title>
            <style>
                /* خلفية بألوان متحركة */
                body { 
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                    background-size: 400% 400%;
                    animation: gradient 15s ease infinite;
                    color: #fff;
                    overflow: hidden;
                }

                @keyframes gradient {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }

                .player-card {
                    background: rgba(0, 0, 0, 0.6);
                    backdrop-filter: blur(15px);
                    padding: 30px;
                    border-radius: 40px;
                    width: 85%;
                    max-width: 400px;
                    text-align: center;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
                }

                input { 
                    width: 80%; padding: 12px; border-radius: 25px; border: none; 
                    background: rgba(255,255,255,0.1); color: #fff; 
                    margin-bottom: 15px; text-align: center; outline: none;
                    border: 1px solid rgba(255,255,255,0.2);
                }

                .btn-search { 
                    width: 90%; padding: 12px; background: #fff; color: #000; 
                    border: none; border-radius: 25px; font-weight: bold; cursor: pointer; 
                }

                /* شريط التقديم المخصص */
                .audio-controls { margin-top: 25px; }
                #seek-bar { width: 100%; cursor: pointer; accent-color: #e73c7e; }
                
                .time-info { display: flex; justify-content: space-between; font-size: 12px; margin-top: 5px; }
                
                .play-btn { font-size: 50px; cursor: pointer; margin: 20px 0; display: inline-block; transition: 0.3s; }
                .play-btn:hover { transform: scale(1.1); }

                /* إخفاء فيديو يوتيوب تماماً */
                #yt-player { display: none; }
                
                .track-name { font-size: 18px; font-weight: bold; margin-bottom: 10px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
            </style>
        </head>
        <body>
            <div class="player-card">
                <h1>🎧 Yousef Music</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="ابحث عن أغنية..." required>
                    <button type="submit" class="btn-search">تشغيل 🚀</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div class="audio-controls">
                        <div class="track-name">{{ title }}</div>
                        
                        <div id="yt-player"></div>

                        <div class="play-btn" id="playIcon" onclick="togglePlay()">⏸️</div>
                        
                        <input type="range" id="seek-bar" value="0" step="1">
                        <div class="time-info">
                            <span id="current-time">0:00</span>
                            <span id="duration">0:00</span>
                        </div>
                    </div>

                    <script>
                        var tag = document.createElement('script');
                        tag.src = "https://www.youtube.com/iframe_api";
                        var firstScriptTag = document.getElementsByTagName('script')[0];
                        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

                        var player;
                        var seekBar = document.getElementById('seek-bar');

                        function onYouTubeIframeAPIReady() {
                            player = new YT.Player('yt-player', {
                                height: '0', width: '0',
                                videoId: '{{ v_id }}',
                                playerVars: { 'autoplay': 1, 'controls': 0 },
                                events: { 'onReady': onPlayerReady }
                            });
                        }

                        function onPlayerReady(event) {
                            updateTimer();
                            setInterval(updateTimer, 1000);
                        }

                        function togglePlay() {
                            if (player.getPlayerState() == 1) {
                                player.pauseVideo();
                                document.getElementById('playIcon').innerHTML = "▶️";
                            } else {
                                player.playVideo();
                                document.getElementById('playIcon').innerHTML = "⏸️";
                            }
                        }

                        function updateTimer() {
                            if (player && player.getCurrentTime) {
                                var curr = player.getCurrentTime();
                                var dur = player.getDuration();
                                seekBar.max = dur;
                                seekBar.value = curr;
                                
                                document.getElementById('current-time').innerHTML = formatTime(curr);
                                document.getElementById('duration').innerHTML = formatTime(dur);
                            }
                        }

                        seekBar.oninput = function() {
                            player.seekTo(seekBar.value);
                        };

                        function formatTime(time) {
                            var min = Math.floor(time / 60);
                            var sec = Math.floor(time % 60);
                            return min + ":" + (sec < 10 ? '0' : '') + sec;
                        }
                    </script>
                {% endif %}
            </div>
        </body>
        </html>
    ''', v_id=v_id, title=title)

if __name__ == '__main__':
    app.run()
                
