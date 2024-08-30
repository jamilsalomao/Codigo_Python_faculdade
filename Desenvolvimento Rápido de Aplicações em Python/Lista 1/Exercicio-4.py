numeros = []

for i in range(5):
    numero = int(input("Digite o {}º número: ".format(i+1)))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)