import os
from src.app import create_app
from dotenv import dotenv_values


conf_env = dotenv_values(".env")
env_name = conf_env["FLASK_ENV"]
app = create_app(env_name)

if __name__ == '__main__':
  # run app
  app.run(host='0.0.0.0')
else:
  application = app