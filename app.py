from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    search_html = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            # هنا بنعمل "تضمين" لنتائج البحث جوه برواز (Frame) داخلي عشان م تطلعش بره الموقع
            search_html = f"""
            <div style="margin-top:20px; border:2px solid #1db954; border-radius:15px; overflow:hidden;">
                <iframe src="https://m.youtube.com/results?search_query={query}" 
                        style="width:100%; height:500px; border:none;">
                </iframe>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Private Station</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ background: #000; color: white; text-align: center; font-family: sans-serif; padding: 15px; }}
                .main-box {{ background: #111; padding: 20px; border-radius: 20px; box-shadow: 0 0 20px #1db954; }}
                input {{ width: 85%; padding: 12px; border-radius: 25px; border: 1px solid #1db954; background: #222; color: white; outline: none; }}
                button {{ margin-top: 10px; width: 50%; padding: 10px; border-radius: 25px; border: none; background: #1db954; color: black; font-weight: bold; }}
                h1 {{ font-size: 22px; color: #1db954; }}
            </style>
        </head>
        <body>
            <div class="main-box">
                <h1>🎵 محطتي الخاصة - يوسف</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية هنا..." required>
                    <button type="submit">ابحث واسمع هنا</button>
                </form>
                {search_html}
            </div>
            <p style="font-size:10px; color:#555; margin-top:15px;">كل النتائج تظهر داخل موقعك الخاص</p>
        </body>
    </html>
    """)
    
