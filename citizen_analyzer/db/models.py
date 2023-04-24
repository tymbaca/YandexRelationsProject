import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, String, Integer, ForeignKey, Date

from citizen_analyzer import settings


class Base(DeclarativeBase):
    pass


class Import(Base):
    __tablename__ = "import"
    id: Mapped[int] = mapped_column(primary_key=True)


class Citizen(Base):
    __tablename__ = "citizen"
    id: Mapped[int] = mapped_column(primary_key=True)
    import_id: Mapped[int] = mapped_column(ForeignKey("import.id"), primary_key=True)
    town: Mapped[str] = mapped_column(String(256), nullable=False)
    street: Mapped[str] = mapped_column(String(256), nullable=False)
    building: Mapped[str] = mapped_column(String(256), nullable=False)
    apartment: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    birthdate: Mapped[datetime.date] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)


class Relation(Base):
    __tablename__ = "relation"
    import_id: Mapped[int] = mapped_column(ForeignKey("import.id"), primary_key=True)
    citizen_id = mapped_column(ForeignKey("citizen.id"), primary_key=True)
    relative_id = mapped_column(ForeignKey("citizen.id"), primary_key=True)
