#conta quantas repeticoes foram encontradas de um elemento em uma matriz
def contaElementosMatriz(matriz, numero):
    contador = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (matriz[linha][coluna] == numero):
                contador += 1
    return contador

#trasnpoe uma matriz
def transposta(matriz):
    transposta = []
    #gerando transposta
    lin = len(matriz)
    col = len(matriz[0])
    for colT in range(col):
        linha = []
        for linT in range(lin):
            linha.append(0)
        transposta.append(linha)
    #Popular a transposta
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            transposta[coluna][linha] = matriz[linha][coluna]

    return transposta

#calcula a media de uma matriz
def mediaMatriz(matriz):
    contador = 0
    acumulador = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            acumulador += matriz[linha][coluna]
            contador += 1

    return acumulador/contador

#retorna o corredor que fez a menor volta, o tempo da menor volta e em que volta ela ocorreu
def kart(matriz):
    menorTempo = 0
    corredor = 0
    menorVolta = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if (menorTempo == 0 or matriz[linha][coluna] < menorTempo):
                menorTempo = matriz[linha][coluna]
                corredor = linha
                menorVolta = coluna

    return (corredor, menorTempo, menorVolta)

#Retorna todos os registros de um determinado setor
def buscaSetorial(matriz, setor):
    busca = []
    for linha in range(len(matriz)):
        if (matriz[linha][2] == setor):
            busca.append(matriz[linha])
    if (len(busca) == 0):
        return "Nenhum registro encontrado"
    return busca

#algoritmo de insertion sort
def ordenaInsercao(lista):
    for indice in range(1, len(lista)):
        valorAtual = lista[indice]
        posicao = indice
        while posicao > 0 and lista[posicao - 1] > valorAtual:
            lista[posicao] = lista[posicao - 1]
            posicao = posicao - 1
        lista[posicao] = valorAtual
    return lista

#Regiao de teste
def main():
    print(contaElementosMatriz([[1,2],[3,2], [3,2,2]],2))
    print(transposta([[1,2],[4,5],[7,8]]))
    print(mediaMatriz([[1,2],[4,5],[7,8]]))
    print(kart([[1,2,3,4,5,6],[1,2,3,0.5,4,5],[1,2,3,0.5,4,5], [1,2,3,0.3,4,5], [1,2,3,0.5,4,5], [1,2,3,0.5,4,5]]))
    print(buscaSetorial([
        ["adalberto", "111111", "Tees", "111"],
        ["adalberto", "111111", "contabilidade", "111"],
        ["adalberto", "111111", "HAHAS", "111"]],
        "contabilidade")
    )
    print(ordenaInsercao([5,6,3,7,8,10,11,2,1]))

if __name__ == "__main__":
    main()
