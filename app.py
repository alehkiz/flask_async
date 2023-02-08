from flask import Flask
import asyncio
from flask.cli import with_appcontext
from config import BaseConfig
from model import User
from configure_app import init

def create_app(name=__name__, mode='production'):
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    init(app)
    return app
    


# app = Flask(__name__)

# @app.route('/')
# async def main():
#     return ''

# app.run(host='0.0.0.0')

