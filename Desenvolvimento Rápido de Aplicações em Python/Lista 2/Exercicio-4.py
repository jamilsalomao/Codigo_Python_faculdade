class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def exibir_endereco(self):
        print(f"Endereço de {self.nome}:")
        print(f"Rua: {self.endereco.rua}")
        print(f"Número: {self.endereco.numero}")
        print(f"Cidade: {self.endereco.cidade}")
        
endereco1 = Endereco("Avenida Olegario Maciel", 1475, "Rio de Janeiro")

pessoa1 = Pessoa("Jamil", endereco1)

pessoa1.exibir_endereco()