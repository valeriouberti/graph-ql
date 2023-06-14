from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    age: int = Column(Integer)