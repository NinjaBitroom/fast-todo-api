from sqlmodel import Field, SQLModel


class TarefaModel(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    titulo: str
    descricao: str
    completado: bool = Field(default=False)
