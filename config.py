import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                      'database/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

BLOGGING_URL_PREFIX = '/blog'
BLOGGING_DISQUS_SITENAME = 'test'
BLOGGING_SITEURL = 'http://localhost:8000'
BLOGGING_SITENAME = 'My Site'
BLOGGING_KEYWORDS = ['blog', 'meta', 'keywords']

FILEUPLOAD_IMG_FOLDER = 'fileupload'
FILEUPLOAD_PREFIX = '/fileupload'
FILEUPLOAD_ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

WHOOSH_BASE = os.path.join(basedir, 'database/search.db')
MAX_SEARCH_RESULTS = 50





WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'