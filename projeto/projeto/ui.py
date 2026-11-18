from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 99:
            try:
                op = UI.menu()
                # Clientes
                if op == 1: UI.cliente_inserir()
                elif op == 2: UI.cliente_listar()
                elif op == 3: UI.cliente_atualizar()
                elif op == 4: UI.cliente_excluir()
                # Categorias
                elif op == 5: UI.categoria_inserir()
                elif op == 6: UI.categoria_listar()
                elif op == 7: UI.categoria_atualizar()
                elif op == 8: UI.categoria_excluir()
                # Produtos
                elif op == 9: UI.produto_inserir()
                elif op == 10: UI.produto_listar()
                elif op == 11: UI.produto_atualizar()
                elif op == 12: UI.produto_excluir()
                elif op == 13: UI.produto_reajustar()
                elif op == 99:
                    print("Saindo do sistema...")
                else:
                    print("Opção inválida!")
            except Exception as erro:
                print(f"Erro: {erro}")

    @staticmethod
    def menu():
        print("\n--- SISTEMA DE COMÉRCIO ELETRÔNICO (ADMIN) ---")
        print("--- Clientes ---")
        print("1-Inserir Cliente | 2-Listar Clientes | 3-Atualizar Cliente | 4-Excluir Cliente")
        print("--- Categorias ---")
        print("5-Inserir Categoria | 6-Listar Categorias | 7-Atualizar Categoria | 8-Excluir Categoria")
        print("--- Produtos ---")
        print("9-Inserir Produto | 10-Listar Produtos | 11-Atualizar Produto | 12-Excluir Produto")
        print("13-Reajustar Preços dos Produtos")
        print("99-Fim")
        return int(input("Informe uma opção: "))

    # Métodos de Cliente
    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)
        print("Cliente inserido com sucesso!")

    @staticmethod
    def cliente_listar():
        print("\n--- Lista de Clientes ---")
        for obj in Service.cliente_listar():
            print(obj)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)
        print("Cliente atualizado com sucesso!")

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)
        print("Cliente excluído com sucesso!")

    # Métodos de Categoria
    @staticmethod
    def categoria_inserir():
        descricao = input("Informe a descrição da categoria: ")
        Service.categoria_inserir(descricao)
        print("Categoria inserida com sucesso!")

    @staticmethod
    def categoria_listar():
        print("\n--- Lista de Categorias ---")
        for obj in Service.categoria_listar():
            print(obj)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("Informe a nova descrição: ")
        Service.categoria_atualizar(id, descricao)
        print("Categoria atualizada com sucesso!")

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        Service.categoria_excluir(id)
        print("Categoria excluída com sucesso!")

    # Métodos de Produto
    @staticmethod
    def produto_inserir():
        UI.categoria_listar()
        descricao = input("Informe a descrição do produto: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe o estoque: "))
        id_categoria = int(input("Informe o ID da categoria: "))
        Service.produto_inserir(descricao, preco, estoque, id_categoria)
        print("Produto inserido com sucesso!")

    @staticmethod
    def produto_listar():
        print("\n--- Lista de Produtos ---")
        for obj in Service.produto_listar():
            print(obj)

    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        UI.categoria_listar()
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o novo estoque: "))
        id_categoria = int(input("Informe o novo ID da categoria: "))
        Service.produto_atualizar(id, descricao, preco, estoque, id_categoria)
        print("Produto atualizado com sucesso!")

    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        Service.produto_excluir(id)
        print("Produto excluído com sucesso!")

    @staticmethod
    def produto_reajustar():
        percentual = float(input("Informe o percentual de reajuste (ex: 10 para +10%, -5 para -5%): "))
        Service.produto_reajustar(percentual)
        print("Preços reajustados com sucesso!")

if __name__ == "__main__":
    UI.main()