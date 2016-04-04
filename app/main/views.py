# -*- coding:cp936 -*-
import os
from flask import render_template, url_for, redirect, request, flash
from . import main
from .forms import EditProfileForm, Postform, CommentForm
from flask_login import login_required, current_user
from app import db
from ..models import  Permission, Post, Comment


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=10, error_out=False)
    posts = pagination.items
    return render_template('main/index.html', posts=posts, pagination=pagination)


@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        return redirect(url_for('auth.user', username=current_user.username))
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('main/edit_profile.html', form=form)


@main.route('/mind', methods=['GET', 'POST'])
def mind():
    form = Postform()
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.filter_by(author=current_user._get_current_object()).order_by(Post.timestamp.desc()).paginate(page, per_page=5, error_out=True)
    posts = pagination.items
    if current_user.scan(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.mind'))
    return render_template('main/mind.html', form=form, posts=posts, pagination=pagination)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, post=post, author=current_user._get_current_object())
        db.session.add(comment)
        return redirect(url_for('.post', id=post.id))
    comments = post.comments
    return render_template('main/post.html', posts=[post], form=form, comments=comments)


