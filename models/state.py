#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances
          with state_id equals to the current State.id"""
        from models import storage
        all_cities = storage.all(City)
        list_cities = []
        for value in all_cities.values():
            if value.state_id == self.id:
                list_cities.append(value)
        return list_cities
