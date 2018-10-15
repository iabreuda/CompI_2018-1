#retorna uma lista sem duplicatas
def unique(lista):
    dicionario = {}
    for elemento in lista:
        dicionario[elemento] = 0
    return dicionario.keys()

#converte um numero para numero romano
def romano(numero):
    unidades = {0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
    dezenas = {0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
    centenas = {0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}

    restoCentena = numero % 100
    centena = (numero - restoCentena)/100
    numero = numero - (centena*100)

    restoDezena = numero % 10
    dezena = (numero - restoDezena)/10
    unidade = numero - (dezena*10)
    return centenas[centena] + dezenas[dezena] + unidades[unidade]

#Calcula a frequencia com que as palavras aparecem
def frequenciaPalavras(frase):
    lista = frase.split(' ')
    dicionario = {}
    for palavra in lista:
        if palavra not in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra] += 1
    return dicionario

#Traduz proteinas RNA
def traducaoRNA(trinca):
    traducao = {'UUU':'Phe','CUU':'Leu','UUA':'Leu','AAG':'Lisina','UCU':'Ser','UAU':'Tyr','CAA':'Gln'}
    return traducao[trinca[0:3]] + '-' + traducao[trinca[3:6]] + '-' + traducao[trinca[6:9]]

#Valor gasto no final das listaCompras
def listaCompras(lista, mercado):
    preco = 0
    for produto in lista:
        if produto in mercado:
            preco += mercado[produto]
    return preco

#Pessoas que sao correspondida
def afinidadePessoal(afinidade):
    listaAfinidades = []
    pessoas = afinidade.keys()
    for pessoa in pessoas:
        if pessoa == afinidade[afinidade[pessoa]]:
            listaAfinidades.append((pessoa, afinidade[pessoa]))

    return listaAfinidades

#Regiao de teste
def main():
    print(unique([1,2,3,3,3,5,5,6,7,7,1,11,11]))
    print(romano(957))
    print(frequenciaPalavras("dinheiro e dinheiro e vice versa"))
    print(traducaoRNA("UUUUUAUCU"))
    supermercado = {
        'amaciante': 4.99,
        'arroz': 10.90,
        'biscoito': 1.69,
        'cafe': 6.98,
        'chocolate': 3.79,
        'farinha': 2.99
    }
    print(listaCompras(['biscoito', 'chocolate', 'farinha'], supermercado))
    afinidade = {
        'Leo': 'Sofia',
        'Marcos': 'Andrea',
        'Sofia': 'Leo',
        'Alex': 'Andrea',
        'Andrea': 'Marcos'
    }
    print(afinidadePessoal(afinidade))

if __name__ == "__main__":
    main()
