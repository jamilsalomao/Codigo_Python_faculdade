def contar_letras(frase, letra):

  frase_sem_espacos = frase.replace(" ", "")

  frase_minuscula = frase_sem_espacos.lower()
  letra_minuscula = letra.lower()

  contagem = frase_minuscula.count(letra_minuscula)

  return contagem

frase = input("Digite uma frase: ")
letra = input("Digite a letra que você quer contar: ")

resultado = contar_letras(frase, letra)

print("A letra", letra, "aparece", resultado, "vezes na frase.")