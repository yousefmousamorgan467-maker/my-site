from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Yousef Dev</title>
            <style>
                body { background-color: #121212; color: #00ff00; text-align: center; font-family: sans-serif; padding-top: 50px; }
                h1 { color: #ff00ff; }
                .btn { background: #ff00ff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>Welcome to Yousef's World! 🚀</h1>
            <p>مبرمج مصري في تالتة ثانوي بيحب البايثون والمونتاج.</p>
            <br>
            <a href="#" class="btn">قريباً: مذكرات الفيزياء والكيمياء</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

