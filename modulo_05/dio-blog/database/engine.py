from sqlmodel import SQLModel, create_engine
from model import post_model

db_name = "blog.sqlite"
db_url = f"sqlite:///{db_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(db_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
