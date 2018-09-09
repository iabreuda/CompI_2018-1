from aula1 import media #importa a funcao de media da aula 1
import math

#Retorna a media de 4 numeros usando a funcao passada
def media4Numeros(n1, n2, n3, n4):
    media1 = media(n1, n2)
    media2 = media(n3, n4)
    return media(media1, media2)

#Numero maximo de um produto que pode ser comprado e seu troco dado preco e saldo
def maximizaCompra(preco, saldo):
    troco = saldo % preco
    quantidade = (saldo - troco)/ preco
    return quantidade, troco

#hipotenuza de um triangulo sabendo os catetos
def hipotenuza(catA, catB):
    return math.hypot(catA, catB)

#distancia entre dois pontos de um plano
def distancia(x1, y1, x2, y2):
    return math.sqrt(
        (x1 - x2)**2 +
        (y1 - y2)**2
    )

#perimetro de um triangulo retangulo sabendo seus catetos
def perimetro(catA, catB):
    return hipotenuza(catA, catB) + catA + catB

#soma quadratica de senos e cossenos sabendo o angulo
def quadSinCos(angulo):
    return math.sin(angulo)**2 + math.cos(angulo)**2

#comprimento do circulo de um raio informado
def comprimentoCirculo(raio):
    return 2*3.1416*raio

#numero de voltas em uma pista sabendo o raio e a distancia percorrida
def numeroDeVoltas(raio, distancia):
    return distancia/(comprimentoCirculo(raio))

#delta de uma equacao de segundo grau
def delta(a, b, c):
    return (b**2) - (4*a*c)

#calculo da raiz quadrada que nao pode ser complexa
def calculoRaizPositiva(a, b, c):
    deltaValor = delta(a,b,c)
    return (
        (-1*b + math.sqrt(deltaValor))/(2*a),
        (-1*b - math.sqrt(deltaValor))/(2*a)
    )

#area de um segmento circular sabendo o raio e o angulo que por padrao e 360
def areaCircular(raio, angulo=360):
    return (angulo*(3.1416*(raio**2)))/360

#numero de termos em um PA
def numeroDeTermos(valorInicial, valorFinal, razao):
    return (
        ((valorFinal - valorInicial)/razao) + 1
    )

#soma de uma PA
def somaPA(valorInicial, valorFinal, nTermos):
    return (
        ((valorFinal - valorInicial)*nTermos)/2
    )

#calculo completo de uma PA
def PA(valorInicial, valorFinal, razao):
    return (
        somaPA(
            valorInicial,
            valorFinal,
            numeroDeTermos(
                valorInicial,
                valorFinal,
                razao
            )
        )
    )

#numero maximo de bolos que podem ser feitos dado os ingredientes
def bolo(trigo, ovo, leite):
    sobraTrigo = trigo % 2
    sobraOvo = ovo % 3
    sobraLeite = leite % 5

    maxTrigo = (trigo - sobraTrigo)/2
    maxOvo = (ovo - sobraOvo)/3
    maxLeite = (leite - sobraLeite)/5

    nMaxBolo = maxTrigo #Comportamento default e definir o Trigo

    if (maxOvo < nMaxBolo):
        nMaxBolo = maxOvo
    if (maxLeite < nMaxBolo):
        nMaxBolo = maxLeite

    return nMaxBolo

#Regiao de teste
def main():
    print(media4Numeros(5,7,16,12))
    print(maximizaCompra(1, 10.5))
    print(hipotenuza(3, 4))
    print(distancia(4, 0, 6 ,6))
    print(perimetro(4, 3))
    print(quadSinCos(157))
    print(comprimentoCirculo(10))
    print(numeroDeVoltas(10,62))
    print(delta(1 ,3, 2))
    print(calculoRaizPositiva(1 ,3, 2))
    print(areaCircular(10,180))
    print(PA(-10,35,3))
    print(bolo(4,6,10))
    print(bolo(4,6,9))
if __name__ == "__main__":
    main()
