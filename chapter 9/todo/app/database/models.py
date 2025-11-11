from sqlalchemy import Table, Column, Integer, String, DateTime
from .connection import metadata, engine


tasks_table = Table(
    'tasks',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(100), unique=True),
    Column('deadline', DateTime) )


async def create_tasks_table():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

