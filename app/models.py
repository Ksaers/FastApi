from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, CHAR, Boolean, text
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from app.config import DATABASE_URL

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
    session = Session(bind=engine.connect())
    return session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    stage_one = Column(Boolean)
    stage_two = Column(Boolean)
    created_at = Column(String, default=datetime.utcnow())


    def get_filtered_data(self):
        return {
            'nickname': self.nickname,
            'stage_one': self.stage_one,
            'stage_two': self.stage_two,
            'created_at': self.created_at
        }

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    stage_number = Column(String)
    stage_end = Column(String)
    created_at = Column(String, default=datetime.utcnow())


    def get_filtered_data(self):
        return {
            'description': self.description,
            'stage_number': self.stage_number,
            'stage_end': self.stage_end,
            'created_at': self.created_at
        }
