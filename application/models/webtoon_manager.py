from application import db
from sqlalchemy import text
from schema import Webtoon

def get_all_webtoons (con):
	return con.execute("select id from webtoon")

def get_webtoons_by_title(title, author, is_finished):
	con = db.engine.connect()
	trans = con.begin()
	
	sql =  text("select * from webtoon where title = :title")
	rawresult = con.execute(sql, title = title)	
	trans.commit()
	result = []
	for row in rawresult:
		dic = {}
		dic['title'] = row['title']
		dic['url'] = row['url']
		dic['author'] = row['author']
		dic['site'] = row['site']
		dic['introduction'] = row['introduction']
		dic['picture'] = row['picture']
		result.append(dic)
	
	return result
