from typing import Dict, Any

from utils.repository import AbstractRepository

class Service:
    repository: AbstractRepository

    def __init__(self, repository: AbstractRepository):
        self.repository = repository()

    def add(self, data: Dict[str, Any]):
        return self.repository.post(data)

    def get_all(self, where):
        return self.repository.get_all(where)