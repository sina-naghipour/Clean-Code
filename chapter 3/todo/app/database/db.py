from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.future import select
from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, update, delete, insert

def create_database_engine(database_url: str):
    engine = create_async_engine(database_url, echo=True, pool_size=10, max_overflow=20)
    return engine


def create_database_session(engine: object):
    session = sessionmaker(class_=AsyncSession, expire_on_commit=False, bind=engine)
    return session


async def get_database(session):
    database = session()
    try:
        yield database
    finally:
        await database.close()


# now we are connected to the database, now we want to be able to do CRUD operations.

# the sole reason of this function is to create a task and thats it.
engine = create_async_engine('postgresql+asyncpg://postgres:toor@localhost:5432/todo')
metadata = MetaData()
async_session = create_database_session(engine)

tasks_table = Table(
    'tasks',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(100), unique=True),
    Column('deadline', DateTime) )

async def create_tasks_table():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


async def create_task(title: str, deadline: str):
    async with async_session() as session:
        query = insert(tasks_table).values(title=title, deadline=datetime.fromisoformat(deadline))
        await session.execute(query)
        await session.commit()
        return True

async def get_task_by_title(title: str):
    async with async_session() as session:

        query = select(tasks_table).where(tasks_table.c.title ==title)
        result = await session.execute(query)
        task = result.fetchone()
        if task:
            return {'title' : task.title, 'deadline' : task.deadline.isoformat()}
        else:
            return None    


async def get_task_by_deadline(deadline: str):
    async with async_session() as session:    

        query = select(tasks_table).where(tasks_table.c.deadline ==datetime.fromisoformat(deadline))
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

