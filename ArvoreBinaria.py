from NodoArvore import NodoArvore


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