# -*- coding:cp936 -*-
from . import admin
from flask import render_template, redirect, url_for, request
from flask_login import login_required
from ..decorators import admin_required, permission_required
from ..models import User, Role, Permission, Comment
from .forms import EditProfileAdminForm
from app import db


@admin.route('/admin_viewer')
@login_required
@admin_required
def admin_viewer():
    return render_template('admin/viewer.html')


@admin.route('/admin_editprofile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_editprofile(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.role = Role.query.get(form.role.data)
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        return redirect(url_for('auth.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.role.data = user.role_id
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('admin/editprofile.html', form=form, user=user)


@admin.route('/moderate')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate():
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(page, per_page=10, error_out=False)
    comments = pagination.items
    return render_template('admin/moderate.html', comments=comments, pagination=pagination, page=page)


@admin.route('/moderate_enable/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_enable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = False
    db.session.add(comment)
    return redirect(url_for('admin.moderate', page=request.args.get('page', 1, type=int)))


@admin.route('/moderate_disable/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_disable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = True
    db.session.add(comment)
    return redirect(url_for('admin.moderate', page=request.args.get('page', 1, type=int)))