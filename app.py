import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# مفتاحك اللي شغال
API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ"

@app.route('/', methods=['GET', 'POST'])
def home():
    v_id = ""
    if request.method == 'POST':
        q = request.form.get('query')
        if q:
            try:
                url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={q}&type=video&key={API_KEY}&maxResults=1"
                res = requests.get(url).json()
                v_id = res['items'][0]['id']['videoId']
            except:
                v_id = ""

    return render_template_string('''
        <body style="background:#000; color:#1db954; text-align:center; font-family:sans-serif;">
            <div style="margin-top:50px; border:2px solid #1db954; display:inline-block; padding:20px; border-radius:15px;">
                <h1>🎸 محرك يوسف الموسيقي</h1>
                <form method="POST">
                    <input type="text" name="query" style="padding:10px; border-radius:5px;">
                    <button type="submit" style="padding:10px; background:#1db954; color:#000; border:none; border-radius:5px; font-weight:bold;">تشغيل</button>
                </form>
                {% if v_id %}
                    <div style="margin-top:20px;">
                        <iframe width="300" height="200" src="https://www.youtube.com/embed/{{ v_id }}" frameborder="0" allowfullscreen></iframe>
                    </div>
                {% endif %}
            </div>
        </body>
    ''', v_id=v_id)

# السطر ده مهم جداً لـ Vercel
# ماتكتبش حاجة تانية بعده
