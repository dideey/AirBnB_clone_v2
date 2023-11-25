#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """"""
    __engine = None
    __session = None
    models_classes = ["User", "Place", "State", "City", "Review"]

    def __init__(self):
        """initiate DB connection"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """fetch all objects"""
        dictionary = {}
        if cls is not None:
            # fetch all objects of cls
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                dictionary[key] = instance
        else:
            # fetch all objects of all classes
            for mycls in self.models_classes:
                mycls = eval(mycls)
                for instance in self.__session.query(mycls).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    dictionary[key] = instance
        return dictionary

    def new(self, obj):
        """addd the new obj to the DB"""
        self.__session.add(obj)

    def save(self):
        """commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from DB"""
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.engine)
        dbsession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(dbsession)
        self.__session = Session()
