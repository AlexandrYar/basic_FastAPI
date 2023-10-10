from fastapi import APIRouter
'''Папка internal  хранит в себе модули сторонних приложений
(redis, postgres и тд)'''

router = APIRouter(
    prefix='/api/user'
)

@router.get('/get_user')
def get_user_info():
    return{
        'ALexandr': 'bim bim bam bam '
    }

@router.post('/set_user')
def set_user():
    pass