from flask_mail import Message
from app import app, mail
from flask import render_template
from .decorators import async
from config import EMAIL_RECIPIENT


def send_async_email(app, message):
    with app.app_context():
        mail.send(message)

@async
def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    send_async_email(app, msg)


def send_contact(name, email, subject, message):
    send_email(subject, 'blog', EMAIL_RECIPIENT,
               render_template('email.txt', name=name, email=email,
                               message=message))
