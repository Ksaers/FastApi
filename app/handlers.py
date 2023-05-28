from datetime import datetime

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.models import User, connect_db, Game
from app.forms import UserCreateForm, GameCreateForm, UserUpdateForm

router = APIRouter()



#Get Запрос для информации игры и пользователя
@router.get('/user_game', name='user_game:get')
def get_user_game(user_id: int, game_id: str, database=Depends(connect_db)):
    exists_user = database.query(User).filter(User.id == user_id).one_or_none()
    exists_game = database.query(Game).filter(Game.id == game_id).one_or_none()

    if not exists_user or not exists_game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User id or game id not found",
        )

    game = database.query(Game).filter(Game.id == game_id).one_or_none()
    user = database.query(User).filter(User.id == user_id).one_or_none()

    if game and user:
        return {
            'user': user.get_filtered_data(),
            'game': game.get_filtered_data(),
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game or User not found",
        )



#Post Создание информации о игре
@router.post('/game', name='game:create')
def create_game(game: GameCreateForm = Body(..., embed=True), database=Depends(connect_db)):
    """
    For stage_end use format dd.mm.yyyy exmp 27.05.2003
    """
    exists_game = database.query
    new_game = Game(
     description=game.description,
     stage_number=game.stage_number,
     stage_end = datetime.strptime(game.stage_end, '%d.%m.%Y').strftime('%Y-%m-%d')
    )
    database.add(new_game)
    database.commit()
    return {'game_id': new_game.id}

#Get Запрос информации о игре
@router.get('/game', name='game:get')
def get_user(description: str, database=Depends(connect_db)):
    game = database.query(Game).filter(Game.description == description).one_or_none()
    return {
        'game': game.get_filtered_data(),
        'game_id': game.id,
    }

#Post Создание нового пользователя
@router.post('/user', name='user:create')
def create_user(user: UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_user = database.query(User.id).filter(User.nickname == user.nickname).one_or_none()
    if exists_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='nickname already taken',
        )

    new_user = User(
        nickname=user.nickname,
        stage_one=user.stage_one,
        stage_two=user.stage_two,
    )
    database.add(new_user)
    database.commit()
    return {'user_id': new_user.id}


#Put Запрос для изменения данных пользователя по его ID
@router.put('/user', name='user:update')
def update_user(
        id: int,
        user_form: UserUpdateForm = Body(..., embed=True),
        database=Depends(connect_db)
):
    """
    Update user information
    """
    user = database.query(User).filter(User.id == id).one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {id} doesnt exist',
        )

    user.nickname = user_form.nickname
    database.add(user)
    database.commit()
    return {'nickname': user_form.nickname}


@router.get('/')
def index():
    """
        Non-functional part
        """
    return {'Write after your ip --> /docs'}
