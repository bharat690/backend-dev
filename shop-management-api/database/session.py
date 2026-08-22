from typing import Generator
from sqlmodel import Session
from database.database import engine


def get_session() -> Generator[Session, None, None]:
    """
    Dependency that provides a database session.
    Ensures proper session cleanup after each request.
    """
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()