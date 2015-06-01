#-*- coding:utf-8 -*-
from application import db
from sqlalchemy import text
from schema import Webtoon
from schema import User

def get_all_webtoons (con):
	return con.execute("select id from webtoon")

def get_webtoons_by_title(title, author, is_finished, userId):
	con = db.engine.connect()

	if is_finished == "true":
		sql = text("select id, title, url, author, site, introduction, picture, ifnull(score, 0) score from webtoon natural left outer join (select user_id, webtoon_id id, score from user__webtoon where user_id = :userId) temp where title like '%" + title +"%' and author like '%"+author+"%' and finished = true")
	else :
		sql = text("select id, title, url, author, site, introduction, picture, ifnull(score, 0) score from webtoon natural left outer join (select user_id, webtoon_id id, score from user__webtoon where user_id = :userId) temp where title like '%" + title +"%' and author like '%"+author+"%'")
	rawresult = con.execute(sql, userId = userId)
	result = []
	for row in rawresult:
		dic = {}
		dic['id'] = row['id']
		dic['title'] = row['title']
		dic['url'] = row['url']
		dic['author'] = row['author']
		dic['site'] = row['site']
		dic['introduction'] = row['introduction']
		dic['picture'] = row['picture']
		dic['score'] = row['score']
		result.append(dic)
	
	return result


def get_webtoons_by_id(con, webtoonId):
	cmd = text("select * from webtoon where id = :webtoonId")
	return con.execute(cmd, webtoonId = webtoonId)
def total_webtoon_num():
	rawResult = db.engine.execute("select count(*) from webtoon")
	result = []
	for row in rawResult:
		result.append(row[0])
	return result[0]
