from app.database import crud
from datetime import datetime


async def get_all_tasks_or_not_found():
    tasks = await crud.get_all_tasks()
    if tasks is None:
        return {'message' : 'no task in database.'}
    else:
        return {'tasks' : tasks, 'message' : 'ok'}


async def get_task_by_title_or_not_found(title: str):
    task = await crud.get_task_by_title(title)
    if task is None:
        return {'message' : 'task not found.'}
    return {'tasks' : task, 'message' : 'ok'}


async def get_tasks_by_deadline_or_not_found(deadline: str):
    deadline = datetime.fromisoformat(deadline)

    tasks = await crud.get_tasks_by_deadline(deadline)
    if tasks is None:
        return {'message' : 'task not found.'}
    tasks = {'tasks' : tasks, 'message' : 'ok'}
    return tasks

async def create_task_or_fail(title: str, deadline: str):
    deadline = datetime.fromisoformat(deadline)
    result = await crud.create_task(title, deadline)
    if result:
        task = await get_task_by_title_or_not_found(title)
        return {'tasks' : task, 'message' : 'ok'}
    else:
        return {'message' : 'task has not been created'}


async def update_task_or_fail(title:str, deadline: str, new_title: str = None):
    deadline = datetime.fromisoformat(deadline)
    task = await crud.get_task_by_title(title)

    if not task:
        return {'message' : 'task not found'}

    result = await crud.update_task(title, deadline, new_title)
    if result:
        task = await crud.get_task_by_title(new_title)
        return {'tasks' : task, 'message' : 'task updated'}
    else:
        return {'message' : 'task did not update'}
    

async def delete_task_or_fail(title: str):
    task = await crud.get_task_by_title(title)
    
    if not task:
        return {'message' : 'task not found'}
    
    result = await crud.delete_task(title)

    if result:
        return {'message' : 'task deleted'}
    else:
        return {'message' : 'task did not delete'}