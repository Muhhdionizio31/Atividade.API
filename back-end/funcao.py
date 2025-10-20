from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY ,
                    nome VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50),
                    preco NUMERIC,
                    quantidade INT             
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()

def adicionar_produtos(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(

                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES(%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)

            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir produto no estoque: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(

                "SELECT * FROM produtos ORDER BY id",
                ()

            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar produto do estoque: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(id_produto, novo_nome, nova_categoria, novo_preco, novo_quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
           "UPDATE produtos SET nome = %s, categoria = %s, preco = %s, quantidade = %s WHERE id = %s",
                (novo_nome, nova_categoria, novo_preco, novo_quantidade, id_produto) 
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def buscar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos WHERE id = %s", (id_produto,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao tentar buscar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "DELETE FROM produtos WHERE id = %s",
                (id_produto,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar produto do estoque: {erro}")
        finally:
            cursor.close()
            conexao.close()
