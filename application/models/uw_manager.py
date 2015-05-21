from sqlalchemy import text
from schema import User_Webtoon

def webtoons_has_common (con, webtoonId):
	cmd = text("select distinct webtoon_id from user__webtoon natural join (select user_id from user__webtoon where webtoon_id = :webtoonId) temp")
	return con.execute(cmd, webtoonId = webtoonId)

def get_score_vecs (con, id1, id2):
	cmd = text("select user_id, score1, ifnull(score2, 0) "
		+ "from (select user_id, score as score1 from user__webtoon where webtoon_id = :id1) temp1 natural left outer join "
		+ "(select user_id, score as score2 from user__webtoon where webtoon_id = :id2) temp2")
	return con.execute(cmd, id1 = id1, id2 = id2)
