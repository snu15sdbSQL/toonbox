from application import db
from sqlalchemy import text
from schema import User


def add_user(email, password, name):
	user = User(
		password = password,
		name     = name,
		email    = email
	)
	db.session.add(user)
	db.session.commit()
	return user.id

def delete_user(id):
	sql = text("delete from user where id = :id")
	db.engine.execute(sql, id = id)
		

def login_check(email, password):
	sql = text("select id from user where email = :email and password = :password")
	raw_result = db.engine.execute(sql, email = email, password = password)
	result = []
	for row in raw_result:
		result.append({0: row[0]})
	if len(result):
		return True
	else:
		return False	

def get_all_users():
	users = db.engine.execute('select * from user')
	return users

def exists_check(email):
	sql = text("select id from user where email = :email")
	raw_result = db.engine.execute(sql, email = email)
	result = []
	for row in raw_result:
		result.append({0: row[0]})
	if len(result):
		return True
	else:
		return False


def get_user_by_email(email):
	sql = text("select * from user where email = :email")
	raw_user = db.engine.execute(sql, email = email)
	for row in raw_user:
		user = {}
		user['user_id'] = row['id']
		user['name'] = row['name']
	return user

