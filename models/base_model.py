#!/usr/bin/python3
"""
Class for BaseModel
"""

import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance
        """
        if kwargs:
            # If the instance is created from a dictionary representation
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # If it's a new instance
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            models.storage.new(self)  # add the instance to the dictionary

    def __str__(self):
        """
        Return the string representation of the BaseModel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        return new_dict
