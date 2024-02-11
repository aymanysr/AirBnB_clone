#!/usr/bin/python3
"""class for the city"""

from models.base_model import BaseModel


class City(BaseModel):
    """class for the city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
