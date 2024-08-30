#Assim como no exercício 5 que eu tive dúvidas para classe abstrata, eu utilizei da internet para me auxiliar no código
from abc import ABC, abstractmethod

class Produto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Venda(ABC):
    @abstractmethod
    def calcular_total(self):
        pass

    @abstractmethod
    def exibir_detalhes(self):
        pass

class VendaProduto(Venda):
    def __init__(self, produto, quantidade, preco):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def calcular_total(self):
        return self.quantidade * self.preco

    def exibir_detalhes(self):
        print("Venda de produto:")
        print(f"Produto: {self.produto.nome}")
        print(f"Descrição: {self.produto.descricao}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço unitário: R${self.preco:.2f}")
        print(f"Total: R${self.calcular_total():.2f}")
        print("-----------------------------------")

class VendaServico(Venda):
    def __init__(self, descricao_servico, quantidade_horas, valor_hora):
        self.descricao_servico = descricao_servico
        self.quantidade_horas = quantidade_horas
        self.valor_hora = valor_hora

    def calcular_total(self):
        return self.quantidade_horas * self.valor_hora

    def exibir_detalhes(self):
        print("Venda de serviço:")
        print(f"Serviço: {self.descricao_servico}")
        print(f"Quantidade de horas: {self.quantidade_horas}")
        print(f"Valor por hora: R${self.valor_hora:.2f}")
        print(f"Total: R${self.calcular_total():.2f}")

produto1 = Produto("Geladeira Electrolux", "Modelo mais recente")
venda_produto = VendaProduto(produto1, 2, 4000)

venda_servico = VendaServico("Manutenção de geladeira", 5, 90)

venda_produto.exibir_detalhes()
venda_servico.exibir_detalhes()