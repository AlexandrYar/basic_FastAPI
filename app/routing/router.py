from fastapi import FastAPI
from dataclasses import dataclass

'''
Класс для путей
register_routes позволяет итерироваться по всем роутерам,
которые находятся в кортеже routes
в
'''
@dataclass(frozen=True)
class Routes:

    routes: tuple

    def register_routes(self, app: FastAPI):

        for router in self.routes:
            app.include_router(router=router)