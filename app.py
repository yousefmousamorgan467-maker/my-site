from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    search_results = ""
    if request.method == 'POST':
        song_name = request.form.get('song_name')
        if song_name:
            # هنا بنعمل رابط بحث مباشر على يوتيوب ميوزيك عشان يظهر للمستخدم
            search_results = f"""
            <div style='margin-top:20px;'>
                <p>نتائج البحث عن: <b>{song_name}</b></p>
                <iframe width="100%" height="300" 
                    src="https://www.youtube.com/embed?listType=search&list={song_name}" 
                    frameborder="0" allowfullscreen>
                </iframe>
            </div>
            """

    return render_template_string(f"""
    <html>
        <head>
            <title>Yousef Search Music</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ 
                    background: #121212; color: white; text-align: center; 
                    font-family: sans-serif; padding: 20px; margin: 0;
                }}
                .search-box {{
                    background: #1e1e1e; padding: 20px; border-radius: 15px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
                }}
                input[type="text"] {{
                    width: 80%; padding: 12px; border-radius: 25px; border: none;
                    margin-bottom: 10px; outline: none;
                }}
                button {{
                    padding: 10px 25px; border-radius: 25px; border: none;
                    background: #1db954; color: white; font-weight: bold; cursor: pointer;
                }}
                h1 {{ color: #1db954; }}
            </style>
        </head>
        <body>
            <div class="search-box">
                <h1>🔍 Yousef Music Search</h1>
                <form method="POST">
                    <input type="text" name="song_name" placeholder="اكتب اسم الأغنية هنا..." required>
                    <br>
                    <button type="submit">بحث</button>
                </form>
                {search_results}
            </div>
            <p style="margin-top:20px; font-size:12px; color:#666;">البحث مدعوم بواسطة YouTube</p>
        </body>
    </html>
    """)
    
