from fastapi import FastAPI
from funcao import adicionar_produtos

# Rodar o FastApi
"""python -m uvicorn api:app --reload"""

# Testar api FastAPI
""" /dosc > Documentação Swagger """
""" /redoc > Documentação  redoc """

# Iniciar FstApi
app = FastAPI(title="Estoque de produtos")

# GET = Pegar / Listar
# POST = Criar / Enviar 
# PUT = Atualiar
# DELETE = Deletar

@app.get("/")
def home():
    return {"mensagem": "Cade meu produto?😑"}

@app.post("/filmes")
def add_produto(nome: str, categoria: str, preco: float, quantidade: int):
    adicionar_produtos(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!!! ✔"}
