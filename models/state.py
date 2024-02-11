#!/user/bin/python3
"""class for the state"""

from models.base_model import BaseModel


class State(BaseModel):
    """class for the state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
