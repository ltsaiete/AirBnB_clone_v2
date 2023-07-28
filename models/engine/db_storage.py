from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None

    classes = {
        'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        Args:
            cls (_type_, optional): _description_. Defaults to None.
        Returns:
            _type_: _description_
        """
        all_dict = {}
        if cls is not None:
            objs = self.__session.query(DBStorage.classes[cls])
            for obj in objs:
                all_dict.update({cls + '.' + obj.id: obj.to_dict()})
        else:
            for k, v in DBStorage.classes.items():
                objs = self.__session.query(v)
                for obj in objs:
                    all_dict.update({k + '.' + obj.id: obj.to_dict()})

        return all_dict

    def new(self, obj):
        """_summary_
        Args:
            obj (_type_): _description_
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """Creates databases tables and starts a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)

        Session = scoped_session(session_factory)
        self.__session = Session()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        Args:
            obj (BaseModel, optional): object to delete. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)

    # def close(self):
    #     """_summary_: close() method
    #     """
    #     self.__session.remove()
