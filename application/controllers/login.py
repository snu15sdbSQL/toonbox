#-*- coding:utf-8 -*-
from application import app
from flask import Flask, redirect, url_for, render_template

@app.route('/')
@app.route('/login')
def login():
   return render_template('login.html')

