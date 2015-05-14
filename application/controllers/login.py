#-*- coding:utf-8 -*-
from application import app
from flask import Flask, redirect, request, url_for, render_template, session
from application.models import user_manager

@app.route('/')
@app.route('/login', methods= ['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		email = request.form['email']
		password = request.form['password']
		login_success = user_manager.login_check(email,password)
		if login_success:
			return redirect(url_for('main'))
		else:
			return redirect(url_for('login'))

@app.route('/signup', methods= ['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		email = request.form['email']
		password = request.form['password']
		name = request.form['name']
		user_id = user_manager.add_user(email, password,name)
		session['user_name'] = name
		session['user_id'] = user_id
		return redirect(url_for('main'))

