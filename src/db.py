from sqlmodel import create_engine, SQLModel
from src.models import TarefaModel

_ = TarefaModel
engine = create_engine("sqlite:///db.sqlite", echo=True)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
