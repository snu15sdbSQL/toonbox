from application import db
from sqlalchemy import text
from schema import Webtoon

def get_all_webtoons (con):
	return con.execute("select id from webtoon")

def get_webtoons_by_title(title, author, is_finished):
	cmd =  text("select * from webtoon where title = :title")
	return db.engine.execute(cmd)
	# return Webtoon.query.filter(Webtoon.title == title).all()