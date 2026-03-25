from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# مفتاحك يا يوسف
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
        <body style="background:#000; color:#1db954; text-align:center; font-family:sans-serif; padding-top:50px;">
            <div style="border:2px solid #1db954; display:inline-block; padding:30px; border-radius:20px; background:#111;">
                <h1>🎸 Yousef Player</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اسم الأغنية..." style="padding:10px; border-radius:10px;">
                    <button type="submit" style="padding:10px; background:#1db954; color:#000; font-weight:bold; border-radius:10px;">تشغيل</button>
                </form>
                {% if v_id and v_id != "error" %}
                    <div style="margin-top:20px;">
                        <iframe width="100%" height="200" src="https://www.youtube.com/embed/{{ v_id }}" frameborder="0" allowfullscreen></iframe>
                    </div>
                {% endif %}
            </div>
        </body>
    ''', v_id=v_id)

# السطر ده هو السر لـ Vercel
# بيعرفه إن ده التطبيق اللي هيشغله
app = app
