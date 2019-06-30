from flask import Flask, render_template
import json
app = Flask(__name__)

with open("static/resume.json") as r:
    resume = json.load(r)


@app.route('/')
def index():
    return render_template('Resume.html')

@app.route('/skills')
def skills(resume=resume):
    return render_template('Skills.html', resume=resume)

@app.route('/experience')
def experience(resume=resume):
    return render_template('Experience.html', resume=resume)

@app.route('/summary')
def summary(resume=resume):
    return render_template('Summary.html', resume=resume)

@app.route('/education')
def education(resume=resume):
    return render_template('Education.html', resume=resume)