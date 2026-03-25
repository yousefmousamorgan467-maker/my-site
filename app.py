from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    sc_player = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # ده الرابط السحري اللي بيجيب نتائج ساوند كلاود جوه صفحتك
            sc_player = f"""
            <div style='margin-top:20px; border-radius:15px; overflow:hidden; border:1px solid #1db954;'>
                <iframe width="100%" height="400" scrolling="no" frameborder="no" allow="autoplay" 
                    src="https://w.soundcloud.com/player/?url=https://soundcloud.com/search?q={query}&color=%231db954&auto_play=true&show_teaser=false">
                </iframe>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Ultimate Player</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #0b0b0b; color: white; text-align: center; font-family: sans-serif; padding: 15px; }}
                .main-card {{ 
                    background: #121212; padding: 25px; border-radius: 25px; 
                    box-shadow: 0 0 15px rgba(29, 185, 84, 0.3); max-width: 450px; margin: auto; 
                }}
                input {{ 
                    width: 100%; padding: 15px; border-radius: 30px; border: 1px solid #333; 
                    background: #1e1e1e; color: white; margin-bottom: 15px; text-align: center; outline: none;
                }}
                button {{ 
                    width: 100%; padding: 12px; border-radius: 30px; border: none; 
                    background: #1db954; color: black; font-weight: bold; font-size: 16px; cursor: pointer;
                }}
                h1 {{ color: #1db954; font-size: 24px; margin-bottom: 20px; }}
            </style>
        </head>
        <body>
            <div class="main-card">
                <h1>🎸 Yousef Music Box</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="ابحث عن أي أغنية في العالم..." required>
                    <button type="submit">تشغيل فوري داخل الموقع</button>
                </form>
                {sc_player}
            </div>
            <p style="font-size:10px; color:#444; margin-top:20px;">تطوير يوسف - تالتة ثانوي 🚀</p>
        </body>
    </html>
    """)
    
