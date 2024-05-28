def palindromo(palavra):
    return palavra == palavra[::-1]

palavra = "ovo"
if palindromo(palavra):
    print(f"{palavra} é um palíndromo." )
else:
    print(f"{palavra} não é um palíndromo.")