from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    player_html = ""
    if request.method == 'POST':
        song_name = request.form.get('song_name')
        if song_name:
            # هنا بنستخدم مشغل يوتيوب بس بنصغر حجمه جداً ونخفي الفيديو
            player_html = f"""
            <div style='margin-top:20px; background:#282828; padding:15px; border-radius:15px;'>
                <p style='color:#1db954;'>جاري تشغيل: <b>{song_name}</b></p>
                <div style="width: 100%; height: 80px; overflow: hidden; border-radius: 10px;">
                    <iframe 
                        width="100%" 
                        height="300" 
                        src="https://www.youtube.com/embed?listType=search&list={song_name}&autoplay=1" 
                        frameborder="0" 
                        style="margin-top: -150px;" 
                        allow="autoplay">
                    </iframe>
                </div>
                <p style="font-size:10px; color:#888; margin-top:10px;">المشغل يعمل بنظام "صوت اليوتيوب" المباشر</p>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef's Ultimate Player</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #121212; color: white; text-align: center; font-family: sans-serif; padding: 20px; }}
                .container {{ max-width: 400px; margin: auto; background: #181818; padding: 25px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
                input {{ width: 100%; padding: 15px; border-radius: 25px; border: none; background: #333; color: white; margin-bottom: 15px; outline: none; }}
                button {{ width: 100%; padding: 12px; border-radius: 25px; border: none; background: #1db954; color: black; font-weight: bold; cursor: pointer; }}
                h1 {{ color: #1db954; font-size: 22px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🔍 محرك بحث يوسف للموسيقى</h1>
                <form method="POST">
                    <input type="text" name="song_name" placeholder="اكتب اسم الأغنية هنا..." required>
                    <button type="submit">بحث وتشغيل</button>
                </form>
                {player_html}
            </div>
        </body>
    </html>
    """)
    
