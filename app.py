from flask import Flask as Flask
app = Flask(__name__)

@app.route("/")
def start():
    return "web-сервер на flask"
