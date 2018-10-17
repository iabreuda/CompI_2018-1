#Jogo da Velha
def jogoVelha():
    palavra = input("Digite uma palavra: ")
    chances = 8
    palavraOculta = list('-'*len(palavra))
    while chances > 0:
        print("Voce tem " + str(chances) + " chances.")
        print(''.join(palavraOculta))
        letra = input("Digite uma letra: ")
        if letra in palavra:
            indice = 0
            for valor in palavra:
                if letra == valor:
                    palavraOculta[indice] = valor
                indice += 1
        if (palavra == ''.join(palavraOculta)):
            print("Parabens, voce acertou a palavra " + palavra + " !!!")
            break
        chances -= 1
    if chances == 0:
        print("Voce perdeu, a palavra correta era: " + palavra)

#Conta o numero de series onde ocorrem numeros repetidos em sequencia
def serieDeNumero():
    listaLancamento = []
    for indice in range(15):
        rolagem = input("Informe a rolagem " + str(indice + 1) +  " : ")
        listaLancamento.append(int(rolagem))
    posicao = 0
    contadorRepeticao = 0
    indice = 0
    for elemento in listaLancamento:
        repete = 0
        if (indice != posicao):
            indice += 1
            continue
        if posicao == len(listaLancamento) - 2:
            break
        while elemento == listaLancamento[posicao + 1]:
            repete += 1
            posicao += 1
        if repete > 0:
            contadorRepeticao += 1
        posicao += 1
        indice += 1
    print(contadorRepeticao)

#Tem um retorno diferente de acordo com a escolha
def funcaoTripla():
    codigo = input("Escolha um codigo de 1 a 4: ")
    a = int(input("Informe o valor a: "))
    b = int(input("Informe o valor b (b > a): "))
    c = int(input("Informe o valor c:"))
    if b < a:
        print("b nao pode ser menor que a")
        return
    print("Valor a = ", str(a))
    print("Valor b = ", str(b))
    print("Valor c = ", str(c))
    if codigo == "1":
        print(funcaoPrimeira(a,b,c))
    elif codigo == "2":
        print(funcaoSegunda(a,b,c))
    elif codigo == "3":
        print(funcaoTerceira(a,b,c))
    elif codigo == "4":
        print(funcaoQuarta(a,b,c))
    else:
        print("Nao foi escolhido um codigo correto")

#Funcao a ser executada pelo codigo 1
def funcaoPrimeira(a,b,c):
    return ((a+b)*c)/2

#Funcao a ser executada pelo codigo 2
def funcaoSegunda(a,b,c):
    return a*a*b*b*c*c

#Funcao a ser executada pelo codigo 3
def funcaoTerceira(a,b,c):
    return (a+b+c)/3

#Funcao a ser executada pelo codigo 4
def funcaoQuarta(a,b,c):
    soma = 0
    while a < b:
        soma += a
        a += c
    return soma

#Retorna todos os registros de um determinado setor
def buscaSetorial():
    busca = []
    matriz = []
    registro = 3
    while registro > 0:
        nome = input("Digite o nome do funcionario: ")
        matricula = input("Digite a matricula do funcionario: ")
        setor = input("Digite o setor de alocacao: ")
        tel = input("Cadastre o telefone do funcionario: ")
        matriz.append([nome, matricula, setor, tel])
        registro -= 1
    setor = input("Deseja buscar por qual setor: ")
    for linha in range(len(matriz)):
        if (matriz[linha][2] == setor):
            busca.append(matriz[linha])
    if (len(busca) == 0):
        return "Nenhum registro encontrado"
    print(busca)



#Regiao de teste
#Basta descomentar o que quer testar e executar o arquivo no terminal
def main():
    #jogoVelha()
    #serieDeNumero()
    #funcaoTripla()
    buscaSetorial()



if __name__ == "__main__":
    main()
