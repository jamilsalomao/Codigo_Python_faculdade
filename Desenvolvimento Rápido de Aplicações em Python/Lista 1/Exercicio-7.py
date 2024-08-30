class Retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura

  def calcular_area(self):
    area = self.largura * self.altura
    print("A área do retângulo é:", area)

  def calcular_perimetro(self):
    perimetro = 2 * (self.largura + self.altura)
    print("O perímetro do retângulo é:", perimetro)

retangulo1 = Retangulo(8, 4)

retangulo1.calcular_area()
retangulo1.calcular_perimetro()