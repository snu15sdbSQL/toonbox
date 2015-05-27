from application import db
from sqlalchemy import text
from schema import User_Webtoon

def webtoons_has_common (con, webtoonId):
	cmd = text("select distinct webtoon_id from user__webtoon natural join (select user_id from user__webtoon where webtoon_id = :webtoonId) temp")
	return con.execute(cmd, webtoonId = webtoonId)

def get_score_vecs (con, id1, id2):
	cmd = text("select user_id, score1, score2 "
		+ "from (select user_id, score as score1 from user__webtoon where webtoon_id = :id1) temp1 natural join "
		+ "(select user_id, score as score2 from user__webtoon where webtoon_id = :id2) temp2")
	return con.execute(cmd, id1 = id1, id2 = id2)

def get_score_vec (con, userId):
	cmd = text("select webtoon_id, score from user__webtoon where user_id = :userId")
	return con.execute(cmd, userId = userId)

def evaluate_webtoon (userId, webtoonId, score):
	con = db.engine.connect()
	trans = con.begin()
	selectCmd = text("select id from user__webtoon where user_id = :userId and webtoon_id = :webtoonId")
	updateCmd = text("update user__webtoon set score = :score where id = :ID")
	insertCmd = text("insert into user__webtoon values (null, :userId, :webtoonId, :score)")
	try:
		rawResult = con.execute(selectCmd, userId = userId, webtoonId = webtoonId)
		result = []
		for row in rawResult:
			result.append({0: row[0]})
		if len(result):
			con.execute(updateCmd, score = score, ID = result[0][0])
		else:
			con.execute(insertCmd, userId = userId, webtoonId = webtoonId, score = score)
		trans.commit()
	except:
		trans.rollback()
		raise

def get_evaluation (userId):
	con = db.engine.connect()
	cmd = text("select * from (select webtoon_id as id, score from user__webtoon where user_id = :userId) temp natural join webtoon")
	rawResult = con.execute(cmd, userId = userId)
	result = []
	for row in rawResult:
		result.append({'id': row['id'], 'title': row['title'], 'url': row['url'], 'author': row['author'],
			'site': row['site'], 'introduction': row['introduction'], 'picture': row['picture'], 'score': row['score']})
	return result
