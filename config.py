import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                      'database/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'ktranman@gmail.com'
MAIL_PASSWORD = 'xmxcmvbyriifmngz'
EMAIL_RECIPIENT = ['ktranman@gmail.com']

POSTS_PER_PAGE = 4
