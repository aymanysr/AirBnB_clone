#!/usr/bin/python3
"""class for the amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class for the amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes amenity"""
        super().__init__(*args, **kwargs)
