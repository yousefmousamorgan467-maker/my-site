from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Yousef's Music World</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { 
                    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
                    background-size: 400% 400%;
                    animation: gradient 10s ease infinite;
                    color: white; text-align: center; font-family: sans-serif; padding-top: 30px;
                    margin: 0; height: 100vh;
                }
                @keyframes gradient {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }
                .card { 
                    background: rgba(255, 255, 255, 0.1); 
                    padding: 20px; 
                    border-radius: 15px; 
                    display: inline-block; 
                    backdrop-filter: blur(10px);
                    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
                    width: 85%;
                    max-width: 400px;
                }
                .song-box { margin-bottom: 25px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 15px; }
                audio { width: 100%; margin-top: 10px; }
                h1 { font-size: 24px; margin-bottom: 20px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎵 Yousef's Music 🎵</h1>
                
                <div class="song-box">
                    <p>Sasa Exclusive 2026</p>
                    <audio controls>
                        <source src="/Sasa_Exclusive_2026.mp3" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </div>

                <div class="song-box">
                    <p>Samer Exclusive</p>
                    <audio controls>
                        <source src="/Samer_Exclusive.mp3" type="audio/mpeg">
                    </audio>
                </div>

                <p style="font-size: 12px; color: #bbb;">Made by Yousef 🚀</p>
            </div>
        </body>
    </html>
    """
    
