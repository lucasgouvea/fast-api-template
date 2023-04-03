from typing import Union
from fastapi import APIRouter, HTTPException

from fast_api_template.modules.user.entities import User

router = APIRouter()

users = [User(**{'id': 1, 'name': "Lucas"}),User(**{'id': 2, 'name': "Felipe"})]

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id == 1:
        return users[0]
    if user_id == 2:
        return users[1]
    raise HTTPException(status_code=404)

@router.get("/users/")
def get_user():
    return users