import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import dotenv_values

from src.app import create_app, db


conf_env = dotenv_values(".env")
env_name = conf_env["FLASK_ENV"]
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()