from typing import Optional
from pydantic import BaseModel


class UserUpdateForm(BaseModel):
    nickname: Optional[str] = None
    stage_one: bool
    stage_two: bool

class UserCreateForm(BaseModel):
    nickname: Optional[str] = None
    stage_one: bool
    stage_two: bool


class GameCreateForm(BaseModel):
    description: str
    stage_number: int
    stage_end: str


