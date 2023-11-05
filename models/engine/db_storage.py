#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from sqlalchemy.schema import MetaData


class DBStorage:
    """This class manages storage of hbnb models in mysqldb format"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialise the database storage engine according to env config"""
        DBStorage.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB"),
            ), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        queried_dict = {}
        if cls is None:
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            for cls in [State, City, User, Amenity, Place, Review]:
                db_query = self.__session.query(cls).all()
                for record in db_query:
                    queried_dict[f'{cls.__name__}.{record.id}'] = record
            return queried_dict
        else:
            db_query = self.__session.query(cls).all()
            for record in db_query:
                queried_dict[f'{cls.__name__}.{record.id}'] = record
            return queried_dict

    def new(self, obj):
        """Adds a new record to storage database"""
        self.__session.add(obj)

    def save(self):
        """Commit the storage session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the obj record from the database if found"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage data into a session from database"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        DBStorage.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False
        ))

    def close(self):
        """Close the currently open session"""
        self.__session.remove()
