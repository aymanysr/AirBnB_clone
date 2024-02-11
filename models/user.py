#!/usr/bin/python3
"""class for the user"""

from models.base_model import BaseModel


class User(BaseModel):
    """class for the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
