from typing import TypedDict, Literal


class RespostaOlaMundo(TypedDict):
    mensagem: Literal["Olá Mundo!"]


class RespostaTarefaDeletada(TypedDict):
    mensagem: Literal["Tarefa deletada com sucesso!"]
