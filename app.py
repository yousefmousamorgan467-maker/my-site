from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    player_html = ""
    if request.method == 'POST':
        search_query = request.form.get('query')
        if search_query:
            # بنستخدم محرك بحث ساوند كلاود المباشر داخل الموقع
            player_html = f"""
            <div style='margin-top:20px;'>
                <iframe width="100%" height="400" scrolling="no" frameborder="no" allow="autoplay" 
                src="https://w.soundcloud.com/player/?url=https://soundcloud.com/search?q={search_query}&auto_play=true">
                </iframe>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Fast Music</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #121212; color: white; text-align: center; font-family: sans-serif; padding: 20px; }}
                .container {{ max-width: 400px; margin: auto; background: #181818; padding: 20px; border-radius: 20px; box-shadow: 0 5px 20px rgba(0,0,0,0.5); }}
                input {{ width: 100%; padding: 12px; border-radius: 25px; border: none; background: #333; color: white; margin-bottom: 15px; text-align: center; }}
                button {{ width: 100%; padding: 12px; border-radius: 25px; border: none; background: #ff5500; color: white; font-weight: bold; cursor: pointer; }}
                h1 {{ color: #ff5500; font-size: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🧡 Yousef Fast Player</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية هنا.." required>
                    <button type="submit">بحث وتشغيل سريع</button>
                </form>
                {player_html}
            </div>
        </body>
    </html>
    """)
    
