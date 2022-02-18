from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/login")
def login():
    return "<p>Login Here</p>"


@app.route('/INSTRUCTION')
def pv():
    return render_template(('pv.html'))

@app.route('/Download')
def dw():
    return render_template(('dw.html'))