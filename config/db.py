from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config.globals import config

sync_engine = create_engine(url=config.sync_db_url, echo=False)
sync_session = sessionmaker(sync_engine)

class Base(DeclarativeBase):
    pass