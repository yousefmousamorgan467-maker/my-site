from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # استبدل كلمة 'yousefmousamorgan467-maker' باسم اليوزر بتاعك على GitHub لو كان مختلف
    github_user = "yousefmousamorgan467-maker"
    repo = "my-site"
    
    return f"""
    <html>
        <head>
            <title>Yousef Music World</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ 
                    background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460);
                    color: white; text-align: center; font-family: sans-serif; padding-top: 30px;
                    margin: 0; height: 100vh;
                }}
                .card {{ 
                    background: rgba(255, 255, 255, 0.1); 
                    padding: 25px; border-radius: 20px; 
                    display: inline-block; backdrop-filter: blur(15px);
                    width: 85%; max-width: 400px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                }}
                .song-box {{ margin-bottom: 30px; }}
                audio {{ width: 100%; filter: drop-shadow(0 2px 5px rgba(0,0,0,0.5)); }}
                h2 {{ margin-bottom: 20px; font-weight: 300; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🎵 Yousef's Playlist 🎵</h2>
                
                <div class="song-box">
                    <p>عصام صاصا 2026</p>
                    <audio controls>
                        <source src="https://raw.githubusercontent.com/{github_user}/{repo}/main/Sasa_Exclusive_2026.mp3" type="audio/mpeg">
                    </audio>
                </div>

                <div class="song-box">
                    <p>سامر المدني</p>
                    <audio controls>
                        <source src="https://raw.githubusercontent.com/{github_user}/{repo}/main/Samer_Exclusive.mp3" type="audio/mpeg">
                    </audio>
                </div>
            </div>
        </body>
    </html>
    """
    
