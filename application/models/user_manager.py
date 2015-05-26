from application import db
from sqlalchemy import text
from schema import User


def add_user(email, password, name):
	user = User(
		password = db.func.md5(password),
		name     = name,
		email    = email
	)
	db.session.add(user)
	db.session.commit()
	return user.id

def login_check(email, password):
	return User.query.filter(User.email == email, User.password == db.func.md5(password)).count() != 0

def get_all_users():
	users = db.engine.execute('select * from user')
	return users

def exists_check(email):
	sql = text("select count(*) from user where email =" + email)
	raw_result = db.engine.execute(sql)
	if raw_result == 0:
		return False
	else:
		return True


def get_user_by_email(email):
	sql = text("select * from user where email =" + email)
	raw_user = db.engine.execute(sql)
	user = {}
	user['id'] = raw_user['id']
	user['name'] = raw_user['name']
	return user