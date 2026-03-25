import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# مفتاح الـ API اللي استخرجته يا يوسف
API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ" 

@app.route('/', methods=['GET', 'POST'])
def home():
    v_id = ""
    if request.method == 'POST':
        q = request.form.get('query')
        if q:
            try:
                # طلب البحث من يوتيوب
                url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={q}&type=video&key={API_KEY}&maxResults=1"
                res = requests.get(url).json()
                if "items" in res:
                    v_id = res["items"][0]["id"]["videoId"]
            except Exception:
                v_id = "error"

    return render_template_string('''
        <!DOCTYPE html>
        <html dir="rtl">
        <body style="background:#000; color:#fff; text-align:center; font-family:sans-serif; padding:20px;">
            <div style="border:2px solid #1db954; border-radius:25px; padding:25px; max-width:420px; margin:auto; background:#111; box-shadow: 0 0 20px #1db954;">
                <h1 style="color:#1db954;">🎸 Yousef Music</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية..." style="width:100%; padding:15px; border-radius:25px; border:none; margin-bottom:15px; text-align:center; background:#222; color:#fff; outline:none;">
                    <button type="submit" style="width:100%; padding:12px; border-radius:25px; border:none; background:#1db954; color:#000; font-weight:bold; cursor:pointer;">بحث وتشغيل 🚀</button>
                </form>
                {% if v_id and v_id != "error" %}
                    <div style="margin-top:20px; border-radius:15px; overflow:hidden;">
                        <iframe width="100%" height="230" src="https://www.youtube.com/embed/{{ v_id }}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
                    </div>
                {% elif v_id == "error" %}
                    <p style="color:red; margin-top:20px;">حدث خطأ في البحث، جرب مرة أخرى.</p>
                {% endif %}
            </div>
            <p style="font-size:12px; color:#444; margin-top:20px;">تطوير يوسف - مبرمج تالتة ثانوي 🎓</p>
        </body>
        </html>
    ''', v_id=v_id)

if __name__ == "__main__":
    app.run()
    
