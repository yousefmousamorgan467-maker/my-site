import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)

# مفتاحك اللي شغال تمام
API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ" 

@app.route('/', methods=['GET', 'POST'])
def home():
    v_id = ""
    if request.method == 'POST':
        q = request.form.get('query')
        if q:
            url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={q}&type=video&key={API_KEY}&maxResults=1"
            res = requests.get(url).json()
            if "items" in res and res["items"]:
                v_id = res["items"][0]["id"]["videoId"]

    return render_template_string('''
        <body style="background:#0b0b0b; color:#fff; text-align:center; font-family:sans-serif; padding:20px;">
            <div style="border:2px solid #1db954; border-radius:30px; padding:30px; max-width:450px; margin:auto; background:#121212; box-shadow: 0 10px 30px rgba(29, 185, 84, 0.3);">
                <h1 style="color:#1db954; font-size:28px;">🎸 Yousef Player Pro</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="ابحث عن أي أغنية أو فيديو..." 
                           style="width:100%; padding:15px; border-radius:30px; border:1px solid #333; margin-bottom:15px; text-align:center; background:#1db9541a; color:#fff; outline:none;">
                    <button type="submit" style="width:100%; padding:15px; border-radius:30px; border:none; background:#1db954; color:#000; font-weight:bold; cursor:pointer; font-size:16px;">تشغيل الآن 🚀</button>
                </form>
                
                {% if v_id %}
                    <div style="margin-top:25px; border-radius:20px; overflow:hidden; border:2px solid #1db954;">
                        <iframe width="100%" height="250" 
                                src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1&rel=0&showinfo=0&controls=1" 
                                frameborder="0" 
                                allow="autoplay; encrypted-media" 
                                allowfullscreen>
                        </iframe>
                    </div>
                    <div style="margin-top:15px;">
                        <a href="https://www.youtube.com/watch?v={{ v_id }}" target="_blank" style="color:#1db954; text-decoration:none; font-size:14px;">فتح في يوتيوب إذا لم يعمل المشغل 🔗</a>
                    </div>
                {% endif %}
            </div>
            <p style="font-size:12px; color:#555; margin-top:30px;">Developed by Yousef 🎓 - Python Specialist</p>
        </body>
    ''', v_id=v_id)
    
