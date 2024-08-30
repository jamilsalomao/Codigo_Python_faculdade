def insertion_sort(lista):

  for i in range(1, len(lista)):
    valor_atual = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > valor_atual:
      lista[j+1] = lista[j]
      j -= 1
    lista[j+1] = valor_atual
minha_lista = [69, 2, 32, 20, 17]
insertion_sort(minha_lista)
print("Lista ordenada:", minha_lista)