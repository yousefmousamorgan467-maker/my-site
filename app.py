from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    audio_player = ""
    if request.method == 'POST':
        song_name = request.form.get('song_name')
        if song_name:
            # استخدام محرك بحث صوتي مفتوح (مثال للتوضيح)
            # هنا بنوجه المشغل ليدور في مكتبة صوتية
            audio_player = f"""
            <div style='margin-top:30px;'>
                <p style='color:#1db954;'>تشغيل الآن: <b>{song_name}</b></p>
                <audio controls autoplay style='width:100%;'>
                    <source src="https://musicapi.rocks/search?q={song_name}" type="audio/mpeg">
                    متصفحك لا يدعم مشغل الصوت.
                </audio>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Music Player</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ 
                    background: #000; color: white; text-align: center; 
                    font-family: 'Segoe UI', sans-serif; padding: 20px; 
                }}
                .main-card {{
                    background: #121212; padding: 30px; border-radius: 20px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.8);
                    max-width: 450px; margin: auto;
                }}
                input[type="text"] {{
                    width: 90%; padding: 15px; border-radius: 30px; border: 1px solid #333;
                    background: #282828; color: white; margin-bottom: 15px; outline: none;
                }}
                button {{
                    padding: 12px 35px; border-radius: 30px; border: none;
                    background: #1db954; color: black; font-weight: bold; cursor: pointer;
                }}
                h1 {{ font-size: 28px; margin-bottom: 25px; color: white; }}
            </style>
        </head>
        <body>
            <div class="main-card">
                <h1>🎸 Music Box</h1>
                <form method="POST">
                    <input type="text" name="song_name" placeholder="ابحث عن أغنية أو فنان..." required>
                    <br>
                    <button type="submit">تشغيل</button>
                </form>
                {audio_player}
            </div>
            <p style="margin-top:30px; font-size:12px; color:#555;">Made by Yousef for Music Lovers</p>
        </body>
    </html>
    """)
    
