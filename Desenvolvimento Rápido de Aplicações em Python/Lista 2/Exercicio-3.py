class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.cargo}.")

pessoa1 = Pessoa("Jamil", 21)
pessoa1.cumprimentar()

funcionario1 = Funcionario("Jeff", 35, "Programador")
funcionario1.cumprimentar()