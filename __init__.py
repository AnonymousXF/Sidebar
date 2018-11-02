from flask import Flask
import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:root@localhost:3306/test")
Session = sessionmaker(bind=engine)
db = Session()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'ZdTaiWxb5nozs2yf'

    from .dashboard import dashboard
    app.register_blueprint(dashboard)

    return app
