from typing import Dict, Any
from sqlalchemy import select
from abc import ABC, abstractmethod

from config.db import sync_engine, sync_session

class AbstractRepository(ABC):
    @abstractmethod
    def get_all(self, where):
        pass

    @abstractmethod
    def post(self, data: Dict[str, Any]):
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def get_all(self, where):
        with sync_engine.connect() as conn:
            query = select(self.model)

            if where.__str__(): query = query.where(where)

            result = conn.execute(query)

        return result.all()

    def post(self, data: Dict[str, Any]):
        with sync_session() as session:
            stmt = self.model(**data)
            result = session.add(stmt)
            session.commit()

        return result