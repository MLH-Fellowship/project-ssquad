import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/aboutSebas')
def sebasPage():
    return render_template('sebastian.html', url=os.getenv("URL"))

@app.route('/aboutSally')
def sallyProfile():
    return render_template('sally.html', url=os.getenv("URL"))

@app.route('/aboutSally-work')
def sallyWork():
    return render_template('sally.html', scrollToAnchor='work')

@app.route('/aboutSally-hobbies')
def sallyHobbies():
    return render_template('sally.html', scrollToAnchor='hobbies')

@app.route('/aboutSally-education')
def sallyEducation():
    return render_template('sally.html', scrollToAnchor='education')

@app.route('/aboutSally-travel')
def sallyTravel():
    return render_template('sally.html', scrollToAnchor='travel')