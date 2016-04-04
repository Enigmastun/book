# -*- coding:cp936 -*-
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views
