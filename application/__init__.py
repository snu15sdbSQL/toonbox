
from flask import Flask
import os

# Generate Flask Instance & config
app = Flask('toonbox')
import config

# ORM & DB Migration Module
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

# DB initialization (db info in config.py)

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
from toonbox.models import schema


#Bind controller function to endpoint
for base, dirs, names in os.walk(os.path.join('toonbox', 'controllers')):
	for name in filter(lambda s: s.endswith('.py') and s != '__init__.py', names) :
		exec('from toonbox.controllers.'+name[:-3]+' import *')

