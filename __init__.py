from flask import Flask
import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:root@localhost:3306/test")
DBSession = sessionmaker(bind=engine)


def create_app():
    app = Flask(__name__)

    from .dashboard import dashboard
    from .api import api
    app.register_blueprint(dashboard)
    app.register_blueprint(api, url_prefix='/api')

    return app
