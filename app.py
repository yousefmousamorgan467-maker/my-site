from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

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
                if "items" in res and len(res["items"]) > 0:
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
            <title>Yousef Music | Elite Edition</title>
            <style>
                :root { --main-color: #00f2ff; --secondary-color: #0061ff; }
                body { 
                    margin: 0; height: 100vh; display: flex; align-items: center; justify-content: center;
                    font-family: 'Poppins', sans-serif;
                    background: #050505; color: #fff; overflow: hidden;
                }
                
                /* خلفية الانيميشن الفخمة */
                .bg-animate {
                    position: absolute; width: 100%; height: 100%;
                    background: linear-gradient(45deg, #050505, #111, #050505);
                    z-index: -1;
                }

                .player-card {
                    background: rgba(255, 255, 255, 0.03);
                    backdrop-filter: blur(25px);
                    padding: 40px; border-radius: 60px; width: 85%; max-width: 420px;
                    text-align: center; border: 1px solid rgba(255, 255, 255, 0.1);
                    box-shadow: 0 40px 100px rgba(0,0,0,0.8), inset 0 0 20px rgba(255,255,255,0.05);
                    position: relative;
                }

                h1 { font-size: 24px; font-weight: 800; letter-spacing: 3px; margin-bottom: 25px; color: var(--main-color); text-shadow: 0 0 15px var(--main-color); }

                input[type="text"] { 
                    width: 85%; padding: 15px; border-radius: 50px; border: none; 
                    background: rgba(255,255,255,0.05); color: #fff; margin-bottom: 20px;
                    text-align: center; border: 1px solid rgba(255,255,255,0.1); outline: none; transition: 0.3s;
                }
                input:focus { border-color: var(--main-color); box-shadow: 0 0 15px rgba(0, 242, 255, 0.2); }

                .btn-search { 
                    width: 100%; padding: 15px; background: linear-gradient(90deg, var(--secondary-color), var(--main-color));
                    color: #fff; border: none; border-radius: 50px; font-weight: bold; cursor: pointer;
                    box-shadow: 0 10px 20px rgba(0, 97, 255,
    
