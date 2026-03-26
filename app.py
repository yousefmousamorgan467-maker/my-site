from flask import Flask, render_template_string

app = Flask(__name__)

# السطر ده هو اللي هيشيل الـ Error بتاع الـ "Method Not Allowed"
@app.route('/', methods=['GET'])
def index():
    # كود التصميم العالمي اللي هيبهرك
    html_code = """
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yousef Music Neon Pro</title>
        <style>
            :root { --neon-green: #00ff00; --glow-shadow: 0 0 15px rgba(0, 255, 0, 0.4); }
            body {
                background: radial-gradient(circle at center, #1a1a1a 0%, #000 100%);
                color: #fff;
                font-family: 'Poppins', sans-serif;
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                overflow: hidden;
            }
            .player-card {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(20px);
                border: 2px solid rgba(0, 255, 0, 0.2);
                border-radius: 40px;
                padding: 40px;
                width: 85%;
                max-width: 480px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.7), 0 0 30px rgba(0, 255, 0, 0.1);
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            .player-card::before {
                content: '';
                position: absolute;
                bottom: -150px;
                left: 50%;
                transform: translateX(-50%);
                width: 300px;
                height: 300px;
                background: radial-gradient(circle, var(--neon-green) 0%, rgba(0, 255, 0, 0) 70%);
                filter: blur(50px);
                opacity: 0.15;
                animation: pulseGlow 4s infinite alternate;
            }
            .profile-pic {
                width: 120px;
                height: 120px;
                background: #222;
                border: 3px solid rgba(255, 255, 255, 0.1);
                border-radius: 50%;
                margin: 0 auto 25px auto;
                background-image: url('https://e.top4top.io/m_3737rddma9.mp3'); /* حط رابط صورتك هنا */
                background-size: cover;
                background-position: center;
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }
            h1 {
                color: var(--neon-green);
                font-size: 30px;
                margin: 0 0 5px 0;
                text-transform: uppercase;
                letter-spacing: 3px;
                text-shadow: 0 0 10px rgba(0, 255, 0, 0.6);
            }
            .status { color: #aaa; font-size: 14px; margin-bottom: 35px; }
            .audio-container {
                background: rgba(0,0,0,0.4);
                padding: 10px;
                border-radius: 50px;
                border: 1px solid rgba(0, 255, 0, 0.2);
            }
            audio {
                width: 100%;
                height: 50px;
            }
            /* ستايل شريط التقديمcontrols - البطل هنا */
            audio::-webkit-media-controls-panel { background-color: rgba(30, 30, 30, 0.9); }
            audio::-webkit-media-controls-current-time-display,
            audio::-webkit-media-controls-time-remaining-display { color: #fff; }
            audio::-webkit-media-controls-play-button,
            audio::-webkit-media-controls-seek-back-button,
            audio::-webkit-media-controls-seek-forward-button { color: var(--neon-green); }
            audio::-webkit-media-controls-timeline {
                /* ده عشان يخلي شريط التقديم أخضر */
                background-color: var(--neon-green);
            }
            .footer { margin-top: 35px; color: #444; font-size: 11px; letter-spacing: 1px; }
            
            @keyframes pulseGlow {
                0% { opacity: 0.1; transform: translateX(-50%) scale(1); }
                100% { opacity: 0.25; transform: translateX(-50%) scale(1.1); }
            }
        </style>
    </head>
    <body>
        <div class="player-card">
            <div class="profile-pic"></div>
            <h1>Yousef Music Pro</h1>
            <p class="status">Exclusive Neon Remix - 2026</p>
            
            <div class="audio-container">
                <audio controls>
                    <source src="https://e.top4top.io/m_3737rddma9.mp3" type="audio/mpeg">
                </audio>
            </div>

            <p class="footer">Coded & Designed by Yousef Mousa</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run()
    
