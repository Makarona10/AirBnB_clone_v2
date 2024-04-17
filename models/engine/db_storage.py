from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """DataBase class"""
    __engine = None
    __session = None
    def __init__(self):
        """Initialize an engine to connect to a database"""
        user = os.getenv("HBNB_MYSQL_USER")
        host = os.getenv("HBNB_MYSQL_HOST")
        env = os.getenv("HBNB_ENV", "none")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f"""mysql+mysqldb://{user}:{pwd}
                        @{host}/{db}""", pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in database"""
        dic = dict()
        if (cls):
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls)
            
            for obj in query:
                k = f"{type(obj).__name__}.{obj.id}"
                dic[k] = obj
        else:
            lst = [User, State, City, Amenity, Place, Review]
            for clss in lst:
                query = self.__session.query(clss)
                for obj in query:
                    k = f"{type(obj).__name__}.{obj.id}"
                    dic[k] = obj
        return dic
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create current database session
        from the engine using a sessionmaker"""
        self.__session = Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()