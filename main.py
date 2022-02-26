from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html')


@app.route('/INSTRUCTION')
def pv():
    return render_template(('is.html'))

@app.route("/CONTACT US")
def ca():
    return render_template(('ca.html'))

@app.route('/DOWNLOAD')
def dw():
    return render_template(('dw.html'))


