from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC by abhis3c (<a href=https://hackerone.com/abhis3c>https://hackerone.com/abhis3c</a>)"
