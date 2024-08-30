#Tive dificuldade para executar esse exercício e por isso recorri a internet para fazer, utilizei Stack Overflow e um site com guia para ajudar com classe abstrata
#Aqui está o código que eu consegui fazer com a ajuda deles
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * self.raio**2
    
retangulo1 = Retangulo(10, 4)
print("Área do retângulo:", retangulo1.area())

circulo1 = Circulo(7)
print("Área do círculo:", circulo1.area())

