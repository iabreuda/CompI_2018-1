from random import randint

#retorna o numero de anos que a populcao A demora paa alcancar a B
def populacao():
    populacaoA = 80000
    populacaoB = 200000
    anos = 0
    while populacaoB > populacaoA:
        anos += 1
        populacaoA += populacaoA*0.03
        populacaoB += populacaoB*0.015
    return anos

#retorna o numero de anos que a populcao A demora paa alcancar a B
#os argumentos sao passados supondo que pop B seja maior que pop A
def populacaoAlterada(populacaoA, populacaoB, taxaA, taxaB):
    anos = 0
    while populacaoB > populacaoA:
        anos += 1
        populacaoA += populacaoA*taxaA*0.01
        populacaoB += populacaoB*taxaB*0.01
    return anos

#Retorna o numero de vezes que um dado foi rolado ate cair um numero igual
def rodarDados():
    resultados = []
    randomizacoes = 0
    recorrente = False
    while (recorrente == False):
        randomizacoes += 1
        resultados.append(randint(1,6))
        if (
            resultados.count(1) > 1 or
            resultados.count(2) > 1 or
            resultados.count(3) > 1 or
            resultados.count(4) > 1 or
            resultados.count(5) > 1 or
            resultados.count(6) > 1
        ):
            recorrente = True

    return randomizacoes

#Informa a posicao de uma determinada letra na sua ocorrencia x
def posLetra(frase, letra, ocorrencia):
    iterador = 0
    indice = -1
    while (iterador < ocorrencia):
        indice = frase.index(letra, indice +1)
        iterador += 1
    return indice

#dado um numero, calcula a serie de fibonacci
def fibonacci(n):
    iteracoes = 0
    valorSerie = 0
    while iteracoes <= n:
        if (iteracoes == 0):
            nMenos1 = 0
            valor = 0
        elif (iteracoes == 1):
            nMenos2 = 0
            nMenos1 = 1
            valor = 1
        else:
            valor = nMenos1 + nMenos2
            nMenos2 = nMenos1
            nMenos1 = valor
        iteracoes += 1
    return valor

#calcula o fatorial de um numero
def fatorial(n):
    iteracoes = 1
    valor = 1
    while iteracoes <= n:
        valor *= iteracoes
        iteracoes += 1
    return valor

#verifica se um determinado numero e primo
def primo(n):
    iteracoes = 2
    while iteracoes < n:
        if (n % iteracoes == 0):
            return "Nao e Primo"
        iteracoes +=1
    return "Primo"

#verifica que peca esta faltando em um quebra-cabeca
def faltando(listaDePecas):
    iteracoes = 1
    listaDePecas.sort()
    tamanho = len(listaDePecas) + 1
    while iteracoes <= tamanho:
        if (listaDePecas.count(iteracoes) == 0):
            return iteracoes
        iteracoes += 1


#Regiao de teste
def main():
    print(populacao())
    print(populacaoAlterada(80000,200000,10,1.5))
    print(rodarDados())
    print(posLetra("mariana come banana", "a", 3))
    print(fibonacci(17))
    print(fatorial(4))
    print(primo(997))
    print(faltando([3,1]))
    print(faltando([1,2,3,5]))
    print(faltando([2,4,3]))

if __name__ == "__main__":
    main()
