from typing import Literal, TypedDict

from fastapi import FastAPI, Form
from sqlmodel import Session

from src.db import engine
from src.models import TarefaModel

app = FastAPI()


class RespostaOlaMundo(TypedDict):
    mensagem: Literal["Olá Mundo!"]


class RespostaOla(TypedDict):
    mensagem: str


class RespostaTarefaDeletada(TypedDict):
    mensagem: Literal["Tarefa deletada com sucesso!"]


@app.get("/")
def raiz() -> RespostaOlaMundo:
    """Olá Mundo!"""
    return {"mensagem": "Olá Mundo!"}


@app.get("/ola/{nome}")
def falar_ola(nome: str) -> RespostaOla:
    """Olá!"""
    return {"mensagem": f"Olá {nome}"}


@app.post("/tarefa/")
def criar_tarefa(titulo: str = Form(), descricao: str = Form()) -> TarefaModel:
    """Criar uma nova tarefa."""
    with Session(engine) as session:
        novo_todo = TarefaModel(
            titulo=titulo,
            descricao=descricao,
            completado=False
        )
        session.add(novo_todo)
        session.commit()
        session.refresh(novo_todo)
        return novo_todo


@app.get("/tarefa/")
def listar_tarefas() -> list[TarefaModel]:
    """Listar todas as tarefas."""
    with Session(engine) as session:
        todos = session.query(TarefaModel).all()
        return todos


@app.get("/tarefa/{tarefa_id}")
def ler_tarefa_por_id(tarefa_id: int) -> TarefaModel | None:
    """Ler uma tarefa por ID."""
    with Session(engine) as session:
        todo = session.get(TarefaModel, tarefa_id)
        return todo


@app.put("/tarefa/{todo_id}")
def atualizar_tarefa(
        todo_id: int,
        titulo: str | None = Form(default=None),
        descricao: str | None = Form(default=None),
        completado: bool | None = Form(default=None)
) -> TarefaModel | None:
    """Atualizar uma tarefa."""
    with Session(engine) as session:
        tarefa = session.get(TarefaModel, todo_id)
        tarefa.titulo = titulo if titulo is not None else tarefa.titulo
        tarefa.descricao = descricao if descricao is not None else tarefa.descricao
        tarefa.completado = completado if completado is not None else tarefa.completado
        session.add(tarefa)
        session.commit()
        session.refresh(tarefa)
        return tarefa


@app.delete("/tarefa/{todo_id}")
def deletar_tarefa(todo_id: int) -> RespostaTarefaDeletada:
    """Deletar uma tarefa."""
    with Session(engine) as session:
        tarefa = session.get(TarefaModel, todo_id)
        session.delete(tarefa)
        session.commit()
        return {"mensagem": "Tarefa deletada com sucesso!"}
