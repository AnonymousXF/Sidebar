from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, BigInteger
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

class MemInfo(Base):
    __tablename__ = 'meminfo'
    id = Column(Integer, primary_key=True)
    host = Column(Text)
    mem_total = Column(BigInteger)
    mem_used = Column(BigInteger)
    mem_free = Column(BigInteger)
    percent = Column(Float)
    timestamp = Column(DateTime)

class CPUInfo(Base):
    __tablename__ = 'cpuinfo'
    id = Column(Integer, primary_key=True)
    host = Column(Text)
    cpu_percent = Column(Float)
    timestamp = Column(DateTime)

Base.metadata.create_all(engine)

