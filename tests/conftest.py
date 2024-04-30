import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.base_class import Base


@pytest.fixture
def engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    return engine


@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()
