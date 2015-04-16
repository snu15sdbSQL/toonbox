from application import db
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

