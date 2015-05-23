#-*- coding:utf-8 -*-
from application import app
from flask import Flask, redirect, url_for, render_template
from application.controllers import update_similarity

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

@app.route('/update_sim')
def update_sim():
   update_similarity.update_similarity()
   return 'success'
