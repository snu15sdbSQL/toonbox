from application import db

#Tables

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(80))
	password = db.Column(db.String(60))


class Webtoon(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	author = db.Column(db.String(30))
	genre = db.Column(db.String(30))
	finished = db.Column(db.Boolean, default = '0')
	title = db.Column(db.String(40))
	picture = db.Column(db.String(80))
	rating = db.Column(db.Float)
	last_update = db.Column(db.DateTime) 
	introduction = db.Column(db.String(150))


# relationship tables

class User_Webtoon(db.Model):
	id 			= db.Column(db.Integer, primary_key = True)
	user_id 	= db.Column(db.Integer, db.ForeignKey('user.id'))
	user   		= db.relationship('User', foreign_keys = [user_id],
		backref = db.backref('user_webtoons', cascade = 'all, delete-orphan', lazy = 'dynamic'))
	webtoon_id 	= db.Column(db.Integer, db.ForeignKey('webtoon.id'))
	webtoon 	= db.relationship('Webtoon', foreign_keys = [webtoon_id],
		backref = db.backref('user_webtoons', cascade = 'all, delete-orphan', lazy = 'dynamic'))
	score 		= db.Column(db.Integer)

class Webtoon_Similarity(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	webtoon_id1 = db.Column(db.Integer)
	webtoon_id2 = db.Column(db.Integer)
	similarity = db.Column(db.Integer)
