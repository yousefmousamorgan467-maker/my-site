from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    audio_player = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # ده "محرك بحث وتحويل" بيطلع رابط MP3 مباشر
            # بنستخدمه كـ iframe عشان هو اللي بيتولي عملية التحويل والتشغيل
            audio_player = f"""
            <div style='margin-top:20px; border-radius:15px; overflow:hidden; border:2px solid #1db954;'>
                <iframe 
                    src="https://tomp3.cc/api/search?q={query}" 
                    style="width:100%; height:400px; border:none;"
                    scrolling="yes">
                </iframe>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Music Station</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #000; color: white; text-align: center; font-family: sans-serif; padding: 15px; }}
                .main-card {{ background: #111; padding: 25px; border-radius: 20px; box-shadow: 0 0 15px #1db954; max-width: 450px; margin: auto; }}
                input {{ width: 100%; padding: 15px; border-radius: 30px; border: none; background: #222; color: white; margin-bottom: 15px; text-align: center; }}
                button {{ width: 100%; padding: 12px; border-radius: 30px; border: none; background: #1db954; color: black; font-weight: bold; cursor: pointer; }}
                h1 {{ color: #1db954; font-size: 22px; }}
            </style>
        </head>
        <body>
            <div class="main-card">
                <h1>🎸 محرك بحث يوسف الحقيقي</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية أو الفنان..." required>
                    <button type="submit">بحث وتشغيل فوراً</button>
                </form>
                {audio_player}
            </div>
            <p style="font-size:10px; color:#444; margin-top:20px;">تطوير يوسف - مبرمج تالتة ثانوي 🚀</p>
        </body>
    </html>
    """)
    
