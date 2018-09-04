# Retorna a area de um Retangulo dado seus 2 lados
def areaRetangulo(ladoA, ladoB):
    return ladoA * ladoB

# Retorna a area de um anel
def areaAnel(raioExterno, raioInterno):
    pi = 3.14
    if (raioExterno < raioInterno):
        return "O Raio externo deve ser maior que o raio interno"
    area = pi*((raioExterno**2) - (raioInterno**2))
    return area

#Informa o quociente e o resto de uma divisao
def divisao(dividendo, divisor):
    resto = dividendo % divisor
    quociente = (dividendo - resto)/divisor
    return quociente, resto

#Retorna o valor do ponto em y
def ordenada(a, b, c, abscissa):
    return a*(abscissa**2) + b*abscissa + c

#Calcula a gorjeta de um garcon
def gorjeta(conta):
    return conta * 0.1

#Calcula a media aritmetica
def media(primeiroValor, segundoValor):
    return (primeiroValor + segundoValor)/2

#Calcula a media ponderada
def mediaPonderada(primeiroValor, primeiroPeso, segundoValor, segundoPeso):
    return (primeiroPeso*primeiroValor + segundoPeso*segundoValor)/(primeiroPeso + segundoPeso)

#Calcula a distancia de deslocamento causada pela correnteza
def correnteza(velocidadeCorrenteza, larguraRio, velocidadeBarco):
      tempoDeTravecia = larguraRio / velocidadeBarco
      return velocidadeCorrenteza*tempoDeTravecia

#Retorna o saldo final, o juros e dado em valor de porcentagem
def juros(saldoInicial, meses, jurosMensal):
    return saldoInicial*(1 + (jurosMensal/100)*meses)

#Calcula a PG por 2 diferentes metodos
def progressaoGeometrica(n, q):
    pg = 1/(1-q)
    aAtual = 1
    soma = 1
    for i in range(1, n+1):
        aAnterior = aAtual
        aAtual = aAnterior*q
        soma += aAtual
    return pg, soma

#O formato da data deve ser hh,mm,ss
#Calcula a diferenca de tempo
def tempoDeProva(tPartida, tChegada):
    hPartida = int(tPartida[:2])
    mPartida = int(tPartida[3:5])
    sPartida = int(tPartida[6:8])
    hChegada = int(tChegada[:2])
    mChegada = int(tChegada[3:5])
    sChegada = int(tChegada[6:8])
    separadorHMPartida = tPartida[2]
    separadarHMChegada = tChegada[2]
    separadorMSPartida = tPartida[5]
    separadarMSChegada = tChegada[5]
    #Validacao pra verificar se respeita o formato
    if (separadarHMChegada != "," or
        separadorHMPartida != "," or
        separadarMSChegada != "," or
        separadorMSPartida != ","):
        return "Caracter de separacao invalido"
    if (hPartida < 0 or hPartida > 24) and (hChegada < 0 or hChegada > 24):
        return "O valor da hora deve estar entre 0 e 24"
    if (mPartida < 0 or mPartida > 60) and (mChegada < 0 or mChegada > 60):
        return "O valor do minuto deve estar entre 0 e 60"
    if (sPartida < 0 or sPartida > 60) and (sChegada < 0 or sChegada > 60):
        return "O valor do segundo deve estar entre 0 e 60"
    #Validacao para garantir que a A chegada ocorre depois da partida
    if (
        (hChegada < hPartida) or
        (hChegada == hPartida and mChegada < mPartida) or
        (hChegada == hPartida and mChegada == mPartida and sChegada < sPartida)
    ):
        return "O cara nao pode chegar antes da partida"

    tempoEmSegundos = (hChegada - hPartida)*3600 + (mChegada - mPartida)*60 + (sChegada - sPartida)
    restoDeHoras = tempoEmSegundos % 3600
    horas = (tempoEmSegundos-restoDeHoras)/3600
    restoDeMinutos = restoDeHoras % 60
    minutos = (restoDeHoras - restoDeMinutos)/60
    segundos = restoDeMinutos
    return (
        str(horas) + " hora(s) " +
        str(minutos) + " minuto(s) " +
        str(segundos) + " segundo(s)"
    )

#Retorna o valor por pessoa apos o acrescimo da gorjeta
def divisaoDeConta(valorDaConta, numDePessoas):
    valorFinal = valorDaConta*1.1
    return valorFinal/numDePessoas

#Retorna a area superficial de um cubo
def areaSupCub(aresta):
    return 6*(aresta**2)

#Regiao de teste
def main():
    print(areaRetangulo(5,7))
    print(areaRetangulo(15,2))
    print(areaRetangulo(500,700))
    print(areaRetangulo(5,0))
    print(areaAnel(2,1))
    print(areaAnel(15,5))
    print(areaAnel(100,0))
    print(divisao(7,3))
    print(divisao(15,5))
    print(divisao(119,10))
    print(ordenada(1,2,3,0))
    print(ordenada(1,2,3,1))
    print(gorjeta(36.5))
    print(media(-5,7))
    print(media(2,-2))
    print(media(5,5))
    print(media(3,4))
    print(media(3.0,4.0))
    print(mediaPonderada(3,2,4,3))
    print(correnteza(10,20,5))
    print(juros(100,10,1))
    print(progressaoGeometrica(10000000,0.2))
    print(tempoDeProva("12,00,00", "13,00,00"))
    print(tempoDeProva("25,00,00", "13,00,00"))
    print(tempoDeProva("09,57,18", "17,10,40"))
    print(divisaoDeConta(100,5))
    print(areaSupCub(2))

if __name__ == "__main__":
    main()
