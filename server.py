
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    
    return render_template('about.html')

@app.route('/index')
def index():


    f = open("templates/scores.json", "r")
    data = json.load(f)
    f.close()

    return render_template('index.html', data = data)



@app.route('/graph')
def graph():


    f = open("templates/scores.json", "r")
    data = json.load(f)
    f.close()

    return render_template('graph.html', data = data)



app.run(debug=True)
