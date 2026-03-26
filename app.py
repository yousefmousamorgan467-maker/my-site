from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # ده كود الـ HTML اللي فيه تصميم موقعك وشريط التقديم
    html_code = """
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yousef Music</title>
        <style>
            body {
                background-color: #000;
                color: #fff;
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                height: 100vh;
            }
            .container {
                padding: 20px;
            }
            h1 {
                color: #00ff00;
                text-shadow: 0 0 10px #00ff00;
                font-size: 2.5em;
            }
            .player-box {
                background: #111;
                border: 2px solid #00ff00;
                border-radius: 20px;
                padding: 30px;
                margin: 20px auto;
                max-width: 80%;
                box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);
            }
            audio {
                width: 100%;
                height: 50px;
                margin-top: 20px;
            }
            /* ده عشان يخلي شكل الشريط أخضر في أغلب المتصفحات */
            audio::-webkit-media-controls-panel {
                background-color: #222;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Yousef Music</h1>
            <p>أقوى ريمكس للدبة - حصرياً 2026</p>
            
            <div class="player-box">
                <p>تشغيل الآن</p>
                <audio controls>
                    <source src="https://e.top4top.io/m_3737rddma9.mp3" type="audio/mpeg">
                    متصفحك لا يدعم تشغيل الصوت.
                </audio>
            </div>
            
            <p style="color: #555;">Designed by Yousef</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
    
