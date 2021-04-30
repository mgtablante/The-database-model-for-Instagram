import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Home (Base):
    __tablename__ = 'home'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(Integer, ForeignKey('Login.Password'))
    user_name =  Column(Integer, ForeignKey('User.user_name'))
    url = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post = Column(Integer, ForeignKey('post.id'))
    Post_p = relationship('Post')
    User = relationship('User')


class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250))
    password = Column(Integer, ForeignKey('Login.password'))
    repassword = Column(Integer, ForeignKey('Login.repassword'))
    sex = Column(String(8))
    phone_number = Column(String(8))
    user_from_id = Column(String(250), nullable=False)
    user_to_id= Column(Integer, ForeignKey('home.id'))
    post = Column(Integer, ForeignKey('post.id'))


class Comments (Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(Integer, ForeignKey('user.id'))
    post = Column(Integer, ForeignKey('post.id'))
    like = Column(Integer, ForeignKey('like.id'))
    login = relationship('Login')
    user = relationship ('User')


class Like (Base):
    __tablename__ = 'like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    likes = Column(String(250))
    user_id = Column(Integer, ForeignKey('post.id'))
    comment = Column(Integer, ForeignKey('comments.id'))


class Post (Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    likes = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Integer, ForeignKey('comments.id'))
    like = Column(Integer, ForeignKey('like.id'))
    login = relationship('Login')
    user = relationship ('User')    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')