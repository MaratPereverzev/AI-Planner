from typing import Dict, Any
from sqlalchemy import select

from model.task import Task
from utils.repository import SQLAlchemyRepository
from config.db import sync_engine

class TaskRepository(SQLAlchemyRepository):
    model = Task

    def get_one(self, id: int):
        pass

    def post(self, data: Dict[str, Any]):
        pass