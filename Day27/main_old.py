from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine, Engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///orm.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

Base.metadata.create_all(engine)
user1 = Users(name='Alice', email='alice@example.com')
user2 = Users(name='Bob', email='bob@example.com')

session.add_all([user1, user2])
session.commit()