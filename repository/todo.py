from model.todo import Todo
from utils.repository import SQLAlchemyRepository

class TodoRepository(SQLAlchemyRepository):
    model = Todo


