from sqlmodel import create_engine, SQLModel, Session
from app.settings import settings

engine = create_engine(settings.database_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Dependency
def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
