import random

#Constroi uma matriz com pares de 1 a 8 em posicoes aleatorias
def constroiMatriz():
    matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    valores = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]

    for numero in valores:
        coordenadaX = random.sample([0,1,2,3],1)[0]
        coordenadaY = random.sample([0,1,2,3],1)[0]
        while matriz[coordenadaX][coordenadaY] != 0:
            posicao = random.sample([0,1,2,3],2)
            coordenadaX = random.sample([0,1,2,3],1)[0]
            coordenadaY = random.sample([0,1,2,3],1)[0]
        matriz[coordenadaX][coordenadaY] = numero
    return matriz

#Gera uma matriz 4x4 com asteristicos
def matrizOcultada():
    matrizOculta = [["*","*","*","*"],["*","*","*","*"],["*","*","*","*"],["*","*","*","*"]]
    return matrizOculta

#Imprime na tela a matriz resultante das jogadas
def imprimirMatriz(matriz):
    print(str(matriz[0][0]) + " " +  str(matriz[0][1]) + " " + str(matriz[0][2]) + " " + str(matriz[0][3]))
    print(str(matriz[1][0]) + " " +  str(matriz[1][1]) + " " + str(matriz[1][2]) + " " + str(matriz[1][3]))
    print(str(matriz[2][0]) + " " +  str(matriz[2][1]) + " " + str(matriz[2][2]) + " " + str(matriz[2][3]))
    print(str(matriz[3][0]) + " " +  str(matriz[3][1]) + " " + str(matriz[3][2]) + " " + str(matriz[3][3]))

#O valor no input deve ser passado no formato [x, y]
def primeiraJogada():
    primeiraPosicao = input("Escolha a primeira posicao [x,y]: ")
    primeiraJogada = [int(primeiraPosicao[1]), int(primeiraPosicao[3])]
    return primeiraJogada

#O valor no input deve ser passado no formato [x, y]
def segundaJogada():
    segundaPosicao = input("Escolha a segunda posicao [x,y]: ")
    segundaJogada = [int(segundaPosicao[1]), int(segundaPosicao[3])]
    return segundaJogada

#Apos uma jogada, modifica a matriz oculta para revelar o valor na posicao
def executaJogada(matrizMemoria, matrizOculta, jogada):
    matrizOculta[jogada[0]][jogada[1]] = matrizMemoria[jogada[0]][jogada[1]]
    imprimirMatriz(matrizOculta)

#Verifica se a combinacao das duas jogadas foi um acerto ou um erro
def validaAcerto(matrizMemoria, matrizOcultada, jogada1, jogada2):
    if (matrizMemoria[jogada1[0]][jogada1[1]] != matrizMemoria[jogada2[0]][jogada2[1]]):
        matrizOcultada[jogada1[0]][jogada1[1]] = "*"
        matrizOcultada[jogada2[0]][jogada2[1]] = "*"
        print("Voce errou... Tente de Novo.")
    else:
        print("Parabens! Voce acertou.")

#Verifica se a jogador acertou todas as posicoes pra que o jogo se encerre
def concluido(matriz):
    for linha in range(4):
        for coluna in range(4):
            if (matriz[linha][coluna] == "*"):
                return False
    return True

#Executa as validacoes necessarias solicitadas
def validaPosicao(jogada, matrizOculta):
    if jogada[0] not in [0,1,2,3]:
        print("Posicao Invalida.")
        return False
    elif jogada[1] not in [0,1,2,3]:
        print("Posicao Invalida.")
        return False
    elif matrizOculta[jogada[0]][jogada[1]] != "*":
        print("Posicao ja escolhida.")
        return False
    return True

#Programa principal que chama os modulos necessario para o jogo
def main():
    matrizMemoria = constroiMatriz()
    matrizOculta = matrizOcultada()
    numeroJogadas = 1

    while concluido(matrizOculta) == False:
        imprimirMatriz(matrizOculta)
        jogada1 = primeiraJogada()
        while validaPosicao(jogada1,matrizOculta) == False:
            jogada1 = primeiraJogada()
        executaJogada(matrizMemoria, matrizOculta, jogada1)
        jogada2 = segundaJogada()
        while validaPosicao(jogada2, matrizOculta) == False:
            jogada2 = segundaJogada()
        executaJogada(matrizMemoria, matrizOculta, jogada2)
        validaAcerto(matrizMemoria, matrizOculta, jogada1, jogada2)
        numeroJogadas += 1

    print("Parabens!! Voce conseguiu descobir todas as casas em " + str(numeroJogadas) + " jogadas!")

if __name__ == "__main__":
    main()
