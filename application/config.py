
from application import app



app.config.update(dict(
    # SQLALCHEMY_DATABASE_URI='mysql://root:db@localhost:3306/toonbox?charset=utf8',
    SQLALCHEMY_DATABASE_URI='mysql://root:db@54.65.177.207:3306/toonbox?charset=utf8',
    DEBUG=True,
    SECRET_KEY='toonbox key',
    migration_directory='migrations',
    compare_type=True
))

