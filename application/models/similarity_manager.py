from application import db
from sqlalchemy import text
from schema import Webtoon_Similarity

def test():
	return db.engine.execute("select * from user")

def connect():
	return db.engine.connect()

def update_similarity(con, id1, id2, sim):
	trans = con.begin()
	deleteCmd = text("delete from webtoon_similarity where webtoon_id1 = :id1 and webtoon_id2 = :id2")

	insertCmd = text("insert into webtoon_similarity values (null, :id1, :id2, :sim)")
	try:
		con.execute(deleteCmd, id1 = id1, id2 = id2)
		con.execute(insertCmd, id1 = id1, id2 = id2, sim = sim)
		trans.commit()
	except:
		trans.rollback()
		raise
