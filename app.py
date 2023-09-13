from flask import Flask

app = Flask(__name__)


@app.route("/home")
def home():
    return "<p>bienvenido al home!</p>"


@app.route("/contacto")
def contacto():
    return "<h3 style=color:blue> Bienvenido a contacto</h3>"