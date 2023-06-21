#!/usr/bin/python3
'''
    Package initializer
'''
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()