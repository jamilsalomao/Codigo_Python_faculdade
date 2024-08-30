class Faturavel:
    def gerar_fatura(self):
        pass  

class Produto(Faturavel):
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def gerar_fatura(self):
        total = self.quantidade * self.preco_unitario
        return f"Fatura do produto {self.nome}:\nQuantidade: {self.quantidade}\nPreço unitário: R${self.preco_unitario:.2f}\nTotal: R${total:.2f}"

class Servico(Faturavel):
    def __init__(self, descricao, horas, preco_hora):
        self.descricao = descricao
        self.horas = horas
        self.preco_hora = preco_hora

    def gerar_fatura(self):
        total = self.horas * self.preco_hora
        return f"Fatura do serviço {self.descricao}:\nHoras: {self.horas}\nPreço por hora: R${self.preco_hora:.2f}\nTotal: R${total:.2f}"

# Exemplo de uso
produto1 = Produto("Geladeira Electrolux", 2, 4000)
servico1 = Servico("Manutenção de geladeira", 5, 90)

print(produto1.gerar_fatura())
print("-----------------------------------")
print(servico1.gerar_fatura())
