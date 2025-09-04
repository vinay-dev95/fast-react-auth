from sqlalchemy import Column, Integer, String
from db.base import Base

class User(Base):
    __tablename__ = "datas"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
