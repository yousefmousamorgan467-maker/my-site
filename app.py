from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yousef Music Elite</title>
        <style>
            :root { --neon: #00ff00; }
            body {
                background: #000;
                color: #fff;
                font-family: 'Segoe UI', sans-serif;
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                overflow: hidden;
            }
            .card {
                background: rgba(255, 255, 255, 0.05);
                border: 2px solid var(--neon);
                border-radius: 50px;
                padding: 40px;
                width: 80%;
                max-width: 450px;
                text-align: center;
                box-shadow: 0 0 30px rgba(0, 255, 0, 0.2);
                position: relative;
            }
            .avatar {
                width: 100px; height: 100px;
                border: 2px solid var(--neon);
                border-radius: 50%;
                margin: 0 auto 20px;
                background: url('https://cdn-icons-png.flaticon.com/512/3659/3659784.png') center/cover;
                animation: pulse 2s infinite;
            }
            h1 { color: var(--neon); letter-spacing: 2px; text-shadow: 0 0 10px var(--neon); }
            audio { width: 100%; margin-top: 25px; filter: hue-rotate(90deg) brightness(1.5); }
            @keyframes pulse {
                0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 255, 0, 0.7); }
                70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(0, 255, 0, 0); }
                100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 255, 0, 0); }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="avatar"></div>
            <h1>YOUSEF MUSIC</h1>
            <p style="color: #888;">الريمكس اللي خارب الدنيا</p>
            
            <audio controls>
                <source src="https://e.top4top.io/m_3737rddma9.mp3" type="audio/mpeg">
            </audio>
            
            <p style="margin-top: 30px; font-size: 12px; color: #444;">DEVELOPED BY YOUSSEF MOUSA</p>
        </div>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run()
    
