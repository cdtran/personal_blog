from app import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from .forms import LoginForm, EditorForm
from .models import Users, Post
from datetime import datetime


@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.filter_by(published=True)
    return render_template('home.html', page='home', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', page='about')


@app.route('/contact')
def contact():
    return render_template('contact.html', page='contact')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(name=form.name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)


@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = EditorForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data,
                    slug=form.slug.data, published=form.title.data,
                    created_timestamp=datetime.utcnow(),
                    updated_timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
    return render_template('post.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/<slug>')
def detail(slug):
    post = Post.query.filter_by(slug=slug).first()
    if post == None:
        flash('Page not found')
        return redirect(url_for('home'))
    return render_template('detail.html', post=post)


@app.route('/<slug>/edit', methods=['GET', 'POST'])
@login_required
def edit(slug):
    form = EditorForm()
    current_post = Post.query.filter_by(slug=slug).first()
    if form.validate_on_submit():
        current_post.title = form.title.data
        current_post.body = form.body.data
        current_post.published = form.published.data
        current_post.slug = form.slug.data
        current_post.updated_timestamp = datetime.utcnow()
        db.session.add(current_post)
        db.session.commit()
        return redirect(url_for('detail', slug=current_post.slug))
    else:
        form.title.data = current_post.title
        form.body.data = current_post.body
        form.published.data = current_post.published
        form.slug.data = current_post.slug
    return render_template('edit.html', form=form)


@app.route('/unpublished')
@login_required
def unpublished():
    posts = Post.query.filter_by(published=False)
    return render_template('unpublished.html', posts=posts)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500