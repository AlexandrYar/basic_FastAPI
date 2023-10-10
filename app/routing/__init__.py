from app.routing.router import Routes
from app.routing.routes import user

'''Инициалицация объекта класса Routes,
в который мы передает кортеж и объектов класса APIrouter'''
__rousers__ = Routes(routes=(user.router, ))