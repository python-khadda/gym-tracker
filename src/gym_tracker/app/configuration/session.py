from typing import cast

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from gym_tracker import DatabaseSettings
from gym_tracker import database


def create_engine_handler(db: DatabaseSettings) -> Engine:
    if db.SQLALCHEMY_DATABASE_URI is None:
        raise RuntimeError("Database configuration not working")

    uri = cast(str, db.SQLALCHEMY_DATABASE_URI)
    return create_engine(url=uri)


def create_session_handler(db: DatabaseSettings) -> sessionmaker:
    engine = create_engine_handler(db)
    return sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
    )


def get_db():
    """Database session generator"""
    db = create_session_handler(database)()
    try:
        yield db
    finally:
        db.close()
