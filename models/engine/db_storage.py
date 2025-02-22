#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


class DBStorage:
    """Represents a database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curr session all objects of the given class"""
        """if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id):
                obj for obj in objs}"""
        objDict = {}
        if cls is None:
            classes = {'State': State, 'City': City, 'User': User, 'Place': Place, 'Review': Review, 'Amenity': Amenity}
            for key, value in classes.items():
                # print("Here")
                objct = self.__session.query(value).all()
                for obj in objct:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    # print(key)
                    objDict[key] = obj
        else:
            if type(cls) == str:
                cls = eval(cls)
            objct = self.__session.query(cls)
            for obj in objct:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objDict[key] = obj

        # print(objDict)
        return objDict

    def new(self, obj):
        """Add obj to the current database session."""
        if not obj:
            return
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
