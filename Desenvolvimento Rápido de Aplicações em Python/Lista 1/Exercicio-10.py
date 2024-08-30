def busca_linear(lista, numero):

  for i in range(len(lista)):
    
    if lista[i] == numero:
      
      return i

  
  return -1


minha_lista = [8, 7, 3, 9, 5, 2, 1]
numero_procurado = 2

resultado = busca_linear(minha_lista, numero_procurado)

if resultado != -1:
  print("O número", numero_procurado, "foi encontrado na posição", resultado)
else:
  print("O número", numero_procurado, "não foi encontrado na lista")