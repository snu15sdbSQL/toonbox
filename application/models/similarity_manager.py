from sqlalchemy import text
from schema import Webtoon_Similarity

def update_similarity(con, id1, id2, sim):
	trans = con.begin()
	selectCmd = text("select id from webtoon__similarity where webtoon_id1 = :id1 and webtoon_id2 = :id2")
	updateCmd = text("update webtoon__similarity set similarity = :sim where id = :ID")
	insertCmd = text("insert into webtoon__similarity values (null, :id1, :id2, :sim)")
	try:
		rawResult = con.execute(selectCmd, id1 = id1, id2 = id2)
		result = []
		for row in rawResult:
			result.append({0: row[0]})
		if len(result):
			con.execute(updateCmd, sim = sim, ID = result[0][0])
		else:
			con.execute(insertCmd, id1 = id1, id2 = id2, sim = sim)
		trans.commit()
	except:
		trans.rollback()
		raise
