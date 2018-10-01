# soma os n primeiros numeros
def somaImpar(n):
    somatorio = 0
    for contador in range(n + 1):
        if (contador % 2 != 0):
            somatorio += contador
    return somatorio

#soma dos fatoriais de 1 a 10
def somaFatorial():
    somatorio = 1
    lista = [2,3,4,5,6,7,8,9,10]
    for numero in lista:
        fatorial = numero
        for numeroAnteriores in range(1,numero):
            fatorial *= numeroAnteriores
        somatorio += fatorial
    return somatorio

#soma o inverso dos numeroes de 1 a 10
def somaDivisoes(n):
    somatorio = 0
    for numero in range (1,n+1):
        somatorio += 1/numero
    return somatorio

#encontre o valor de uma determinada serie
def serie(n):
    valor = 0
    for numero in range(n+1):
        valor += ((-1)**numero)/(2*numero + 1)
    return 4*valor

#retorna os divisores de um numero
def divisores(n):
    divisores = []
    for numero in range(1, n+1):
        if (n % numero == 0):
            divisores.append(numero)
    return divisores

#conta o numero de aparicoes de uma letra em uma palavra
def contaLetra(frase, letra):
    contador = 0
    for letraNaFrase in frase:
        if letraNaFrase == letra:
            contador += 1
    return contador

#calcula uma sera onde o denominador e fatorial e o numerador segue uma regra
def serieFatorial():
    s = 0
    lista = [1,2,3,4,5,6,7,8,9,10]

    for numerador in lista:
        denominador = 1
        for numero in range(lista[-1*numerador],1, -1):
            denominador *= numero
        if (numerador % 2 != 0):
            numerador = -1*numerador
        s += numerador/denominador
    return s

#soma todos os primos de um determinado intervalo
def somaPrimos(limInf, limSup):
    listaDePrimos = []

    for numero in range(limInf, limSup + 1):
        primo = True
        for divisor in range(2, numero):
            if (numero % divisor == 0):
                primo = False
        if (primo == True):
            listaDePrimos.append(numero)

    return sum(listaDePrimos)

#verifica se a soma de todos os divisores e igual ao numero
def numeroPerfeito(n):
    divisores = []
    for numero in range(1, n):
        if (n % numero == 0):
            divisores.append(numero)

    if (sum(divisores) == n):
        return "Perfeito"
    return "Imperfeito"

#traduz uma palavra para a lingua do p
def linguaDoP(palavra):
    vogal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    posicao = 0
    traducaoP = list(palavra)
    for letra in list(palavra):
        if letra in vogal:
            traducaoP.insert(posicao+1, "p"+letra)
            posicao += 1
        posicao += 1
    return ''.join(traducaoP)

#calcula o numero final da bacterias apos sua reproducao
def bacteriaReproducao(inicial, noites):
    return inicial*(2**noites)

#diz qual e a melhor opcao de bacteria a ser escolhida
def quantidadeBacterias(listaDeBacterias):
    melhorEscolha = []
    iterador = 0
    for bacterias in listaDeBacterias:
        numeroFinal = bacteriaReproducao(bacterias[0], bacterias[1])
        if (len(melhorEscolha) == 0):
            melhorEscolha = [iterador, numeroFinal]
        elif (melhorEscolha[1] < numeroFinal):
            melhorEscolha = [iterador, numeroFinal]
        iterador += 1
    return melhorEscolha


#Regiao de teste
def main():
    print(somaImpar(7))
    print(somaFatorial())
    print(somaDivisoes(10))
    print(serie(10))
    print(divisores(10))
    print(contaLetra("mariana come banana", "n"))
    print(serieFatorial())
    print(somaPrimos(7,55))
    print(numeroPerfeito(6))
    print(linguaDoP("exemplo"))
    print(bacteriaReproducao(1,4))
    print(quantidadeBacterias([(145,4),(2,12),(3,3),(135,22)]))
    print(quantidadeBacterias([(2,5),(3,4)]))
    print(quantidadeBacterias([(2,1),(4,5),(30,4),(20,6),(2,8)]))

if __name__ == "__main__":
    main()
