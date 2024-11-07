from .. import Base,Session
from sqlalchemy.orm import Mapped,mapped_column
from datetime import date

class Movie(Base):
    __tablename__ = "Movie"

    title:Mapped[str]
    director:Mapped[str]
    release_year:Mapped[int]
    rating:Mapped[float] = mapped_column(nullable=True)
