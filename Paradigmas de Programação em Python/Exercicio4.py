def somar_numero_str(numero):
    string_numero = str(numero)
    soma = 0

    for letra in string_numero:
        soma += int(letra)
    print(soma)

numero = 123
somar_numero_str(numero)