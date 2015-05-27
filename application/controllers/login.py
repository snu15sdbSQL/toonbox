#-*- coding:utf-8 -*-
from application import app
from flask import Flask, redirect, request, url_for, render_template, session
from application.models import user_manager

@app.route('/')
@app.route('/login', methods= ['GET','POST'])
def login():
	if request.method == 'GET':
		if 'user_name' in session:
			return redirect(url_for('main'))
		else:
			return render_template('login.html')
	else:
		email = request.form['email']
		password = request.form['password']
		user_exists = user_manager.login_check(email,password)
		print(user_exists)
		if user_exists:
			user = user_manager.get_user_by_email(email)
			session['user_name'] = user['name']
			session['user_id'] = user['user_id']
			return redirect(url_for('main'))
		else:
			return render_template('login_fail.html')


@app.route('/signup', methods= ['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		email = request.form['email']
		password = request.form['password']
		name = request.form['name']
		if not user_manager.exists_check(email):
			user_id = user_manager.add_user(email, password,name)
			session['user_name'] = name
			session['user_id'] = user_id
			return redirect(url_for('main'))
		else:
			return '이미 해당 이메일의 유저가 존재합니다.'


@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('login'))
