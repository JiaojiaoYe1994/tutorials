# -*- coding: utf-8 -*-
'''
This script is used for Web App test using FLASK.
'''

from flask import Flask,request
from datetime import datetime


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    
    page = '<!DOCTYPE html>' \
              '<title> Web App </title>' \
              '<h1>Have fun </h1>' \
              '<form action="/" method="POST" enctype="multipart/form-data">' \
              'Input: <textarea name="input",rows="100" cols="100"></textarea> <br>' \
              '<input type="submit" value="Submit" />' \
              '</form>'

    if request.method == 'POST':
        
        content = request.form['input']

        now = str(datetime.now())
        
        page += '<hr>'
        page += now + '</br>'
        page += "Your input is: " + content + '</br>'
        page += '<hr>'
        # return "Hello World!"

    return page


if __name__ == '__main__':

    app.run(host='0.0.0.0',
    	port='8080')
