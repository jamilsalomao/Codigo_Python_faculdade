class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        
carro1 = Carro("Toyota", "Yaris", 2024)

carro2 = Carro("Volkswagen", "Jetta", 2020)

carro1.detalhes()
print("----------------")
carro2.detalhes()