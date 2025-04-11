from json import loads
from datetime import date, datetime
from sqlalchemy import select, and_

from model.todo import Todo
from prompts import create
from config.openai import client
from utils.service import Service
from repository.todo import TodoRepository

class TodoService(Service):
    def __init__(self):
        super().__init__(TodoRepository)

    def add(self, data):
        response = client.responses.create(
            model="gpt-4o-mini",
            input=create(data)
        )
        todo = loads(response.output_text)
        result = super().add(todo)

        return "Ваша Тудудушка добавлена успешно!" if len(result.__str__()) else "Что-то пошло не так при создании Тудудушки"

    def get_all(self):
        result = super().get_all()
        todos = "".join(
            f"""
            {index + 1})
            start: {result[index].start_datetime}
            finish: {result[index].finish_datetime}
            text: {result[index].text}
            """ for index in range(len(result)))

        return todos if len(result) > 0 else "Пока что Вы не создали ни одной Тудудушки :("

    def get_today(self):
        today = date.today()

        where = (
            and_(
                Todo.start_datetime <= datetime.combine(today, datetime.max.time()),
                Todo.start_datetime >= datetime.combine(today, datetime.min.time())
            )
        )

        result = super().get_all(where=where)

        todos = "".join(
            f"""
                    {index + 1})
                    start: {result[index].start_datetime}
                    finish: {result[index].finish_datetime}
                    text: {result[index].text}
                    """ for index in range(len(result)))

        return todos if len(result) > 0 else "Пока что Вы не создали ни одной Тудудушки :("