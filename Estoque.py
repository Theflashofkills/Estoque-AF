from Produto import Produto

def cadastrar_produto(estoque):
    id = int(input("ID: "))
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")
    numero_serie = input("Número de Série: ")
    local = input("Local de Armazenamento: ")
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(input("Valor Unitário: "))
    produto = Produto(id, descricao, categoria, numero_serie, local, quantidade, valor_unitario)
    estoque.inserir(produto)
    print("Produto cadastrado com sucesso!")

def remover_produto(estoque):
    id = int(input("ID do produto a remover: "))
    estoque.remover(id)
    print("Produto removido com sucesso!")

def atualizar_produto(estoque):
    id = int(input("ID do produto a atualizar: "))
    nodo = estoque.buscar(id)
    if nodo:
        produto = nodo.produto
        print(f"Produto atual: {produto.descricao}, {produto.categoria}, {produto.numero_serie}, {produto.local}, {produto.quantidade}, {produto.valor_unitario}")
        descricao = input("Nova Descrição (deixe em branco para não alterar): ")
        categoria = input("Nova Categoria (deixe em branco para não alterar): ")
        numero_serie = input("Novo Número de Série (deixe em branco para não alterar): ")
        local = input("Novo Local de Armazenamento (deixe em branco para não alterar): ")
        quantidade = input("Nova Quantidade (deixe em branco para não alterar): ")
        valor_unitario = input("Novo Valor Unitário (deixe em branco para não alterar): ")

        if descricao:
            produto.descricao = descricao
        if categoria:
            produto.categoria = categoria
        if numero_serie:
            produto.numero_serie = numero_serie
        if local:
            produto.local = local
        if quantidade:
            produto.quantidade = int(quantidade)
        if valor_unitario:
            produto.valor_unitario = float(valor_unitario)
        
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def consultar_produto(estoque):
    id = int(input("ID do produto a consultar: "))
    nodo = estoque.buscar(id)
    if nodo:
        produto = nodo.produto
        print(f"\nDescrição: {produto.descricao}")
        print(f"Categoria: {produto.categoria}")
        print(f"Número de Série: {produto.numero_serie}")
        print(f"Local: {produto.local}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Valor Unitário: R$ {produto.valor_unitario:.2f}")
    else:
        print("Produto não encontrado.")

def relatorio_estoque(estoque):
    produtos = estoque.em_ordem()
    if not produtos:
        print("Estoque vazio.")
        return

    while True:
        print("\n1. Produtos por Categoria")
        print("2. Ordenar por Descrição (A-Z)")
        print("3. Ordenar por Descrição (Z-A)")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            categorias = {}
            for produto in produtos:
                if produto.categoria not in categorias:
                    categorias[produto.categoria] = []
                categorias[produto.categoria].append(produto)
            for categoria, prods in categorias.items():
                print(f"\nCategoria: {categoria}")
                for prod in prods:
                    print(f"ID: {prod.id}, Descrição: {prod.descricao}, Quantidade: {prod.quantidade}, Valor Unitário: {prod.valor_unitario}")
        elif escolha == '2':
            produtos_ordenados = sorted(produtos, key=lambda p: p.descricao)
            for prod in produtos_ordenados:
                print(f"ID: {prod.id}, Descrição: {prod.descricao}, Quantidade: {prod.quantidade}, Valor Unitário: {prod.valor_unitario}")
        elif escolha == '3':
            produtos_ordenados = sorted(produtos, key=lambda p: p.descricao, reverse=True)
            for prod in produtos_ordenados:
                print(f"ID: {prod.id}, Descrição: {prod.descricao}, Quantidade: {prod.quantidade}, Valor Unitário: {prod.valor_unitario}")
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

