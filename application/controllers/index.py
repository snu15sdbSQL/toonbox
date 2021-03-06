#-*- coding:utf-8 -*-
from application import app
from flask import Flask, redirect, url_for, render_template, session
from application.controllers import update_similarity
from application.controllers import recommend_webtoon
from application.models import webtoon_manager, uw_manager


# @app.route('/')
@app.route('/main')
def main():
   webtoon_num = webtoon_manager.total_webtoon_num()
   score_num = uw_manager.total_score_num()
   number = {}
   number['toon'] = webtoon_num
   number['score'] = score_num
   return render_template('main.html', number = number)


@app.route('/recommend')
def recommend():
   return render_template('webtoon_list.html', results = recommend_webtoon.recommend(session['user_id']))

@app.route('/search')
def search():
   return render_template('search.html')

@app.route('/evaluation_history')
def evaluation_history():
   results = uw_manager.get_evaluation(session['user_id'])
   return render_template('webtoon_list.html', results = results)

@app.route('/update_sim')
def update_sim():
   update_similarity.update_similarity()
   return 'success'

@app.route('/test_recommend')
def test_recommend():
   print(uw_manager.get_evaluation(session['user_id']))
   return 'success'

@app.route('/load_sim')
def load_sim():
   recommend_webtoon.similarity_loading()
   return 'success'
