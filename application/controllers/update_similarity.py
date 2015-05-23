#-*- coding:utf-8 -*-
from application import app
from application import db
from application.models import similarity_manager, uw_manager, webtoon_manager

def update_similarity():
	con = db.engine.connect()
	
	rawResult = webtoon_manager.get_all_webtoons(con)
	webtoons = []
	for row in rawResult:
		webtoons.append({'id': row[0]})
	
	for webtoon in webtoons:
		id1 = webtoon['id']
		targets = get_sim_targets(con, id1)
		for target in targets:
			id2 = target['id']
			sim = calculate_similarity(con, id1, id2)
			similarity_manager.update_similarity(con, id1, id2, sim)
			

def get_sim_targets(con, id1):
	rawResult = uw_manager.webtoons_has_common(con, id1)
	targets = []
	for row in rawResult:
		targets.append({'id': row[0]})
	return targets

def calculate_similarity(con, id1, id2):
        rawResult = uw_manager.get_score_vecs(con, id1, id2)
        result = []
        for row in rawResult:
                result.append({'user_id': row[0], 'score1': row[1], 'score2' : row[2]})

        size1 = 0
        size2 = 0
        total = 0.
        for dic in result:
                total += dic['score1'] * dic['score2']
                size1 += dic['score1'] ** 2
                size2 += dic['score2'] ** 2
        return total / (size1 * size2) ** 0.5
