from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Даниил, возраст: 18'}

@app.get('/users')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    user = f'Имя: {username}, возраст: {age}'
    users[new_id] = user
    return f"User {new_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(username: str, age: int, user_id: int) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User with id:{user_id} was deleted.'