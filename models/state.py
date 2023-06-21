#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(60), nullable=False)
    cities = relationship('City', backref='state')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            cities_list = []
            cities_objs = storage.all(City)
            for k, v in cities_objs.values():
                if v.state_id == self.id:
                    cities_list.append(v)

            return cities_list
