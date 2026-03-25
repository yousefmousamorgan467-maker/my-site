from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sc_player = ""
    if request.method == 'POST':
        track_url = request.form.get('track_url')
        if track_url:
            # ده كود بيحول رابط ساوند كلاود لمشغل صوت شيك
            sc_player = f"""
            <div style='margin-top:20px;'>
                <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" 
                src="https://w.soundcloud.com/player/?url={track_url}&color=%231db954&auto_play=true&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false">
                </iframe>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Sound Player</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #121212; color: white; text-align: center; font-family: sans-serif; padding: 20px; }}
                .box {{ background: #181818; padding: 25px; border-radius: 20px; max-width: 400px; margin: auto; }}
                input {{ width: 100%; padding: 12px; border-radius: 20px; border: 1px solid #333; background: #222; color: white; margin-bottom: 10px; }}
                button {{ width: 100%; padding: 10px; border-radius: 20px; border: none; background: #1db954; font-weight: bold; cursor: pointer; }}
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🎧 Yousef Music Box</h1>
                <p style="font-size: 14px; color: #888;">انسخ رابط الأغنية من SoundCloud وحطه هنا:</p>
                <form method="POST">
                    <input type="text" name="track_url" placeholder="https://soundcloud.com/..." required>
                    <button type="submit">تشغيل الآن</button>
                </form>
                {sc_player}
            </div>
        </body>
    </html>
    """)
    
