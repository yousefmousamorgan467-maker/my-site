from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ"

@app.route('/', methods=['GET', 'POST'])
def index():
    v_id = None
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            try:
                url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}&maxResults=1"
                res = requests.get(url).json()
                v_id = res['items'][0]['id']['videoId']
            except:
                v_id = "error"
    
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="ar">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Yousef Audio Player</title>
        </head>
        <body style="background:#000; color:#1db954; text-align:center; font-family:sans-serif; padding-top:100px;">
            <div style="border:2px solid #1db954; display:inline-block; padding:40px; border-radius:30px; background:#111; box-shadow: 0 0 30px #1db954;">
                <h1 style="font-size:35px; margin-bottom:10px;">📻 يوسف ميوزك</h1>
                <p style="color:#888; margin-bottom:30px;">وضع "الصوت فقط" مفعل ✅</p>
                
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية..." 
                           style="padding:15px; border-radius:25px; border:none; width:250px; text-align:center; outline:none; background:#222; color:#fff;">
                    <br><br>
                    <button type="submit" style="padding:12px 30px; background:#1db954; color:#000; font-weight:bold; border:none; border-radius:25px; cursor:pointer; font-size:18px;">
                        استماع الآن 🎵
                    </button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:30px;">
                        <p style="color:#1db954; font-weight:bold;">جاري التشغيل في الخلفية...</p>
                        <iframe width="1" height="1" 
                                src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" 
                                frameborder="0" allow="autoplay">
                        </iframe>
                        <div style="margin-top:10px;">
                            <button onclick="location.reload()" style="background:red; color:white; border:none; padding:5px 15px; border-radius:15px; cursor:pointer;">إيقاف الصوت ⏹️</button>
                        </div>
                    </div>
                {% endif %}
            </div>
            <p style="color:#333; margin-top:50px;">تطوير يوسف - ثانوية عامة 🎓</p>
        </body>
        </html>
    ''', v_id=v_id)

app = app
    
