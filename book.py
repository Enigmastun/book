#! -*- cp:936 -*-
from flask_script import Manager
from app import create_app
from app import db
from app.models import User, Role
from flask_migrate import Migrate, MigrateCommand
from app import mail

app = create_app('default')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    #manager.run()
    app.run(debug=True)








