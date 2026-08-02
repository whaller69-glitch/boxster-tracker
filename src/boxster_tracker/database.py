from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


def create_database(db_path: Path):
    engine = create_engine(
        f"sqlite:///{db_path}",
        echo=False,
    )

    Base.metadata.create_all(engine)

    return engine


def create_session_factory(engine):
    return sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )


def get_session(db_path: Path):
    engine = create_database(db_path)

    factory = create_session_factory(engine)

    return factory()

