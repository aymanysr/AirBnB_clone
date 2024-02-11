#!/usr/bin/python3
"""
initializes the models package
"""


from models.engine.file_storage import FileStorage
from models.user import User


storage = FileStorage()
storage.reload()
