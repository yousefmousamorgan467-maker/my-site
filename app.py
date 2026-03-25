from flask import Flask, render_template_string, request, redirect
import requests

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
            <title>Yousef Music Studio</title>
            <style>
                body { background: #000; color: #1db954; text-align: center; font-family: sans-serif; padding: 20px; }
                .card { border: 2px solid #1db954; display: inline-block; padding: 30px; border-radius: 25px; background: #111; width: 100%; max-width: 400px; margin-top: 40px; }
                input { padding: 15px; border-radius: 25px; border: none; width: 85%; margin-bottom: 15px; background: #222; color: #fff; text-align: center; outline: none; }
                button { padding: 12px 25px; background: #1db954; color: #000; font-weight: bold; border: none; border-radius: 25px; cursor: pointer; width: 100%; }
                .loader { display: none; color: #fff; margin-top: 10px; font-size: 14px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎸 Yousef Studio</h1>
                <form method="POST">
                    <input type="text" name="query" placeholder="اسم الأغنية..." required>
                    <button type="submit">بحث وتشغيل 🚀</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:25px;">
                        <h3 style="color:#fff;">🎶 {{ title }}</h3>
                        <iframe width="1" height="1" src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" frameborder="0" allow="autoplay"></iframe>
                        <p style="font-size:12px;">✅ شغالة في الخلفية</p>
                        
                        <button onclick="downloadDirect('{{ v_id }}')" id="dlBtn" style="background:#fff; color:#000; margin-top:15px;">
                            تحميل MP3 مباشر ⬇️
                        </button>
                        <div id="status" class="loader">جاري تجهيز الملف... ثواني</div>
                    </div>
                {% endif %}
            </div>

            <script>
                async function downloadDirect(vId) {
                    const btn = document.getElementById('dlBtn');
                    const status = document.getElementById('status');
                    btn.style.display = 'none';
                    status.style.display = 'block';

                    try {
                        // استخدام API بتاع Cobalt للتحميل المباشر
                        const response = await fetch('https://api.cobalt.tools/api/json', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                            body: JSON.stringify({
                                url: `https://www.youtube.com/watch?v=${vId}`,
                                downloadMode: 'audio',
                                audioFormat: 'mp3'
                            })
                        });
                        const data = await response.json();
                        if (data.url) {
                            window.location.href = data.url; // التحميل بيبدأ هنا فوراً
                        } else {
                            alert('عذراً، حاول مرة أخرى');
                        }
                    } catch (e) {
                        alert('حدث خطأ في الاتصال بالسيرفر');
                    } finally {
                        btn.style.display = 'block';
                        status.style.display = 'none';
                    }
                }
            </script>
        </body>
        </html>
    ''', v_id=v_id, title=title)

app = app
                    
