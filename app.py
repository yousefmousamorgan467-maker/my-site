from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    player_html = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # استخدام محرك بحث بيحول الاسم لرابط تشغيل صوتي/مرئي مستقر
            # ده كود بيجيب أول نتيجة بحث من يوتيوب ويشغلها في "برواز" محمي
            player_html = f'''
            <div style="margin-top:20px; border-radius:15px; overflow:hidden; border:2px solid #1db954;">
                <iframe 
                    width="100%" 
                    height="250" 
                    src="https://www.youtube-nocookie.com/embed?listType=search&list={query}" 
                    frameborder="0" 
                    allow="autoplay; encrypted-media" 
                    allowfullscreen>
                </iframe>
            </div>
            '''

    return render_template_string(f'''
    <html>
        <head>
            <title>Yousef Ultimate Music</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #000; color: white; text-align: center; font-family: sans-serif; padding: 15px; }}
                .card {{ background: #111; padding: 25px; border-radius: 20px; box-shadow: 0 0 20px #1db954; max-width: 450px; margin: auto; }}
                input {{ width: 100%; padding: 15px; border-radius: 30px; border: none; background: #222; color: white; margin-bottom: 15px; text-align: center; }}
                button {{ width: 100%; padding: 12px; border-radius: 30px; border: none; background: #1db954; color: black; font-weight: bold; cursor: pointer; }}
                h1 {{ color: #1db954; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎸 محرك يوسف الموسيقي</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية هنا..." required>
                    <button type="submit">تشغيل فوري</button>
                </form>
                {player_html}
            </div>
            <p style="font-size:10px; color:#444; margin-top:20px;">تطوير يوسف - تالتة ثانوي 🚀</p>
        </body>
    </html>
    ''')
    
