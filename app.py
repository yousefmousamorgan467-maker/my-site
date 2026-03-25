from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Yousef Music</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e); color: white; text-align: center; font-family: sans-serif; padding-top: 50px; }
                .card { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; display: inline-block; backdrop-filter: blur(10px); width: 80%; }
                audio { width: 100%; margin-top: 10px; }
                .song { margin-bottom: 20px; border-bottom: 1px solid #444; padding-bottom: 10px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🎵 Yousef's Playlist 🎵</h2>
                
                <div class="song">
                    <p>عصام صاصا 2026</p>
                    <audio controls>
                        <source src="Sasa_Exclusive_2026.mp3" type="audio/mpeg">
                    </audio>
                </div>

                <div class="song">
                    <p>سامر المدني</p>
                    <audio controls>
                        <source src="Samer_Exclusive.mp3" type="audio/mpeg">
                    </audio>
                </div>
            </div>
        </body>
    </html>
    """
    
