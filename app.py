from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Yousef Dev</title>
            <style>
                body { background-color: #1a1a1a; color: white; text-align: center; font-family: Arial; padding-top: 50px; }
                h1 { color: #ff00ff; }
                .btn { background: #ff00ff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>Welcome to Yousef's World!</h1>
            <p>يوسف في تالتة ثانوي بيحب البايثون والمونتاج</p>
            <br>
            <a href="#" class="btn">Physics & Chemistry</a>
        </body>
    </html>
    """

# ده السطر المهم لـ Vercel
# مش محتاجين app.run هنا لأنه هو اللي بيشغله
