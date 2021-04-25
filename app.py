#!/usr/local/bin/python3

import datetime
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', body="Custom body")
    
@app.route('/login',methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user=request.form["email_address"]
		pw=request.form["password"]
		return f"email={user} password={pw}" 
	else:
		return render_template('login.html')

@app.route('/owner')
def get_Owner():
    return 'Hello world from Kishan'

@app.route('/datetime')
def get_datetime():
    dt = datetime.datetime.now()
    return str(dt)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
