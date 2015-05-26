#-*- coding:utf-8 -*-
from application import app
from flask import Flask, request, redirect, url_for, render_template, session, abort
from application.models import webtoon_manager
import json

@app.route('/get_webtoons_by_title', methods= ['POST'])
def get_webtoons_by_title():
	title = request.form['title']
	author = request.form['author']
	is_finished = request.form['is_finished']
	results = webtoon_manager.get_webtoons_by_title(title, author, is_finished)
	#return json.dumps(results)
	return render_template('search_result.html', results=results)

