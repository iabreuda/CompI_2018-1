import math
import datetime

def concat(a, b):
    return str(a) + str(b) + str(b) + str(a)

def suaSorte(nome, idade):
    sorte = (((((idade*4) + 8)*60)/240) + 22) - idade
    return "Parabens " + nome + "! seu numero da sorte eh " + str(sorte) + "!"

def stringConc(palavra1, palavra2):
    if (len(palavra1) < 15):
        return "Primeira palavra nao tem 15 caracteres"
    if (len(palavra2) < 15):
        return "Segunda palavra nao tem 15 caracteres"
    return palavra1[5:] + palavra2[-10:]

def funcao4(s, x, i):
    if (len(x) != 1):
        return "Nao eh um char"
    if (i < 0 or i > len(s)-1):
        return "o numero inteiro deve estar entre 0 e o comprimento da string -1"
    return s[:i-1] + x + s[i:]

def funcao5(s):
    middle = len(s) / 2
    return s[:int(middle)] + s + s[int(middle):]

def funcao6(s):
    middle = len(s) / 2
    return "#" + s[:int(middle)] + "#" + s[int(middle):] + '#'

def funcao7(s):
    if (len(s) < 3):
        return "Tem que ter mais que 3 chars"
    tam = len(s)
    return  s[-3:] + s[:tam-3]

def funcao8(s,x):
    tam = len(s)
    return  s[-x:] + s[:tam-x]

def funcao9(s,x):
    if (len(s) < x):
        return "Tem que ter mais que" + str(x) + " chars"
    tam = len(s)
    return  s[-x:] + s[:tam-x]

def funcao10(d1, d2):
    dia1 = int(d1[:2])
    mes1 = int(d1[3:5])
    ano1 = int(d1[6:])
    dia2 = int(d2[:2])
    mes2 = int(d2[3:5])
    ano2 = int(d2[6:])

    if (ano1 > ano2):
        return "Segunda data tem que ser maior que a primeira"
    elif (ano1 == ano2 and mes1 > mes2):
        return "Segunda data tem que ser maior que a primeira"
    elif (ano1 == ano2 and mes1 == mes2 and dia1 >= dia2):
        return "Segunda data tem que ser maior que a primeira"

    diff = (ano2 - ano1)*365 + (mes2 - mes1)*30 + (dia2 - dia1)
    return diff

def funcao11(rx10, ry10, rx11, ry11, rx20, ry20, rx21, ry21):
    if (rx20 >= rx10 and rx20 <= rx11):
        return True
    elif (rx21 >= rx10 and rx21 <= rx11):
        return True
    elif (ry21 >= ry10 and ry21 <= ry11):
        return True
    elif (ry20 >= ry10 and ry20 <= ry11):
        return True
    else:
        return False

#Regiao de teste
def main():
    print(concat(2,3))
    print(suaSorte("Igor",28))
    print(stringConc("Eu nao sei o que escrever","Isso deve funcionar"))
    print(funcao4("Igor", "D", 3))
    print(funcao5("Igor"))
    print(funcao6("Igor"))
    print(funcao7("abcdefg"))
    print(funcao8("abcdefg", 4))
    print(funcao9("abcdefg", 4))
    print(funcao10("20/03/1990", "20/03/2018"))
    print(funcao10("20/03/2018", "20/06/2018"))
    print(funcao10("02/03/1982", "01/02/1983"))
    print(funcao11(0,0,1,1,0,0,1,1))
    print(funcao11(0,0,2,2,1,1,3,3))
    print(funcao11(0,0,1,1,2,2,3,3))

if __name__ == "__main__":
    main()
