from flask import Flask, render_template_string, request

app = Flask(__name__)

# مفتاح الـ API الخاص بـ يوسف
API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ"

@app.route('/', methods=['GET', 'POST'])
def index():
    v_id = None
    title = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            try:
                url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}&maxResults=1"
                res = requests.get(url).json()
                if "items" in res and res["items"]:
                    v_id = res['items'][0]['id']['videoId']
                    title = res['items'][0]['snippet']['title']
            except:
                v_id = "error"
    
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Yousef Studio Pro</title>
            <style>
                body { background: #000; color: #1db954; text-align: center; font-family: sans-serif; padding: 20px; }
                .card { border: 2px solid #1db954; display: inline-block; padding: 30px; border-radius: 25px; background: #111; width: 100%; max-width: 400px; margin-top: 40px; box-shadow: 0 0 20px rgba(29,185,84,0.3); }
                input { padding: 15px; border-radius: 25px; border: none; width: 85%; margin-bottom: 15px; background: #222; color: #fff; text-align: center; outline: none; }
                button { padding: 12px 25px; background: #1db954; color: #000; font-weight: bold; border: none; border-radius: 25px; cursor: pointer; width: 100%; }
                #status { display: none; color: #fff; margin-top: 15px; background: #333; padding: 10px; border-radius: 10px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎸 Yousef Studio</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اسم الأغنية اللي عايزها..." required>
                    <button type="submit">بحث وتشغيل 🚀</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:25px;">
                        <h3 style="color:#fff;">🎶 {{ title }}</h3>
                        <iframe width="1" height="1" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay"></iframe>
                        <p style="font-size:12px; color: #888;">✅ شغالة في الخلفية (صوت فقط)</p>
                        
                        <button onclick="startDownload('{{ v_id }}')" id="dlBtn" style="background:#fff; color:#000; margin-top:15px;">
                            تحميل MP3 للموبايل ⬇️
                        </button>
                        <div id="status">جاري سحب الأغنية من السيرفر.. انتظر ثواني</div>
                    </div>
                {% endif %}
            </div>

            <script>
                function startDownload(vId) {
                    const btn = document.getElementById('dlBtn');
                    const status = document.getElementById('status');
                    btn.style.display = 'none';
                    status.style.display = 'block';

                    // الحيلة هنا: بنبعت الطلب لسيرفر تحميل خارجي بيحولها لـ MP3 أوتوماتيك
                    const dlUrl = `https://api.vevioz.com/api/button/mp3/${vId}`;
                    
                    // هنفتح لينك التحميل في صفحة خفية عشان يبدأ التحميل فوراً
                    const win = window.open(dlUrl, '_blank');
                    
                    // بعد 5 ثواني هنرجع الزرار تاني
                    setTimeout(() => {
                        btn.style.display = 'block';
                        status.style.display = 'none';
                    }, 5000);
                }
            </script>
        </body>
        </html>
    ''', v_id=v_id, title=title)

app = app
    
