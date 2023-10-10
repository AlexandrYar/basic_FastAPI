import logging

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, select

from app.configuration.db import session
from app.shemas.db.user.model import User

class Database():

    def set_user(self, user: User):
        session.add(user)
        logging.info(f'Добавление пользователя с id: {user.id} в БД прошло успешно...')


    def get_user_by_id(self, id: int):
        stmt = select(User).where(User.id == id)
        user = session.scalar(stmt)
        logging.info(f'Выдача информации по пользователю с id: {user.id} в БД прошло успешно...')
        return user

    def delete_user_by_id(self, id: int):
        user = self.get_user_by_id(id)
        session.delete(user)
        logging.info(f'Пользователь с id:{user.id} удален из БД...')

    def upgrade_user_by_id(self, user: User):
        pass
