# -*- coding:cp936 -*-
from flask_wtf import Form
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_pagedown.fields import PageDownField


class EditProfileForm(Form):
    location = StringField('Where are you living', validators=[Length(1, 64)])
    about_me = StringField('introduce yourself', validators=[Length(1, 128)])
    submit = SubmitField(u'提交')


class Postform(Form):
    body = PageDownField('What do you want to do', validators=[DataRequired()])
    submit = SubmitField('tijiao')


class CommentForm(Form):
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField(u'评论')
