from application import db

#Tables

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(40))
	email = db.Column(db.String(80))
