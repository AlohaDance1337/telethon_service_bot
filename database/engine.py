from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from tools import config

engine = create_async_engine(config.postgres_dsn)
async_session = async_sessionmaker(engine)
