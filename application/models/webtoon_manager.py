from sqlalchemy import text
from schema import Webtoon

def get_all_webtoons (con):
	return con.execute("select id from webtoon")
