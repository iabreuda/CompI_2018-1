
#conta o numero de palavras em uma frase
def numeroDePalavras(frase):
    return len(str.split(frase))

#corta uma palavra que apareca na frase dentro dos limites informados
def cortaPalavra(frase, palavra, posicaoInicial, posicaoFinal):
    posicao = str.find(frase, palavra, posicaoInicial, posicaoFinal)
    if (posicao != -1): # Recursao para contar as ocorrencias
        return cortaPalavra(
            str.replace(frase, palavra, "", 1),
            palavra,
            posicaoInicial,
            posicaoFinal-len(palavra)
        )
    return frase

#substitui espacao por # em uma string
def substituiHash(frase):
    return str.join(
        "#",
        str.split(frase)
    )

#Remove tudo antes da primeira ocorrencia do caracter em uma string
def trechoString(frase, caractere):
    return str.strip(frase, caractere)

#Separa valor de uma tupla com 3 elements em um tupla numerica e outra de string
def separaTupla(tupla):
    tuplaString = ()
    tuplaNum = ()
    if (isinstance(tupla[0], str)):
        tuplaString += (tupla[0],)
    else:
        tuplaNum += (tupla[0],)

    if (isinstance(tupla[1], str)):
        tuplaString += (tupla[1],)
    else:
        tuplaNum += (tupla[1],)

    if (isinstance(tupla[2], str)):
        tuplaString += (tupla[2],)
    else:
        tuplaNum += (tupla[2],)

    return tuplaString, tuplaNum

#retorna uma lista com os valores intercalados
def intercalaLista(lista1, lista2):
    return [
        lista1[0],
        lista2[0],
        lista1[1],
        lista2[1],
        lista1[2],
        lista2[2]
    ]

#Regiao de teste
def main():
    print(numeroDePalavras(" Estou testando o numero de palavras "))
    print(cortaPalavra("Estou testando o numero testando de palavras", "testando", 2, 100))
    print(substituiHash(" Estou testando o numero de palavras "))
    print(trechoString("abcabc", "a"))
    print(separaTupla((1,"Teste",3)))
    print(intercalaLista([1,3,5],[2,4,6]))

if __name__ == "__main__":
    main()
