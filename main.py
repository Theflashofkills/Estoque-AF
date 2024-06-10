from FuncoesEstoque import (
    cadastrar_produto,
    remover_produto,
    atualizar_produto,
    consultar_produto,
    relatorio_estoque,
)
from ArvoreBinaria import ArvoreBinaria


def menu():
    estoque = ArvoreBinaria()
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Remover Produto")
        print("3. Atualizar Produto")
        print("4. Consultar Produto")
        print("5. Relatório de Estoque")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_produto(estoque)
        elif escolha == '2':
            remover_produto(estoque)
        elif escolha == '3':
            atualizar_produto(estoque)
        elif escolha == '4':
            consultar_produto(estoque)
        elif escolha == '5':
            relatorio_estoque(estoque)
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
