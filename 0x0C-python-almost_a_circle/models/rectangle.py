#!/usr/bin/python3
"""Creating a rectangle class"""
import json
from models.base import Base

class Rectangle(Base):
    """The class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    


