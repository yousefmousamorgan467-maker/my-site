from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return """
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yousef Music</title>
        <style>
            body { background-color: #000; color: #fff; font-family: sans-serif; text-align: center; margin: 0; padding: 50px 20px; }
            h1 { color: #00ff00; text-shadow: 0 0 10px #00ff00; }
            .player-box { background: #111; border: 2px solid #00ff00; border-radius: 20px; padding: 30px; margin: 20px auto; max-width: 400px; }
            audio { width: 100%; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Yousef Music</h1>
        <p>الريمكس الحصري - شريط التقديم شغال</p>
        <div class="player-box">
            <audio controls>
                <source src="https://e.top4top.io/m_3737rddma9.mp3" type="audio/mpeg">
            </audio>
        </div>
        <p style="color: #555;">Designed by Yousef</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
    
