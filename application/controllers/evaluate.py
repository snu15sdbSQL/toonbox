#-*- coding:utf-8 -*-
from application import app
from flask import Flask, request, redirect, url_for, render_template, session, abort
from application.models import uw_manager
import json

@app.route('/evaluate_webtoon', methods= ['POST'])
def evaluate_webtoon():
	userId = request.form['id']
	webtoonId = request.form['webtoon']
	score = request.form['score']
	uw_manager.evaluate_webtoon(userId, webtoonId, score)
	return 'success'
