from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    published = db.Column(db.Boolean, index=True, default=False)
    slug = db.Column(db.String(140), unique=True)
    created_timestamp = db.Column(db.DateTime, index=True)
    updated_timestamp = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '<Post %r>' % (self.body)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return self.id
        except NameError:
            return str(self.id)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

