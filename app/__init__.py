import os
import datetime
from flask import Flask, render_template, request, Response
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cachce=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),user=os.getenv("MYSQL_USER"),password=os.getenv("MYSQL_PASSWORD"),host=os.getenv("MYSQL_HOST"),port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

#Sebastian's Functions
@app.route('/aboutSebas')
def sebasProfile():
    return render_template('sebastian.html', extra_hobbies="Hobbies", hobby_list=["Going to the beach","Swimming","Reading"],
    extra_work="Work experiences", work_list=["Freelance web page dev","Indoor cycling staff"], 
    extra_education="Education",education_list=["Harkness Highscool", "MLH Fellowship"])

@app.endpoint("sebasWork")
def sebasWork():
    return render_template('sebastian.html', scrollToAnchor='work', extra_hobbies="Hobbies", hobby_list=["Going to the beach","Swimming","Reading"],
    extra_work="Work experiences", work_list=["Freelance web page dev","Indoor cycling staff"], 
    extra_education="Education",education_list=["Harkness Highscool", "MLH Fellowship"])

@app.endpoint("sebasHobbies")
def sebasHobbies():
    return render_template('sebastian.html', scrollToAnchor='hobbies', extra_hobbies="Hobbies", hobby_list=["Going to the beach","Swimming","Reading"],
    extra_work="Work experiences", work_list=["Freelance web page dev","Indoor cycling staff"], 
    extra_education="Education",education_list=["Harkness Highscool", "MLH Fellowship"])

@app.endpoint("sebasEducation")
def sebasEducation():
    return render_template('sebastian.html', scrollToAnchor='education', extra_hobbies="Hobbies", hobby_list=["Going to the beach","Swimming","Reading"],
    extra_work="Work experiences", work_list=["Freelance web page dev","Indoor cycling staff"], 
    extra_education="Education",education_list=["Harkness Highscool", "MLH Fellowship"])

@app.endpoint("sebasTravel")
def sebasTravel():
    return render_template('sebastian.html', scrollToAnchor='travel', extra_hobbies="Hobbies", hobby_list=["Going to the beach","Swimming","Reading"],
    extra_work="Work experiences", work_list=["Freelance web page dev","Indoor cycling staff"], 
    extra_education="Education",education_list=["Harkness Highscool", "MLH Fellowship"])

@app.route('/jinjaTest')
def jinjTest():
    return render_template('extraTemplate.html', url=os.getenv("URL"), my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

#Endpoints
app.add_url_rule("/aboutSebas-work", endpoint="sebasWork")
app.add_url_rule("/aboutSebas-hobbies", endpoint="sebasHobbies")
app.add_url_rule("/aboutSebas-education", endpoint="sebasEducation")
app.add_url_rule("/aboutSebas-travel", endpoint="sebasTravel")



#Sally's Functions
@app.route('/aboutSally')
def sallyProfile():
    return render_template('sally.html', extra_hobbies="Hobbies", hobby_list=["Watching YouTube","Listening to music"],
    extra_work="Projects", work_list=["Task Tracker Website","News Website"], 
    extra_education="Education", education_list=["Saratoga High School", "MLH Fellowship"])

@app.endpoint('sallyWork')
def sallyWork():
    return render_template('sally.html', scrollToAnchor='work', extra_hobbies="Hobbies", hobby_list=["Watching YouTube","Listening to music"],
    extra_work="Projects", work_list=["Task Tracker Website","News Website"], 
    extra_education="Education", education_list=["Saratoga High School", "MLH Fellowship"])

@app.endpoint('sallyHobbies')
def sallyHobbies():
    return render_template('sally.html', scrollToAnchor='hobbies', extra_hobbies="Hobbies", hobby_list=["Watching YouTube","Listening to music"],
    extra_work="Projects", work_list=["Task Tracker Website","News Website"], 
    extra_education="Education", education_list=["Saratoga High School", "MLH Fellowship"])

@app.endpoint('sallyEducation')
def sallyEducation():
    return render_template('sally.html', scrollToAnchor='education', extra_hobbies="Hobbies", hobby_list=["Watching YouTube","Listening to music"],
    extra_work="Projects", work_list=["Task Tracker Website","News Website"], 
    extra_education="Education", education_list=["Saratoga High School", "MLH Fellowship"])

@app.endpoint('sallyTravel')
def sallyTravel():
    return render_template('sally.html', scrollToAnchor='travel', extra_hobbies="Hobbies", hobby_list=["Watching YouTube","Listening to music"],
    extra_work="Projects", work_list=["Task Tracker Website","News Website"], 
    extra_education="Education", education_list=["Saratoga High School", "MLH Fellowship"])

#Endpoints
app.add_url_rule("/aboutSally-work", endpoint="sallyWork")
app.add_url_rule("/aboutSally-hobbies", endpoint="sallyHobbies")
app.add_url_rule("/aboutSally-education", endpoint="sallyEducation")
app.add_url_rule("/aboutSally-travel", endpoint="sallyTravel")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    if 'name' not in request.form:
        return Response("Invalid name", status=400)
    if 'email' not in request.form or '@' not in request.form['email']:
        return Response("Invalid email", status=400)
    if 'content' not in request.form or request.form['content'] == '':
        return Response("Invalid content", status=400)
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

#@app.route('/api/timeline_post', methods=['DELETE'])
#def delete_time_line_post():

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline", timeline_posts=get_time_line_post())
    
