import os
from dotenv import load_dotenv

from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy import create_engine, MetaData


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
print(DATABASE_URL,' <- URL')
engine = create_engine(DATABASE_URL)
engine = engine

Session = sessionmaker(bind=engine)
session = Session()
session = session

metadata = MetaData()


print('BIM BIM BAM BAM')
