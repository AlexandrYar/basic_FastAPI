from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

from app.configuration.db import metadata

Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    passwordHash= Column(String, nullable=False)
    email = Column(String, nullable=False)
    role = Column(String(50))
    
    def __repr__(self) -> str:
        return f"User: \n\tid :{self.id}, \n\tlogin :{self.login}, \n\temail :{self.email}, \n\tpasswordHash :{self.passwordHash}, "
    