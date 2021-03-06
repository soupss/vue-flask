"""
manage.py
- provides a command line utility for interacting with the
application to perform interactive debugging and setup
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.app import create_app
from app.models import db, Article

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                Article=Article)

if __name__ == '__main__':
    manager.run()
