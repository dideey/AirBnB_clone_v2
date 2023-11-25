#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all,delete", backref="user")
    reviews = relationship("Review", cascade="all,delete", backref="user")

    @property
    def reviews(self):
        """getter attribute reviews that returns the list of Review
          instances with place_id equals to the current Place.id
        """
        from models import storage
        review = []
        all_reviews = storage.all(Review)
        for value in all_reviews.values():
            if value.place_id == self.id:
                review.append(value)
        return review
