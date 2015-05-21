#-*- coding:utf-8 -*-
from application import app
from flask import Flask, request, redirect, url_for, render_template, session, abort
from application.models import webtoon_manager
import json

@app.route('/get_webtoons_by_title', methods= ['POST'])
def get_webtoons_by_title():
	title = request.form['title']
	results = webtoon_manager.get_webtoons_by_title(title)
	return json.dumps(results)