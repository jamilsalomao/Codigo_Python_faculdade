class Reserva:
    def __init__(self, codigo_reserva, data, hora):
        self.codigo_reserva = codigo_reserva
        self.data = data
        self.hora = hora

class ReservaHotel(Reserva):
    def __init__(self, codigo_reserva, data, hora, nome_hotel, noites):
        super().__init__(codigo_reserva, data, hora)
        self.nome_hotel = nome_hotel
        self.noites = noites

    def exibir_detalhes(self):
        print("Reserva de Hotel:")
        print(f"Código: {self.codigo_reserva}")
        print(f"Data: {self.data}")
        print(f"Check-In: {self.hora}")
        print(f"Hotel: {self.nome_hotel}")
        print(f"Noites: {self.noites}")

    def calcular_custo(self, preco_por_noite):
        return self.noites * preco_por_noite

class ReservaVoo(Reserva):
    def __init__(self, codigo_reserva, data, hora, numero_voo, classe):
        super().__init__(codigo_reserva, data, hora)
        self.numero_voo = numero_voo
        self.classe = classe

    def exibir_detalhes(self):
        print("Reserva de Voo:")
        print(f"Código: {self.codigo_reserva}")
        print(f"Data: {self.data}")
        print(f"hora: {self.hora}")
        print(f"Número do Voo: {self.numero_voo}")
        print(f"Classe: {self.classe}")

    def calcular_custo(self, preco_por_classe):
        
        return preco_por_classe

reserva_hotel = ReservaHotel("HL123", "21-12-2024", "12:00", "Hotel Barra", 5)
reserva_voo = ReservaVoo("RV454", "21-12-2024", "8:00", "GO123", "Executiva")

reserva_hotel.exibir_detalhes()
custo_hotel = reserva_hotel.calcular_custo(150)
print(f"Custo total do hotel: R${custo_hotel}")
print("-----------------------------------")

reserva_voo.exibir_detalhes()
custo_voo = reserva_voo.calcular_custo(800)
print(f"Custo total do voo: R${custo_voo}")
print("-----------------------------------")

custo_total = custo_hotel + custo_voo
print(f"Custo total da viagem: R${custo_total:.2f}")