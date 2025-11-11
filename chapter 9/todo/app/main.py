from fastapi import FastAPI, Request
from database import crud
import json


app = FastAPI()


@app.get('/')
async def list_tasks():
    try:
        return await crud.get_all_tasks()
    except Exception as e:
        return {'message' : f'could not resolve tasks. raised an exception : {e}.'}

@app.get('/title/{title}')
async def read_task_by_title(title: str):
    return await crud.get_task_by_title(title)


@app.get('/deadline/{deadline}')
async def read_task_by_title(deadline: str):
    return await crud.get_task_by_deadline(deadline)


@app.post('/create')
async def create_new_task(request: Request):
    payload = await request.json()
    result = await crud.create_task(payload.get('title'), payload.get('deadline'))
    if result:
        return await crud.get_task_by_title(payload.get('title'))
    else:
        return {'message' : 'task has not been created'}


@app.put('/update')
async def update_task(request: Request):
    payload = await request.json()
    task = await crud.get_task_by_title(payload.get('title'))

    if not task:
        return {'message' : 'task not found'}

    result = await crud.update_task(payload.get('title'), payload.get('deadline'), payload.get('new_title'))
    if result:
        return {'message' : 'task updated'}
    else:
        return {'message' : 'task did not update'}


@app.delete('/delete')
async def delete_task(request: Request):
    payload = await request.json()
    task = await crud.get_task_by_title(payload.get('title'))
    
    if not task:
        return {'message' : 'task not found'}
    
    result = await crud.delete_task(payload.get('title'))

    if result:
        return {'message' : 'task deleted'}
    else:
        return {'message' : 'task did not delete'}