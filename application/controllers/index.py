#-*- coding:utf-8 -*-
from application import app
from flask import Flask, redirect, url_for, render_template
from application.models import similarity_manager

@app.route('/')
@app.route('/main')
def main():
   return render_template('main.html')


@app.route('/evaluate')
def evaluate():
   return render_template('evaluate.html')

@app.route('/search')
def search():
   return render_template('search.html')

@app.route('/evaluate_history')
def evaluate_history():
   return render_template('evaluate_history.html')

@app.route('/update_similarity')
def update_similarity():
   result = similarity_manager.test();
   for row in result:
	print(row[0])
   con = similarity_manager.connect()
   similarity_manager.update_similarity(con, 1, 2, 0.3)
   return render_template('main.html')
