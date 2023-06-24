from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        self.__engine.connect()
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if getenv('HBNB_ENV'):
            Base.metadata.drop_all(self.__engine)
