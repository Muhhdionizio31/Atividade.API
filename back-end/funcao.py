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
            print(f"Erro ao listar produtos do estoque: {erro}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(campo, novo_valor, id):
    try:
        conexao, cursor = conectar()
        cursor.execute(f"UPDATE produtos SET {campo} = %s WHERE id = %s", (novo_valor, id))
        conexao.commit()
        print(f"{campo.capitalize()} atualizado com sucesso!")
    except Exception as erro:
        print(f"Erro ao atualizar: {erro}")
    finally:
        conexao.close()
