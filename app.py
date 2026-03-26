from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # هنا هنحط روابط الأغاني اللي عندك
    songs = [
        {"name": "ريمكس الدبة - حصري", "url": "https://e.top4top.io/m_3737rddma9.mp3"},
        {"name": "توزيع كيمو الديب - جديد", "url": "https://l.top4top.io/m_3025u08un1.mp3"}, # مثال لملف تالت عندك
        {"name": "تراك سامر مدني", "url": "https://a.top4top.io/m_3025y9y9y1.mp3"} # مثال
    ]
    
    html_code = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yousef Music Player</title>
        <style>
            body { background: #000; color: #fff; font-family: sans-serif; text-align: center; margin: 0; padding: 20px; }
            .main-card { background: #111; border: 2px solid #0f0; border-radius: 30px; padding: 20px; max-width: 500px; margin: auto; box-shadow: 0 0 20px #0f03; }
            .logo { width: 80px; height: 80px; border: 2px solid #0f0; border-radius: 50%; margin-bottom: 15px; }
            h1 { color: #0f0; font-size: 24px; text-shadow: 0 0 10px #0f0; }
            
            /* ستايل قائمة الأغاني */
            .playlist { margin-top: 30px; text-align: right; }
            .song-item { 
                background: #222; margin: 10px 0; padding: 15px; border-radius: 15px; 
                cursor: pointer; transition: 0.3s; border-right: 5px solid #0f0;
                display: flex; justify-content: space-between; align-items: center;
            }
            .song-item:hover { background: #333; transform: scale(1.02); }
            .play-icon { color: #0f0; font-weight: bold; }

            .player-fixed { margin-top: 20px; background: #000; padding: 15px; border-radius: 20px; border: 1px dashed #0f0; }
            audio { width: 100%; }
        </style>
    </head>
    <body>
        <div class="main-card">
            <img src="https://cdn-icons-png.flaticon.com/512/3659/3659784.png" class="logo">
            <h1>Yousef Music Elite</h1>
            <p style="color: #888;">اختار الأغنية اللي عايز تسمعها</p>

            <div class="player-fixed">
                <audio id="mainPlayer" controls autoplay>
                    <source id="audioSource" src="{{ songs[0].url }}" type="audio/mpeg">
                </audio>
                <p id="nowPlaying" style="font-size: 12px; color: #0f0; margin-top: 10px;">شغال دلوقتي: {{ songs[0].name }}</p>
            </div>

            <div class="playlist">
                {% for song in songs %}
                <div class="song-item" onclick="playSong('{{ song.url }}', '{{ song.name }}')">
                    <span>{{ song.name }}</span>
                    <span class="play-icon">▶</span>
                </div>
                {% endfor %}
            </div>
        </div>

        <script>
            function playSong(url, name) {
                var audio = document.getElementById('mainPlayer');
                var source = document.getElementById('audioSource');
                var text = document.getElementById('nowPlaying');
                
                source.src = url;
                audio.load();
                audio.play();
                text.innerText = "شغال دلوقتي: " + name;
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_code, songs=songs)

if __name__ == '__main__':
    app.run()
    
