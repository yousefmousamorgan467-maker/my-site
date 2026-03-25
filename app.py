from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    results_html = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # ده المحرك اللي بيعرض نتائج البحث جوه موقعك مباشرة
            results_html = f'''
            <div style="margin-top:20px; border-radius:15px; overflow:hidden; border:2px solid #1db954;">
                <iframe width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" 
                    src="https://w.soundcloud.com/player/?url=https://soundcloud.com/search?q={query}&color=%231db954&auto_play=false&show_teaser=false&visual=false">
                </iframe>
            </div>
            '''

    return render_template_string(f'''
    <html>
        <head>
            <title>Yousef Music Search</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #000; color: white; text-align: center; font-family: sans-serif; padding: 15px; }}
                .main-card {{ 
                    background: #111; padding: 25px; border-radius: 20px; 
                    box-shadow: 0 0 15px #1db954; max-width: 450px; margin: auto; 
                }}
                input {{ 
                    width: 100%; padding: 15px; border-radius: 30px; border: 1px solid #333; 
                    background: #1e1e1e; color: white; margin-bottom: 15px; text-align: center; outline: none;
                }}
                button {{ 
                    width: 100%; padding: 12px; border-radius: 30px; border: none; 
                    background: #1db954; color: black; font-weight: bold; cursor: pointer;
                }}
                h1 {{ color: #1db954; font-size: 24px; }}
            </style>
        </head>
        <body>
            <div class="main-card">
                <h1>🎸 Yousef Search Engine</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم أي أغنية..." required>
                    <button type="submit">ابحث واسمع فوراً</button>
                </form>
                {results_html}
            </div>
            <p style="font-size:10px; color:#444; margin-top:20px;">تطوير يوسف - تالتة ثانوي 🚀</p>
        </body>
    </html>
    ''')
    
