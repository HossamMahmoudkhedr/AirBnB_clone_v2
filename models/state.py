#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.city import City
        cities = relationship("City", backref="state", cascade='all, delete')
    else:
        @property
        def cities(self):
            """an amenities property for handling associated amenities"""
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                assert type(city) is City
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
