from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy.orm import Mapped,mapped_column

Engine = create_engine("sqlite:///test.db")
Session = sessionmaker(bind=Engine)

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True,unique=True,autoincrement=True)

def up():
    Base.metadata.create_all(bind=Engine)

def down():
    Base.metadata.drop_all(bind=Engine)

from .models import Movie

down()
up()