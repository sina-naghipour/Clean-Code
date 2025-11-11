from datetime import datetime
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from .connection import async_session
from .models import tasks_table


async def create_task(title: str, deadline: datetime):
    async with async_session() as session:
        query = insert(tasks_table).values(title=title, deadline=deadline)
        await session.execute(query)
        if await session.commit():
            return True
        return False
    

async def get_task_by_title(title: str):
    async with async_session() as session:

        query = select(tasks_table).where(tasks_table.c.title ==title)
        result = await session.execute(query)
        task = result.fetchone()
        if task:
            return {'title' : task.title, 'deadline' : task.deadline.isoformat()}
        else:
            return None    


async def get_tasks_by_deadline(deadline: datetime):
    async with async_session() as session:    

        query = select(tasks_table).where(tasks_table.c.deadline ==deadline)
        result = await session.execute(query)
        tasks = result.fetchall()
        if tasks:
            return [{'title' : task.title, 'deadline' : task.deadline.isoformat()} for task in tasks]
        else:
            return None    


async def get_all_tasks():
    async with async_session() as session:
        query = select(tasks_table)
        result = await session.execute(query)
        tasks = result.fetchall()
        tasks = [{
                'title' : task.title,
                'deadline' : task.deadline.isoformat(),
            } for task in tasks]
        return tasks


async def update_task(title: str, deadline: datetime, new_title = None):
    if new_title is None:
        new_title = title
    async with async_session() as session:
        query = update(tasks_table).where(tasks_table.c.title == title).values(title = new_title, deadline = datetime.fromisoformat(deadline))
        result = await session.execute(query)
        await session.commit()

        if result.rowcount > 0:
            return True
        else:
            return False


async def delete_task(title: str):
    async with async_session() as session:
        query = delete(tasks_table).where(tasks_table.c.title == title)
        result = await session.execute(query)
        await session.commit()
        
        if result.rowcount > 0:
            return True
        else:
            return False

