def calcular_media(lista_numeros):

  if not lista_numeros:
    return None 

  soma = sum(lista_numeros)

  quantidade = len(lista_numeros)

  media = soma / quantidade

  return media

minha_lista = [10, 24, 3, 12, 34]
resultado = calcular_media(minha_lista)
print("A média é:", resultado)