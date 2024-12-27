from datetime import datetime

from sqlalchemy import BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    chat_id: Mapped[BigInteger] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    username: Mapped[Text] = mapped_column(Text, default=None)
    full_name: Mapped[Text] = mapped_column(Text, default=None)
    date_register: Mapped[datetime] = mapped_column(server_default=func.now())
