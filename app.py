from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Yousef Music World</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { 
                    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                    background-size: 400% 400%;
                    animation: gradient 15s ease infinite;
                    color: white; 
                    text-align: center; 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    padding-top: 50px;
                    height: 100vh;
                    margin: 0;
                }
                @keyframes gradient {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }
                .container {
                    background: rgba(0, 0, 0, 0.6);
                    padding: 30px;
                    border-radius: 20px;
                    display: inline-block;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                }
                h1 { color: #fff; text-shadow: 2px 2px 4px #000; }
                .music-card { margin-top: 20px; padding: 15px; border-top: 1px solid #555; }
                audio { margin-top: 10px; filter: invert(100%); width: 250px; }
                .btn { 
                    display: inline-block;
                    background: #fff; color: #e73c7e; 
                    padding: 10px 25px; text-decoration: none; 
                    border-radius: 50px; font-weight: bold;
                    transition: 0.3s; margin-top: 20px;
                }
                .btn:hover { transform: scale(1.1); background: #ff00ff; color: #fff; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎵 Yousef's Playlist 🎵</h1>
                <p>تالتة ثانوي وبايثون.. ومزاج عالي</p>
                
                <div class="music-card">
                    <p>اسم الأغنية الأولى</p>
                    <audio controls>
                        <source src="رابط_الأغنية_هنا.mp3" type="audio/mpeg">
                        متصفحك لا يدعم مشغل الأغاني.
                    </audio>
                </div>

                <div class="music-card">
                    <p>اسم الأغنية الثانية</p>
                    <audio controls>
                        <source src="رابط_الأغنية_هنا.mp3" type="audio/mpeg">
                    </audio>
                </div>

                <br>
                <a href="#" class="btn">Physics Notes 📚</a>
            </div>
        </body>
    </html>
    """
    
