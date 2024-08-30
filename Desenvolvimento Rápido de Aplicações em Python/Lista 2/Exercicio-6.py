#Tive um pouco de dificuldade para realizar esse exercício e utilizei de base outro exercício para fazer o meu

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco,
            "valor_total": self.preco * self.quantidade,
            "data_validade": getattr(self, "data_validade", None)
        }

class Eletronico(Produto):
    def __init__(self, nome, preco, quantidade, garantia):
        super().__init__(nome, preco, quantidade)
        self.garantia = garantia

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Garantia: {self.garantia} anos")

class Alimento(Produto):
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade

    def exibir_detalhes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Validade: {self.data_validade}")

def imprimir_detalhes_estoque(produtos):
    for produto in produtos:
        info_produto = produto.calcular_valor_total()
        print(f"Produto: {info_produto['nome']}")
        print(f"Quantidade: {info_produto['quantidade']}")
        print(f"Preço unitário: R${info_produto['preco_unitario']:.2f}")
        print(f"Valor total: R${info_produto['valor_total']:.2f}")
        if info_produto['data_validade']:
            print(f"Validade: {info_produto['data_validade']}")
        if isinstance(produto, Eletronico):
            print(f"Garantia: {produto.garantia} anos")
        print("-----------------------------------")

eletronicos = [
    Eletronico("Monitor", 900, 10, 2),
    Eletronico("Notebook", 3500, 5, 3)
]
alimentos = [
    Alimento("Leite", 4, 20, "31/10/2024"),
    Alimento("Biscoito", 10, 15, "15/09/2024")
]

print("Detalhes dos eletrônicos:")
imprimir_detalhes_estoque(eletronicos)

print("\nDetalhes dos alimentos:")
imprimir_detalhes_estoque(alimentos)