class Produto:
    def __init__(self, id, descricao, categoria, numero_serie, local, quantidade, valor_unitario):
        self.id = id
        self.descricao = descricao
        self.categoria = categoria
        self.numero_serie = numero_serie
        self.local = local
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def __str__(self):
        return f"ID: {self.id}, Descrição: {self.descricao}, Categoria: {self.categoria}, Número de Série: {self.numero_serie}, Local: {self.local}, Quantidade: {self.quantidade}, Valor Unitário: {self.valor_unitario}"
