# -*- coding:cp936 -*-
from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission


def permission_required(permission):
    def decotator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.scan(permission):
                abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return decotator


def admin_required(func):
    return permission_required(Permission.ADMINISTER)(func)
