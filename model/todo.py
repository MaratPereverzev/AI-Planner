from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from config.db import Base

class Todo(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    start_datetime =  mapped_column(
        TIMESTAMP(timezone=False),
        nullable=False
    )
    finish_datetime = mapped_column(
        TIMESTAMP(timezone=False),
        nullable=False
    )