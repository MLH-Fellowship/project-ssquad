import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


if __name__ == '__main__':
    app.run(host='127.0.0.1')

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

#Sebastian's Functions
@app.route('/aboutSebas')
def sebasProfile():
    return render_template('sebastian.html', url=os.getenv("URL"))

@app.endpoint("sebasWork")
def sebasWork():
    return render_template('sebastian.html', scrollToAnchor='work')

@app.endpoint("sebasHobbies")
def sebasHobbies():
    return render_template('sebastian.html', scrollToAnchor='hobbies')

@app.endpoint("sebasEducation")
def sebasEducation():
    return render_template('sebastian.html', scrollToAnchor='education')

@app.endpoint("sebasTravel")
def sebasTravel():
    return render_template('sebastian.html', scrollToAnchor='travel')

#Endpoints
app.add_url_rule("/aboutSebas-work", endpoint="sebasWork")
app.add_url_rule("/aboutSebas-hobbies", endpoint="sebasHobbies")
app.add_url_rule("/aboutSebas-education", endpoint="sebasEducation")
app.add_url_rule("/aboutSebas-travel", endpoint="sebasTravel")

#Sally's Functions
@app.route('/aboutSally')
def sallyProfile():
    return render_template('sally.html', url=os.getenv("URL"))

@app.endpoint('sallyWork')
def sallyWork():
    return render_template('sally.html', scrollToAnchor='work')

@app.endpoint('sallyHobbies')
def sallyHobbies():
    return render_template('sally.html', scrollToAnchor='hobbies')

@app.endpoint('sallyEducation')
def sallyEducation():
    return render_template('sally.html', scrollToAnchor='education')

@app.endpoint('sallyTravel')
def sallyTravel():
    return render_template('sally.html', scrollToAnchor='travel')

#Endpoints
app.add_url_rule("/aboutSally-work", endpoint="sallyWork")
app.add_url_rule("/aboutSally-hobbies", endpoint="sallyHobbies")
app.add_url_rule("/aboutSally-education", endpoint="sallyEducation")
app.add_url_rule("/aboutSally-travel", endpoint="sallyTravel")
