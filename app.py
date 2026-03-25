from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    audio_player = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # هنا بنستخدم رابط سحري بيحول البحث لملف صوتي مباشر
            # الرابط ده بيعتمد على مكتبة أغانى عامة
            audio_source = f"https://api.vevioz.com/api/button/mp3/{query}"
            
            audio_player = f"""
            <div style='margin-top:30px; background:#222; padding:20px; border-radius:15px; border:1px solid #1db954;'>
                <p style='color:#1db954; margin-bottom:15px;'>🎶 جاري محاولة تشغيل: <b>{query}</b></p>
                <iframe src="{audio_source}" 
                        style="width:100%; height:60px; border:none; overflow:hidden;" 
                        scrolling="no">
                </iframe>
                <p style='font-size:11px; color:#666; margin-top:10px;'>ملاحظة: إذا لم يظهر المشغل، جرب كتابة اسم الفنان بدقة.</p>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Pro Player</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #000; color: white; text-align: center; font-family: sans-serif; padding: 20px; }}
                .container {{ max-width: 400px; margin: auto; }}
                .search-card {{ background: #111; padding: 25px; border-radius: 20px; border: 1px solid #333; }}
                input {{ width: 100%; padding: 15px; border-radius: 30px; border: none; background: #282828; color: white; margin-bottom: 15px; text-align: center; }}
                button {{ width: 100%; padding: 12px; border-radius: 30px; border: none; background: #1db954; color: black; font-weight: bold; cursor: pointer; }}
                h1 {{ font-size: 24px; color: #1db954; margin-bottom: 25px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="search-card">
                    <h1>🎸 Yousef Music Box</h1>
                    <form method="POST">
                        <input type="text" name="query" placeholder="اكتب اسم الأغنية..." required>
                        <button type="submit">تشغيل داخل الموقع</button>
                    </form>
                    {audio_player}
                </div>
            </div>
        </body>
    </html>
    """)
            
