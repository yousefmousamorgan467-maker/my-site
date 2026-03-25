import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# مفتاحك اللي بعتهولي في الرسالة اللي فاتت
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
                if "items" in res and res["items"]:
                    v_id = res["items"][0]["id"]["videoId"]
            except:
                pass

    return render_template_string('''
        <body style="background:#000; color:#fff; text-align:center; font-family:sans-serif; padding:20px;">
            <div style="border:2px solid #1db954; border-radius:25px; padding:25px; max-width:420px; margin:auto; background:#111; box-shadow: 0 0 20px #1db954;">
                <h1 style="color:#1db954;">🎸 محرك يوسف الموسيقي</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية هنا..." style="width:100%; padding:15px; border-radius:25px; border:none; margin-bottom:15px; text-align:center; background:#222; color:#fff;">
                    <button type="submit" style="width:100%; padding:12px; border-radius:25px; border:none; background:#1db954; color:#000; font-weight:bold; cursor:pointer;">تشغيل فوري 🚀</button>
                </form>
                {% if v_id %}
                    <div style="margin-top:20px; border-radius:15px; overflow:hidden;">
                        <iframe width="100%" height="230" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                    </div>
                {% endif %}
            </div>
            <p style="font-size:12px; color:#444; margin-top:20px;">تطوير يوسف - مبرمج تالتة ثانوي 🎓</p>
        </body>
    ''', v_id=v_id)

# ده سطر مهم عشان Vercel يشوف الـ app
app = app
    
