# -*- coding:cp936 -*-
from flask_wtf import Form
from wtforms import SubmitField, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp
from ..models import User

class Loginform(Form):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')


class Registerform(Form):
    email = StringField('Register Email', validators=[DataRequired(), Email()])
    username = StringField('Nickname', validators=[DataRequired(), Regexp('^[A-Za-z][A-Za-z0-9_]*$', message='forbidden')])
    password = PasswordField('Insert Password', validators=[DataRequired(), Length(8, 18)])
    password2 = PasswordField('Insert again', validators=[DataRequired(), EqualTo('password', message='mi ma bu yi yang')])
    submit = SubmitField('zhu ce')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered')





