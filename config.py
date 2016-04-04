# -*- coding:cp936 -*-


class Config:
        SECRET_KEY = 'YOU WILL NEVER GUESS IT'
        SQLALCHEMY_COMMIT_ON_TEARDOWN = True
        SQLALCHEMY_TRACK_MODIFICATIONS = True
        MAIL_SERVER = 'smtp.qq.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True

        MAIL_USERNAME = '496271730@qq.com'
        MAIL_PASSWORD = 'zaxdkdrqucqebiee'
        FLASKY_ADMIN = '845216875@qq.com'

        @staticmethod
        def init_app(app):
            pass


class Development(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:/Users/Join Smit/PycharmProjects/book/app/static/data.db"


config = {
    'default': Development
}

