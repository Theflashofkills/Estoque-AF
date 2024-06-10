class Produto:
    def __init__(self, id, descricao, categoria, numero_serie, local, quantidade, valor_unitario):
        self.id = id
        self.descricao = descricao
        self.categoria = categoria
        self.numero_serie = numero_serie
        self.local = local
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

class NodoArvore:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = NodoArvore(produto)
        else:
            self._inserir(self.raiz, produto)

    def _inserir(self, nodo, produto):
        if produto.id < nodo.produto.id:
            if nodo.esquerda is None:
                nodo.esquerda = NodoArvore(produto)
            else:
                self._inserir(nodo.esquerda, produto)
        else:
            if nodo.direita is None:
                nodo.direita = NodoArvore(produto)
            else:
                self._inserir(nodo.direita, produto)

    def buscar(self, id):
        return self._buscar(self.raiz, id)

    def _buscar(self, nodo, id):
        if nodo is None or nodo.produto.id == id:
            return nodo
        if id < nodo.produto.id:
            return self._buscar(nodo.esquerda, id)
        return self._buscar(nodo.direita, id)

    def em_ordem(self):
        produtos = []
        self._em_ordem(self.raiz, produtos)
        return produtos

    def _em_ordem(self, nodo, produtos):
        if nodo:
            self._em_ordem(nodo.esquerda, produtos)
            produtos.append(nodo.produto)
            self._em_ordem(nodo.direita, produtos)

    def remover(self, id):
        self.raiz, _ = self._remover(self.raiz, id)

    def _remover(self, nodo, id):
        if nodo is None:
            return nodo, None
        if id < nodo.produto.id:
            nodo.esquerda, removido = self._remover(nodo.esquerda, id)
        elif id > nodo.produto.id:
            nodo.direita, removido = self._remover(nodo.direita, id)
        else:
            if nodo.esquerda is None:
                return nodo.direita, nodo
            elif nodo.direita is None:
                return nodo.esquerda, nodo
            temp = self._min_value_node(nodo.direita)
            nodo.produto = temp.produto
            nodo.direita, _ = self._remover(nodo.direita, temp.produto.id)
        return nodo, nodo

    def _min_value_node(self, nodo):
        atual = nodo
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

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
        print(f"Produto: {produto.descricao}, {produto.categoria}, {produto.numero_serie}, {produto.local}, {produto.quantidade}, {produto.valor_unitario}")
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

if __name__ == "__main__":
    menu()
