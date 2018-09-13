#Inverte as palavras de uma frase
def inverterFrase(frase):
    lista = str.split(frase, " ")
    list.reverse(lista)
    return str.join(" ", lista)

#Ordena as palavras de uma frase por ordem alfabetica
def ordenaFrase(frase):
    lista = str.split(frase, " ")
    list.sort(lista)
    return str.join(" ", lista)

#Substitui todas as vogais por I
def tudoI(frase):
    for vogal in ["a", "e", "o", "u"]:
        frase = str.replace(frase, vogal, "i")
    return frase

#Adiciona uma palavra em uma posica, se a palavra a ser adicionada ja existe, coloque-a em caps
def mudaFrase(frase, palavra, posicao):
    lista = str.split(frase, " ")
    if (palavra in lista):
        indice = list.index(lista, palavra)
        lista[indice] = str.upper(lista[indice])
    else:
        list.insert(lista, posicao, palavra)
    return str.join(" ", lista)

#Informa o numero total de faltas que ocorreram no acumulado dos 3 jogos
def faltasCamp(jogo1, jogo2, jogo3):
    faltasJogo1 = jogo1[-1][0] + jogo1[-1][1]
    faltasJogo2 = jogo2[-1][0] + jogo2[-1][1]
    faltasJogo3 = jogo3[-1][0] + jogo3[-1][1]
    return faltasJogo1 + faltasJogo2 + faltasJogo3

#Inclui um numero e retorna uma lista ordenada apos a inclusao
def incluiNumero(lista, numero):
    list.insert(lista, 0, numero)
    list.sort(lista)
    return lista

#Informa elementos maiores que um limite em uma lista
def elementosMaiores(lista, limite):
    list.insert(lista, 0, limite)
    list.sort(lista)
    posicao = list.index(lista, limite)
    return lista[posicao+1:]

#Retorna o maior elemento de uma lista
def maiorElemento(lista):
    list.sort(lista)
    return lista[-1]

#Calcula a media da turma e informa as notas acima desta media
def mediaTurma(notas):
    media = sum(notas)/len(notas)
    return media, elementosMaiores(notas, media)

#Verifica se um colchao passa ou nao na porta dada as dimensoes dos objetos
def passaColchao(dimensoesColchao, alturaPorta, larguraPorta):
        '''
        Para que o colchao passe, ele precisa ter duas dimensoes
        menor que a maior dimessao da porta
        '''
        maiorDimensaoDaPorta = max(alturaPorta, larguraPorta)

        list.insert(dimensoesColchao, 0, maiorDimensaoDaPorta)
        list.sort(dimensoesColchao)
        list.reverse(dimensoesColchao)
        posicao = list.index(dimensoesColchao, maiorDimensaoDaPorta)

        if (len(dimensoesColchao[:posicao]) <= 1):
            return True
        return False

#Regiao de teste
def main():
    print(inverterFrase("eu gosto de chocolate"))
    print(ordenaFrase("eu gosto de doce"))
    print(tudoI("Levei meu cachorro para passear"))
    print(mudaFrase("Meu nome e ana", "ana", 1))
    print(mudaFrase("Meu nome e ana", "primeira", 1))
    print(faltasCamp(["Brasil", "Italia", [10,9]],["Brasil", "Espanha", [5,7]],["Italia", "Espanha", [7,8]]))
    print(incluiNumero([1,6,8,9,17,56], 7))
    print(elementosMaiores([56,17,11,8,5,3], 10))
    print(maiorElemento([1,6,8,100,9,17,56]))
    print(mediaTurma([10,10,8,8,6,6,4,4,2,2,0,0]))
    print(passaColchao([25,120,220],200,100))
    print(passaColchao([25,205,220],200,100))
    print(passaColchao([25,200,220],200,100))

if __name__ == "__main__":
    main()
