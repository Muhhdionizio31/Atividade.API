from fastapi import FastAPI
from funcao import adicionar_produtos, listar_produtos, atualizar_produto, buscar_produto, deletar_produto

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

@app.post("/produtos")
def add_produto(nome: str, categoria: str, preco: float, quantidade: int):
    adicionar_produtos(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!!! ✔"}

@app.get("/listar_produtos")
def exibir():
    produtos = listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({ 
            "id": linha[0], 
            "nome":linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
    return {"produtos": lista}

@app.put("/produtos/{id_produto}")
def atualizacao_produtos(id_produto: int, novo_nome: str,  nova_categoria: str, novo_preco: float, nova_quantidade: int):
    produto = buscar_produto(id_produto)
    if produto:
        atualizar_produto(id_produto, novo_nome, nova_categoria, novo_preco, nova_quantidade,)
        return{"mensagem": "Produto atualizado com sucesso!"}
    else:
        return{"erro": "Produto não encontrado"}

@app.delete("/produtos/{id_produto}")
def atualizacao_produtos(id_produto: int):
    deletar_produto(id_produto)
    produto = buscar_produto(id_produto)
    if produto:
        atualizar_produto(id_produto)
        return{"mensagem": "Produto deletado com sucesso!"}
    else:
        return{"erro": "Produto não encontrado"}
