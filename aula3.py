import math

# Retorna o valor absoluto
def valAbsoluto(valor):
    return abs(valor)

#calcula a raiz 
def raiz(a, b, c):
    delta = (b**2) - (4*a*c)
    if (delta == 0):
        raiz = -1*b/2*a
        return {'NdeRaizes':1, "raiz": raiz}
    elif (delta > 0):
        raiz1 = ((-1*b - math.sqrt(delta)) / 2*a)
        raiz2 = ((-1*b + math.sqrt(delta)) / 2*a)
        return {'NdeRaizes':2, "raiz1": raiz1, "raiz2": raiz2}
    else:
        return {'NdeRaizes':0}
    return

def gagueira(palavra):
    return (palavra + palavra + palavra)

def funcao(x):
    if (x < 0):
        return None
    elif (x < 2):
        return x
    elif (x <= 3.5):
        return 2
    elif (x <= 5):
        return 3
    else:
        return x**2 - 10*x + 28

def maxMin(x, y):
    if (x == y):
        return None
    elif (x < y):
        return {'Max':y, 'Min':x}
    else:
        return {'Max':x, 'Min':y}

def meia(idade, carteirinha):
    if ((idade <= 21 or idade >= 65) or carteirinha == True):
        return "Meia Entrada"
    else:
        return "Inteira"

def classificacao(Cv, Ce, Cs, Fv, Fe, Fs):
    pontosC = 3*Cv + Ce
    pontosE = 3*Fv + Fe
    if (pontosC == pontosE):
        if (Cs > Fs):
            return "Cormengo"
        elif (Fs > Cs):
            return "Flaminthians"
        else:
            return "Empate geral"
    elif (pontosC > pontosE):
        return "Cormengo"
    else:
        return "Flaminthians"

def aviao(comp, qtd, qtdcomp):
    x = comp*qtdcomp
    if (x > qtd):
        return "Insuficiente"
    else:
        return "Suficiente"


#Regiao de teste
def main():
    print(valAbsoluto(-14))
    print(raiz(1,10,1))
    print(gagueira("teste"))
    print(maxMin(3,7))
    print(meia(70, True))
    print(classificacao(10,5,18,11,2,18))
    print(classificacao(10,5,18,11,1,18))
    print(classificacao(9,5,-1,10,2,10))
    print(aviao(10,100,10))
    print(aviao(10,90,10))
    print(aviao(5,40,2))
if __name__ == "__main__":
    main()
