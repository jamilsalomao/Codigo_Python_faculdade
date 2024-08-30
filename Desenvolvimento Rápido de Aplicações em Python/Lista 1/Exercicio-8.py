def selection_sort(lista):

  tamanho = len(lista)

  for i in range(tamanho):

    menor = i

    for j in range(i+1, tamanho):
      if lista[j] < lista[menor]:
        menor = j

    lista[i], lista[menor] = lista[menor], lista[i]

minha_lista = [38, 22, 47, 19, 8]
selection_sort(minha_lista)
print("Lista ordenada:", minha_lista)