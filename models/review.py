#!/usr/bin/python3
"""class for the review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class for the review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
