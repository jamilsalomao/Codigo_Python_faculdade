def crie_matriz(n_linhas:int, n_colunas:int, valor:int) -> list:
    matriz = list()
    for _ in range(n_linhas):
        linha = list()
        for _ in range(n_colunas):
            linha += [valor]
        matriz += [linha]
    return matriz

def adicionar_itens_matriz(cadeia_caracter:str, matriz:list) -> None:
    n_linhas:int = len(matriz)
    n_colunas:int = len(matriz[0])
    indice:int = 0
    tamanho_cadeia_caracter = len(cadeia_caracter)

    for coluna in range(n_colunas):
        i,j = 0, coluna
        while i < n_linhas and j >= 0 and indice < tamanho_cadeia_caracter:
            matriz[i][j] = cadeia_caracter[indice]
            indice += 1
            i += 1
            j -= 1
    for linha in range(1, n_linhas):
        i,j = linha, n_colunas - 1
        while i < n_linhas and j >= 0 and indice < tamanho_cadeia_caracter:
            matriz[i][j] = cadeia_caracter[indice]
            indice += 1
            i += 1
            j -= 1
def imprime_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

A = crie_matriz(3, 3, 0)
cadeia_caracter = "ABCDEFGHI"
adicionar_itens_matriz(cadeia_caracter, A)
imprime_matriz(A)

