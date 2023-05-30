
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

    return render_template('index.html')

app.run(debug=True)