from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("mysql+mysqlconnector://root:root@localhost:3306/test")
Session = sessionmaker(bind=engine)
db = Session()
Base = declarative_base()

class Host(Base):
    __tablename__ = 'host'
    host_name = Column(Text)
    host_ip = Column(String(20), primary_key=True)
    user = Column(String(20), primary_key=True)
    pwd = Column(String(64))

Base.metadata.create_all(engine)

