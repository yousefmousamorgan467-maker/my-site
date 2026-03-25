from flask import Flask, render_template_string, request, redirect
import requests

app = Flask(__name__)

# مفتاح الـ API الخاص بك يا يوسف
API_KEY = "AIzaSyDBfEkyok9JzZJ8DQCFLard7EJSglE8CAQ"

@app.route('/', methods=['GET', 'POST'])
def index():
    v_id = None
    title = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            try:
                # طلب البحث من يوتيوب
                url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}&maxResults=1"
                res = requests.get(url).json()
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
            <title>Yousef Music Pro</title>
            <style>
                body { 
                    background: #000; 
                    color: #1db954; 
                    text-align: center; 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    padding: 20px; 
                }
                .card { 
                    border: 2px solid #1db954; 
                    display: inline-block; 
                    padding: 30px; 
                    border-radius: 30px; 
                    background: #111; 
                    box-shadow: 0 10px 30px rgba(29, 185, 84, 0.2); 
                    width: 90%; 
                    max-width: 450px; 
                    margin-top: 50px;
                }
                input { 
                    padding: 15px; 
                    border-radius: 25px; 
                    border: 1px solid #333; 
                    width: 85%; 
                    margin-bottom: 15px; 
                    background: #222; 
                    color: #fff; 
                    text-align: center; 
                    outline: none;
                }
                button { 
                    padding: 12px 30px; 
                    background: #1db954; 
                    color: #000; 
                    font-weight: bold; 
                    border: none; 
                    border-radius: 25px; 
                    cursor: pointer; 
                    font-size: 16px;
                    transition: 0.3s;
                }
                button:hover { transform: scale(1.05); background: #1ed760; }
                .download-btn { 
                    background: #fff; 
                    color: #000; 
                    margin-top: 15px;
                    display: inline-block;
                    text-decoration: none;
                    padding: 10px 20px;
                    border-radius: 20px;
                    font-weight: bold;
                }
                .status { color: #888; font-size: 14px; margin-top: 10px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎸 Yousef Studio</h1>
                <p style="color:#eee;">ابحث، استمع، وحمّل MP3 مباشرة</p>
                
                <form method="POST">
                    <input type="text" name="query" placeholder="اكتب اسم الأغنية أو الفنان..." required>
                    <br>
                    <button type="submit">تشغيل الآن 🎵</button>
                </form>

                {% if v_id and v_id != "error" %}
                    <div style="margin-top:25px; border-top: 1px solid #333; padding-top: 20px;">
                        <h3 style="color:#fff;">🎶 {{ title }}</h3>
                        
                        <iframe id="player" width="1" height="1" 
                                src="https://www.youtube.com/embed/{{ v_id }}?autoplay=1" 
                                frameborder="0" allow="autoplay"></iframe>
                        
                        <p class="status">✅ الصوت شغال الآن (يمكنك الخروج من المتصفح)</p>
                        
                        <a href="/download/{{ v_id }}" target="_blank" class="download-btn">
                            تحميل الأغنية MP3 ⬇️
                        </a>
                    </div>
                {% elif v_id == "error" %}
                    <p style="color:#ff4444; margin-top:20px;">❌ عذراً، لم نجد نتائج. تأكد من اسم الأغنية.</p>
                {% endif %}
            </div>
            <p style="color:#444; margin-top:40px; font-size: 12px;">Developed by Yousef 🎓 - Secondary 3 Student</p>
        </body>
        </html>
    ''', v_id=v_id, title=title)

@app.route('/download/<v_id>')
def download(v_id):
    # تحويل لموقع y2mate الموثوق للتحميل مباشرة
    return redirect(f"https://www.y2mate.com/youtube/{v_id}")

# سطر مهم لعمل التطبيق على Vercel
app = app
