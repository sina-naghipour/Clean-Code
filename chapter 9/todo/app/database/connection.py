from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData


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


engine = create_database_engine('postgresql+asyncpg://postgres:toor@localhost:5432/todo')
metadata = MetaData()
async_session = create_database_session(engine)