#-*- coding:utf-8 -*-
from application import app
from application import db
from application.models import similarity_manager, uw_manager, webtoon_manager
from operator import itemgetter

def similarity_loading():
	con = db.engine.connect()
	
	rawResult = similarity_manager.get_similarity(con)
	global similarity_matrix
	similarity_matrix = {}
	for row in rawResult:
		similarity_matrix[(row[0], row[1])] = row[2]

def recommend(userId):
	con = db.engine.connect()
	rawResult = webtoon_manager.get_all_webtoons(con)
	webtoons = []
	for row in rawResult:
		webtoons.append({'id': row[0]})
	
	rawResult = uw_manager.get_score_vec(con, userId)
	score_vec = {}
	for row in rawResult:
		score_vec[row[0]] = row[1]
	
	psudo_score_list = []
	for webtoon in webtoons:
		id1 = webtoon['id']
		psudo_score = 0.
		for id2 in score_vec:
			psudo_score += score_vec[id2] * similarity_matrix.get((id1, id2), 0)
		psudo_score_list.append((id1, psudo_score))

	psudo_score_list.sort(key=itemgetter(1), reverse = True)
	
	recommend_list = []
	count = 0
	for webtoon in psudo_score_list:
		if(not(webtoon[0] in score_vec)):
			recommend_list.append(webtoon)
			count += 1
		if(count == 10):
			break
	return recommend_list
