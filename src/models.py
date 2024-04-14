from sqlmodel import Field as SQLModelField, SQLModel
from pydantic import BaseModel, Field as PydanticField


class TarefaModel(SQLModel, table=True):
    id: int = SQLModelField(primary_key=True, default=None)
    titulo: str
    descricao: str
    completado: bool = SQLModelField(default=False)


class RespostaOla(BaseModel):
    mensagem: str = PydanticField(examples=["Olá Gabriel"])
