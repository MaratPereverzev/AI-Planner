from abc import ABC, abstractmethod
from typing import Dict, Any
from sqlalchemy import select

from config.db import sync_engine
from model.task import Task


class AbstractRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_one(self, id: int):
        pass

    @abstractmethod
    def post(self, data: Dict[str, Any]):
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def get_all(self):
        with sync_engine.connect() as conn:
            query = select(self.model)
            result = conn.execute(query)

        return result.all()

    def get_one(self, id: int):
        pass

    def post(self, data: Dict[str, Any]):
        pass