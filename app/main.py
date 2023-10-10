from app.repository.postgres.db import Database
from app.configuration.db import metadata, engine
from app.routing import __rousers__

from fastapi import FastAPI

import logging

class Server:
    db : Database
    app : FastAPI
    def __init__(self,) -> None:
        self.db = Database()
        self.app = FastAPI()
        self.__register_routes(self.app)
        logging.info('Создание таблица БД...')
        metadata.create_all(bind=engine)
        logging.info('Все таблицы БД обновлены...')
    
    @staticmethod
    def __register_routes(app:FastAPI):
        __rousers__.register_routes(app)

server = Server()
app = server.app
