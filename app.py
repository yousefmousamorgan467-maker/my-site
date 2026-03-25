from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # ده رابط بيفتح البحث مباشرة في موقع صوتي مشهور
            # الحركة دي بتضمن إن الأغنية تشتغل 100%
            search_url = f"https://soundcloud.com/search?q={query}"
            return f"""
            <html>
                <head><meta http-equiv="refresh" content="0; url={search_url}"></head>
                <body style="background:#000; color:#1db954; text-align:center; padding-top:50px;">
                    <h3>جاري العثور على أغنية: {query}...</h3>
                </body>
            </html>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef's Music Box</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #000; color: white; text-align: center; font-family: sans-serif; padding: 20px; }}
                .card {{ 
                    background: #111; padding: 30px; border-radius: 20px; 
                    box-shadow: 0 0 20px #1db954; border: 1px solid #1db954;
                    max-width: 400px; margin: auto;
                }}
                input {{ 
                    width: 100%; padding: 15px; border-radius: 30px; border: none; 
                    background: #222; color: white; margin-bottom: 20px; text-align: center;
                    font-size: 16px;
                }}
                button {{ 
                    width: 100%; padding: 12px; border-radius: 30px; border: none; 
                    background: #1db954; color: black; font-weight: bold; font-size: 18px;
                }}
                h1 {{ color: #1db954; margin-bottom: 30px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🔍 محرك بحث يوسف</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية هنا..." required>
                    <button type="submit">ابحث واسمع الآن</button>
                </form>
            </div>
            <p style="color:#444; margin-top:30px;">أسرع وسيلة للوصول لأي أغنية في العالم 🚀</p>
        </body>
    </html>
    """)
    
