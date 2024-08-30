def fibonacci(n):
    sequencia = [1,1]
    while len(sequencia) < n:
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)
    return sequencia

n = 10
resultado = fibonacci(n)
print(resultado)




