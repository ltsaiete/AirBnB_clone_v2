#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    # amenity_ids = []

    reviews = relationship('Review', backref='place',
                           cascade="save-update, delete")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        from models import storage

        @property
        def reviews(self):
            reviews_list = []
            reviews_objs = storage.all(Review)
            for k, v in reviews_objs.values():
                if v.place_id == self.id:
                    reviews_list.append(v)
            return reviews_list
