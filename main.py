from crud import *
import login

if login.fazer_login():

    while True:

        print("\n===== SISTEMA =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            pro_nome = input("Nome do produto: ")
            pro_descricao = input("Descrição do produto: ")
            pro_marca = input("Marca do produto: ")
            pro_preco = input("Preço do produto: ").replace(",", ".")
            pro_data_validade = input("Data de validade (YYYY-MM-DD): ")
            cadastrar_produto(pro_nome, pro_descricao, pro_marca, pro_preco, pro_data_validade)
            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            produtos = listar_produtos()
            if produtos:
                for produto in produtos:
                    print(produto)
            else:
                print("Nenhum produto cadastrado.")

        elif opcao == "3":
            pro_id = input("ID do produto a atualizar: ")
            pro_nome = input("Novo nome: ")
            pro_descricao = input("Nova descrição: ")
            pro_marca = input("Nova marca: ")
            pro_preco = input("Novo preço: ").replace(",", ".")
            pro_data_validade = input("Nova data de validade (YYYY-MM-DD): ")
            atualizar_produto(pro_id, pro_nome, pro_descricao, pro_marca, pro_preco, pro_data_validade)
            print("Produto atualizado com sucesso!")

        elif opcao == "4":
            pro_id = input("ID do produto a deletar: ")
            deletar_produto(pro_id)
            print("Produto deletado com sucesso!")

        elif opcao == "5":
            break