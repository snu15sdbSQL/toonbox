
from application import app


app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://root:db@localhost:3306/toonbox',
    DEBUG=True,
    SECRET_KEY='toonbox key',
    # SQLALCHEMY_DATABASE_URI='mysql://hermes:hermes_pass@10.113.168.97:3306/line_hermes?charset=utf8',
    migration_directory='migrations',
    compare_type=True
))

