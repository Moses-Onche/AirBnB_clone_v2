#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Defines a review for the database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        place_id (sqlalchemy String): id of the review's place.
        user_id (sqlalchemy String): id of the review's user.
        text (sqlalchemy String): The description of the review.
        """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
