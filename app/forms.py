from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField,\
    BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email
from .models import Post


class LoginForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class EditorForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 140)])
    slug = StringField('Slug', validators=[DataRequired(), Length(1, 94)])
    body = TextAreaField()
    published = BooleanField('Publish?')
    submit = SubmitField('Submit')

    def validate_slug(self, field):
        if Post.query.filter_by(slug=field.data).first() and field.data \
                != self.slug.data:
            raise ValidationError('Slug already in use.')


class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
