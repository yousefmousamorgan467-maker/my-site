from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    audio_player = ""
    if request.method == 'POST':
        song_name = request.form.get('song_name')
        if song_name:
            # ده رابط لمحرك بحث بيحول اسم الأغنية لرابط صوتي مباشر
            # ملحوظة: لو الأغنية مجاتش، جرب تكتب اسم الفنان مع الأغنية
            search_query = song_name.replace(" ", "+")
            audio_player = f"""
            <div style='margin-top:30px;'>
                <p style='color:#1db954;'>جاري تشغيل: <b>{song_name}</b></p>
                <audio controls autoplay style='width:100%;'>
                    <source src="https://api.deezer.com/search?q={search_query}" type="audio/mpeg">
                    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
                    متصفحك لا يدعم المشغل.
                </audio>
                <p style='font-size:10px; color:#555; margin-top:10px;'>إذا لم تعمل الأغنية، قد يكون الرابط تحت الصيانة.</p>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Music Box</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #000; color: white; text-align: center; font-family: sans-serif; padding: 20px; }}
                .main-card {{ background: #121212; padding: 30px; border-radius: 25px; border: 1px solid #282828; max-width: 400px; margin: auto; }}
                input {{ width: 100%; padding: 15px; border-radius: 30px; border: none; background: #282828; color: white; margin-bottom: 15px; text-align: center; }}
                button {{ width: 100%; padding: 12px; border-radius: 30px; border: none; background: #1db954; color: black; font-weight: bold; font-size: 16px; cursor: pointer; }}
                h1 {{ font-size: 24px; color: #1db954; }}
            </style>
        </head>
        <body>
            <div class="main-card">
                <h1>🎸 Yousef Music Box</h1>
                <form method="POST">
                    <input type="text" name="song_name" placeholder="اكتب اسم الأغنية.." required>
                    <button type="submit">بحث وتشغيل</button>
                </form>
                {audio_player}
            </div>
        </body>
    </html>
    """)
    
