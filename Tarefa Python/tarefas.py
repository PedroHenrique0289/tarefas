'''exercicio 1:
print("Olá mundo")
'''


'''exercicio 2:
nome = input("qual é o seu nome? ")
idade = input("qual é a sua idade?")
cidade = input("qual é a sua cidade?")
print("olá," + (nome) + "! Você tem " + (idade) + "anos e mora em " + (cidade) + "." )
'''


'''exercicio 3
nome = input("qual é o seu nome? ")
print ("Olá, " + (nome))
'''


'''exercicio 4:
idade = input("qual é a sua idade? ")
print ("Você tem " + (idade) + " anos.")
'''


'''exercicio 5:
numero = int(input("Digite um número inteiro:"))
numero2 = int(input("Digite outro número para somar:"))
print ("A soma dos resultados é:", (numero + numero2) )
'''


'''exercicio 6:
numero = int(input("digite um numero:"))
numero2 = int(input("digite outro:"))
print("A soma dos resultados é:", (numero + numero2) )
print("A subtração dos resultados é:", (numero - numero2) )
print("A multiplicação dos resultados é:", (numero * numero2) )
print("A divisão dos resultados é:", (numero / numero2) )'''


'''exercicio 7:
numero = int(input("digite um numero:"))
print("O dobro do numero é:", (numero * 2))
'''


'''exercicio 8:
numero = int(input("digite um numero:"))
print("O triplo do numero é:", (numero * 3))
print("A metade do numero é:", (numero / 2))
'''


'''exercicio 9:
nome =  input("digite seu nome:")
nome2 =  input("digite seu sobrenome:")
print("Seu nome completo é:" , (nome + nome2))
'''


'''exercicio 10:
ano =  input("digite o seu ano de nascimento:")    
idade = 2026 - int(ano)
print("Sua idade é:", (idade))
'''


'''exercicio 11:
metros = float(input("digite um valor em metros:"))
centimetros = metros * 100
milimetros = metros * 1000
print("O valor em centimetros é:", (centimetros))
print("O valor em milimetros é:", (milimetros))
'''


'''exercicio 12:
minutos = int(input("digite um valor em minutos:"))
segundos = minutos * 60
print("O valor em segundos é:", (segundos))
'''


'''exercicio 13:
horas = int(input("digite um valor em horas:"))
minutos = horas * 60
print("O valor em minutos é:", (minutos))
'''


'''exercicio 14:
graus = float(input("digite um valor em graus Celsius:"))
fahrenheit = (graus * 9/5) + 32
print("O valor em Fahrenheit é:", (fahrenheit))
'''


'''exercicio 15:
reais = float(input("Digite um valor em reais: "))
dolar = 5.00
dolares = reais / dolar
print("Você pode comprar:", dolares, "dólares")
'''


'''exercicio 16:
lado = float(input("Digite o lado do quadrado em metros: "))
area = lado * lado 
print("A área do quadrado é:", area, "metros quadrados")
'''


'''exercicio 17:
largura = float(input("Digite a largura de um triangulo: "))
altura = float(input("Digite a altura de um trianglo: "))
area = (largura * altura)
print("A área do triângulo é:", area)
'''


'''exercicio 18:
base = float(input("Digite a base de um triangulo: "))
altura = float(input("Digite a altura de um triangulo: "))
area = (base * altura) / 2
print("A area do triangulo é:", area)
''' 


'''exercicio 19:
raio = float(input("Digite o raio: "))
area = 3.14 * raio ** 2
print("A área do círculo é:", area)
'''


'''exercicio 20:
largura = float(input("Digite a largura de um retangulo: "))
altura = float(input("Digite a altura de um retangulo: "))
perimetro = 2 * (largura + altura)
print("Perímetro:", perimetro)
'''


'''exercicio 21:
notas = float(input("Digite a primeira nota: "))
notas2 = float(input("Digite a segunda nota: "))
notas3 = float(input("Digite a terceira nota: "))
media = (notas + notas2 + notas3) / 3
print("A média das notas é:", media)
'''


'''exercicio 22:
valor = float(input("Digite o valor recebido por horas: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))
salario = valor * horas
print("O salário do funcionário é:", salario)
'''


'''exercicio 23:
salario = float(input("Digite o salário do funcionário: "))
aumento = 0.10
novo = salario + (salario * aumento)
print("O salário atual é:", salario)
print("O aumento do salário é:", aumento)
print("O novo salário é:", novo)    
'''


'''exercicio 24:
preco = float(input("Digite o preço do produto: "))
desconto = 0.15
novo = preco - (preco * desconto)
print("O preço atual do produto é:", preco)
print("O desconto é:", desconto)
print("O novo preço do produto é:", novo)
'''


'''exercicio 25:
valor = float(input("Digite o valor total da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
valor_parcela = (valor / parcelas)
print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
'''


'''exercicio 26:
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
'''


'''exercicio 27:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 * 2 + nota2 * 3) / (2 + 3)
print(f"A média ponderada é: {media:.2f}")
'''


'''exercicio 28:
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
quociente = numero1 // numero2
resto = numero1 % numero2
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")
'''


'''exercicio 29:
numero = int(input("Digite um número inteiro: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"Antecessor: {antecessor}")
print(f"Sucessor: {sucessor}")
'''


'''exercicio 30:
bas = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
resultado = bas ** expoente
print(f"Resultado: {resultado}")
'''


'''exercicio 31:
numero = float(input("Digite um número:"))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é igual a zero")
'''


'''exercicio 32:
idade = int(input("Digite sua idade:"))

if idade > 18:
    print("Você é de maior")
elif idade < 18:
    print("Você é de menor")
else:
    print("a idade é igual a zero")
'''


'''exercicio 33:
numero = int(input("Digite um número inteiro:"))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar")
'''


'''exercicio 34:
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

if numero1 > numero2:
    print("O primeiro número é maior")
elif numero1 < numero2:
    print("O numero 2 é maior")
else:
    print("Os números são iguais")
'''


'''exercicio 35:
numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior número é:", numero2)
else:
    print("o maior número é:", numero3)
'''


'''exercicio 36:
numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))
menor = min(numero1, numero2, numero3)

print("O menor número é:", menor)
'''


'''exercicio 37:
media = float(input("Digite a média do aluno:"))
if media >=6:
    print("Aprovado")
else:
    print("Reprovado")
'''


'''exercicio 38:
media = float(input("Digite a média do aluno:"))
if media >=7:
    print("Aprovado")
elif media >=5 and media <7:
    print("Recuperação")
else: 
    print("Reprovado")
'''


'''exercicio 39:
idade = int(input("Digite sua idade:"))
if idade <=11:
    print("Criança")
elif  idade >=12 and idade <=17:
    print("Adolescente")
elif idade >=18 and idade <=59:
    print("Adulto")
else:
    print("Idoso")
'''


'''exercicio 40:
senha = "1234"
tentativa = input("Digite a senha: ")
if tentativa == senha:
    print("Acesso permitido")
else:
    print("Acesso negado")
'''


'''exercicio 41:
usuario = "admin"
senha = "1234"
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
'''


'''exercicio 42:
numero = int(input("Digite um número inteiro: "))
if numero % 5 ==0:
    print("O número é divisível por 5")
else:
    print("O número não é divisível por 5")
'''


'''exercicio 43:
numero = int(input("Digite um número inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e por 5")
else:
    print("O número não é divisível por 3 e por 5")
'''


'''exercicio 44:
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
'''


'''exercicio 45:
valor = float(input("Digite um valor: "))
if valor >= 200:
    desconto = valor * 0.10
    novo_valor = valor - desconto
    print(f"Desconto de 10% aplicado. Novo valor: {novo_valor:.2f}")
else:
    print("Nenhum desconto aplicado. Valor final: {:.2f}".format(valor))
'''


'''exercicio 46:
valor = float(input("Digite um valor: "))
frete = 20.00
if valor >= 150:
    frete = 0
    print("Frete grátis aplicado. Valor final: {:.2f}".format(valor))
else:
    valor_final = valor + frete
    print("Frete de R$ 20,00 aplicado. Valor final: {:.2f}".format(valor_final))
'''


'''exercicio 47:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
else:
    print("Erro: Operação inválida.")
'''


'''exercicio 48:
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os lados podem formar um triângulo.")
else:
    print("Os lados não podem formar um triângulo.")
'''


'''exercicio 49:
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
'''


'''exercicio 50:
salario = float(input("Digite o seu salário: "))
if salario <= 2000:
    imposto = 0
elif salario <= 4000:
    imposto = salario * 0.10
else:
    imposto = salario * 0.20
salario_restante = salario - imposto
print("Valor do imposto: R$", imposto)
print("Salário restante: R$", salario_restante)
'''


'''exercicio 51:
for p in range(1,11,1):
    print(p)
'''


'''exercicio 52:
for p in range(10,-1,-1):
    print(p)
'''


'''exercicio 53:
for p in range(0,101,2):
    print(p)
'''


'''exercicio 54:
for p in range(1,100,2):
    print(p)
'''


'''exercicio 55:
numero = int(input("Digite um número: "))
for p in range(1, 11):
    print(numero, "x", p, "=", numero * p)
'''


'''exercicio 56:
Nmr = int(input("Digite um número: "))
soma = 0
for p in range(1, Nmr + 1):
    soma = soma + p 
print("A soma é:", soma)
'''


'''exercicio 57:
numero = int(input("Digite um número inteiro não negativo: "))
fatorial = 1
for p in range(1, numero + 1):
    fatorial *= p
print("O fatorial de", numero, "é:", fatorial)
'''


'''exercicio 58:
pares = 0 
for p in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        pares += 1

print("Quantidade de números pares digitados:", pares)
'''


'''exercicio 59:
numeros = 0
soma = 0
for p in range(10):
    numero = int(input("Digite números positivos e negativos: "))
    if numero > 0:
        numeros += 1
    soma += numero

print("Quantidade de números positivos digitados:", numeros)
print("Soma de todos os números digitados:", soma)
'''


'''exercicio 60:
maior = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    if maior is None or numero > maior:
        maior = numero
print("Maior valor:", maior)
'''


'''exercicio 61:
menor = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    if menor is None or numero < menor:
        menor = numero
print("Menor valor:", menor)
'''


'''exercicio 62:
soma = 0
for i in range(5):
    nota = float(input("Digite a nota: "))
    soma += nota
media = soma / 5
print("Soma:", soma)
print("Média:", media)
'''


'''exercicio 63:
senha_correta = "1234"
senha = input("Digite a senha: ")
while senha != senha_correta:
    print("Senha incorreta!")
    senha = input("Digite a senha novamente: ")
print("Acesso permitido")
'''

'''exercicio 64:
numero = int(input("Digite um número positivo: "))
while numero <= 0:
    numero = int(input("Número inválido. Digite outro: "))
print("Número positivo:", numero)
'''


'''exercicio 65:
opc = -1
while opc != 0:
    print("\n1 - Dizer olá")
    print("2 - Mostrar uma mensagem")
    print("0 - Sair")

    op = int(input("Escolha uma opção: "))

    if opc == 1:
        print("Olá!")
    elif opc == 2:
        print("Esta é uma mensagem!")
    elif opc == 0:
        print("Saindo...")
    else:
        print("Opção inválida!")
'''


'''exercicio 66:
soma = 0
numero = int(input("Digite um número: "))
while numero != 0:
    soma += numero
    numero = int(input("Digite outro número: "))

print("Soma final:", soma)
'''


'''exercicio 67:
notas = 0
quantidade = 0
numero = int(input("Digite uma nota (ou -1 para sair): "))
while numero != -1:
    notas += numero
    quantidade += 1
    numero = int(input("Digite outra nota (ou -1 para sair): "))
    if quantidade > 0:
        media = notas / quantidade
        print("Média das notas:", media, "com", quantidade, "notas digitadas.")
    else:
        print("Nenhuma nota foi digitada.")
'''


'''exercicio 68:
secreto = 123
numero = int(input("Digite um número: "))
while numero != secreto:
    if numero < secreto:
        print("O número é menor que o número secreto.")
    else:
        print("O número é maior que o número secreto.")
    numero = int(input("Digite outro número inteiro: "))
'''


'''exercicio 69:
numero = int(input("Digite um número maior que 1: "))
primo = True
for p in range(2, numero):
    print("Dividindo por ",p)
    if numero % p == 0:
        primo = False
        break

if (primo == True):
    print("O numero é primo")
else:
    print("O numero nao é primo")
'''


'''exercicio 70:
nmr1 = int(input("Digite o primeiro número: "))
nmr2 = int(input("Digite o segundo número: "))

for p in range(nmr1, nmr2 + 1):
    primo = True
    if p < 2:
        primo = False
    for divisor in range(2, p):
        if p % divisor == 0:
            primo = False
            break
    if primo:
        print(p)
'''


'''exercicio 71:
nome = input("Digite seu nome ou uma frase: ")
print("Seu nome/frase tem", len(nome), "caracteres.")
'''


'''exercicio 72:
palavras = input("Digite uma palavra ou frase: ")
print("Sua palavra/frase em maiúsculas:", palavras.upper())
print("Sua palavra/frase em minúsculas:", palavras.lower())
'''


'''exercicio 73:
palavra = input("Digite uma palavra: ")
if palavra != "":
    print("A primeria letra da palavra é:", palavra[0])
    print("A última letra da palavra é:", palavra[-1])
'''


'''exercicio 74:
frase = input("Digite uma frase: ")
frase = frase.lower()
print("A palavra tem", frase.count("a"), "letras 'a'.")
'''


'''exercicio 75:
palavra = input("Digite uma palavra: ")
palavra = palavra.lower()
if palavra == palavra[::-1]:
    print("A palavra pode ser lida igualmente de trás para frente ")
else:
    print("A palavra não pode ser lida igualmente de trás para frente")
'''


'''exercicio 76:
palavra = input("Digite uma palavra:")
palavra2 = palavra.split( )
print(palavra2)
'''



'''exercicio 77:
palavra = input("Digite uma palavra:")
palavra2 = palavra.split( )
for p in palavra2:
    print(p)
'''


'''exercicio 78:
frase = input("Digite uma frase: ")
palavras = frase.split( )
print("A frase possui", len(palavras),"palavras.")
'''


'''exercicio 79:
frase = input("Digite uma frase: ")
palavra = input("Digite a palavra que deseja substituir: ")
Npalavra = input("Digite a nova palavra:")
resultado = frase.replace(palavra, Npalavra)
print("Frase modificada:", resultado)
'''


'''exercicio 80:
email = input("Digite seu email: ")
posicaoA = email.find("@")
if posicaoA != -1 and "." in email[posicaoA +1:]:
    print("Email válido")
else:
    print("Email inválido")
'''


'''exercicio 81:
nomes = ["Pedro", "Vitor", "Emanuel", "Felipe", "Alice"]
for nome in nomes:
    print(nome)
'''


'''exercicio 82:
listanomes = []
for i in range(5):
    nomes = input("Digite um nome: ")
    listanomes.append(nomes)
for nome in listanomes:
    print(nome)
'''


'''exercicio 83:
numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for numero in numeros:
    soma = soma + numero
print("A soma dos números é:", soma)
'''


'''exercicio 84:
numeros = [10,20,55,74,23]
maiorN = numeros[0]
for numero in numeros:
    if numero > maiorN:
        maiorN = numero
print("O maior número é:", maiorN)
'''


'''exercicio 85:
numeros = [10,20,55,74,23]
menorN = numeros[0]
for numero in numeros:
    if numero < menorN:
        menorN = numero
print("O menor número é:", menorN)
'''


'''exercicio 86:
notas = []
soma = 0
for i in range(5):
    nota = float(input("Digite a nota do aluno: "))
    soma = soma + nota
media = soma / 5

print("A média das notas é:", media)
'''


'''exercicio 87:
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Os números pares são:", pares)
'''


'''exercicio 88:
nomes = ["Pedro", "Vitor", "Emanuel", "Felipe", "Alice"]
remover = input("Digite o nome que deseja remover: ")
nomes.remove(remover)

print("Lista atualizada:", nomes)
'''


'''exercicio 89:
produtos = []
for i in range(5):
    produto = input("Digite o nome do produto: ")
    produtos.append(produto)
buscar = input("Digite o nome do produto que deseja buscar: ")
if buscar in produtos:
    print("Produto encontrado!")
else:
    print("Produto não encontrado.")
'''


'''exercicio 90:
numeros = []
for i in range(5):
    nmr = int(input("Digite um número: "))
    numeros.append(nmr)
crescente = sorted(numeros)
decrescente = sorted(numeros, reverse=True)

print("Números em ordem crescente:", crescente)
print("Números em ordem decrescente:", decrescente)
'''


'''exercicio 91:
numeros = []
for i in range(10):
    nmr = int(input("Digite um número: "))
    numeros.append(nmr)

diferentes = set(numeros)
print("Números diferentes:", diferentes)
'''


'''exercicio 92:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
intersecao = conjunto1 & conjunto2
print("Valores que aparecem nos dois conjuntos:", intersecao)
'''


'''exercicio 93:
XeY = (10, 20)
print("O valor de X é:", XeY[0])
print("O valor de Y é:", XeY[1])
'''


'''exercicio 94:
info = {"Nome": "Pedro", 
        "Idade": 18, 
        "Cidade": "Uberlândia"}

print("Meu nome é", info["Nome"], ", tenho", info["Idade"], "anos e moro em", info["Cidade"])
'''




'''exercicio 95:
Notas = []
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
dc = {
      "Nome": nome, 
      "Nota1": nota1, 
      "Nota2": nota2,
}
dc ["Média"] = media

print(dc["Média"])
'''


'''exercicio 96:
lista = []
produtos = {}
produtos["nome"] = input("Digite o nome do produto: ")
produtos["preço"] = float(input("Digite o preço do produto: "))
lista.append(produtos)
produtos["nome"] = input("Digite o nome do produto: ")
produtos["preço"] = float(input("Digite o preço do produto: "))
lista.append(produtos)
produtos["nome"] = input("Digite o nome do produto: ")
produtos["preço"] = float(input("Digite o preço do produto: "))
lista.append(produtos)

for i in range(3):
    print(lista[i])
'''


'''exercicio 97:
produtos = [
    {"nome": "mouse", "preço": 50},
    {"nome": "teclado", "preço": 100},
    {"nome": "monitor", "preço": 500}
]
maior = produtos[0]
for p in produtos:
    if p["preço"] > maior["preço"]:
        maior = p
print("O produto mais caro é o", maior["nome"], "com preço de R$", maior["preço"])
'''



'''exercicio 98:
list = {
    "gestor": "34984289524",
    "senac": "34999999999",
    "davi": "34888888888"
}
nome = input("digite o nome da pessoa: ")
if nome in list:
    print(f"Telefone {nome}: {list[nome]}")
else:
    print("pessoa não encontrada")
'''


'''exercicio 99:
digite = input("Digite alguma frase: ")
pala = digite.lower().split()
cont = {}
for palavra in pala:
    if palavra in cont:
        cont[palavra] += 1
    else:
        cont[palavra] = 1
print(cont)
'''


'''exercicio 98:
estoq = {
    "arroz": 20,
    "feijao": 10,
    "pc": 30
}

nomeprod = input("Digite o nome do produto: ")
quant = int(input("Digite a quantidade de produto: "))
if nomeprod in estoq:
    if quant <= estoq[nomeprod]:
        estoq[nomeprod] -= quant
        print(f"retirada realizada, a quantidade de sobra atual é: {estoq[nomeprod]}")
    else:
        print(f"Não tem estoque")
else:
    print("Não encontrei esse produto")
print(f"A quantidade atual é {estoq}")
'''


'''exercicio 101:
def saudacao():
    print("Bem-vindo ao programa.")

saudacao()
'''


'''exercicio 102:
def saudacao(nome):
    print("Bem-vindo ao programa",nome)

saudacao("Pedro")
'''


'''exercicio 103:
def soma(x, y):
    return x + y

print(soma(5, 3))
'''


'''exercicio 104:
def maior (x, y):
    if x > y:
        return x
    else:
        return y

print(maior(10, 5 ))
'''


'''exercicio 105:
numero = int(input("Digite um número inteiro: "))
def inteiro(numero):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

inteiro(numero)
'''


'''exercicio 106:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print(media(nota1, nota2, nota3,))
'''


'''exercicio 107:
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
def LA():
    area = largura * altura
    return area

print(LA())
'''


'''exercicio 108:
temperatura = float(input("Digite a temperatura em Celsius: "))
def pf(temperatura):
    fahrenheit = (temperatura * 9/5) + 32
    return fahrenheit

print(pf(temperatura))
'''


'''exercicio 109:
intN = int(input("Digite um número inteiro: "))
def F(intN):
    fatorial = 1
    for p in range(1, intN + 1):
        fatorial *= p
    return fatorial

print(F(intN))
'''


'''exercicio 110:
nmr = int(input("Digite um número: "))
def primo(nmr):
    if nmr < 2:
        return False
    for i in range(2, nmr):
        if nmr % i == 0:
            return False
    return True
print(primo(nmr))
'''


'''exercicio 111:
p = input("Digite uma palavra: ")
def vogais(palavra):
    palavra = palavra.lower()
    quantidade = 0
    for letra in palavra:
        if letra in "aeiou":
            quantidade += 1
    return quantidade

print("A quantidade de vogais na palavra é:", vogais(p))
'''


'''exercicio 112:
numeros = [1, 8, 3, 45, 5, 72, 8, 98, 10]
def maiorN(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

print("O maior número é:", maiorN(numeros))
'''


'''exercicio 113:
def media(x,y,z,a,b):
    print(f"a média é: {(x + y + z + a + b) / 5}")

x = int(input("Digite a primeira nota "))
y = int(input("Digite a segunda nota "))
z = int(input("Digite a terceira nota "))
a = int(input("Digite a quarta nota "))
b = int(input("Digite a quinta nota "))

media(x,y,z,a,b)
'''


'''exercicio 114:
def posi(p):
    positivo = []
    for numero in p:
        if numero > 0:
            positivo.append(numero)
    return positivo

numeros = [-1, 5, 6, 0, -3, 7]
print(f"{posi(numeros)}")
'''


'''exercicio 115:
def somar(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def divisao(a,b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opcao = int(input("Escolha uma opção: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if opcao == 1:
    print(f"Resultado: {somar(num1, num2)}")
elif opcao == 2:
    print(f"Resultado: {subtrair(num1, num2)}")
elif opcao == 3:
    print(f"Resultado: {multiplicar(num1, num2)}")
elif opcao == 4:
    print(f"Resultado: {divisao(num1, num2)}")
else:
    print("Opção inválida!")
'''


'''exercicio 116:
arq = open("nomes.txt", "a")
nome = input("Digite seu nome: ")
arq.write(nome)
arq.write("\n")
arq.close()

print("Todos os nomes foram salvos no arquivo 'nomes.txt'.")
'''


'''exercicio 117:
arq = open("nomes.txt", "a")
while True:
    nome = input("Digite seu nome (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        print("Programa encerrado.")
        break
    arq.write(nome)
    arq.write("\n")
arq.close()

print("Todos os nomes foram salvos no arquivo 'nomes.txt'.")
'''


'''exercicio 118:
lerarq = open("nomes.txt", "r")
conteudo = lerarq.read()

print("Conteúdo do arquivo 'nomes.txt':")
print(conteudo)
'''


'''exercicio 119:
abrir = open("nomes.txt", "r")
for linha in abrir:
    print(linha.strip())
abrir.close()
'''

'''exercicio 120:
contar = open("nomes.txt", "r")
linhas = contar.readlines()

print("Quantidade de linhas no arquivo 'nomes.txt':", len(linhas))
'''


'''exercicio 121:
try:
    nmrint = int(input("Digite um número inteiro: "))
    print("Você digitou o número:", nmrint)
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
'''


'''exercicio 122:
try:
    nmr = float(input("Digite um número inteiro: "))
    nmrr = float(input("Digite um número inteiro: "))
    r = nmr / nmrr

    print("O resultado da divisão é:", r)
except ValueError:
    print("Digite apenas números inteiros")

except ZeroDivisionError:
    print("Erro: Você não digitou um número válido.")
'''


'''exercicio 123:
import calculos 
nmr = 200
nmrr = 10
r1 = calculos.soma(nmr, nmrr)
r2 = calculos.multiplicacao(nmr, nmrr)

print("O resultado da soma é:", r1)
print("O resultado da multiplicação é:", r2)
'''


'''exercicio 124:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoal= Pessoa("Pedro", 18)

print("Nome:", pessoal.nome)
print("Idade:", pessoal.idade)
'''


'''exercicio 125:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1= Pessoa("Pedro", 18)
pessoa2= Pessoa("Vitor", 20)

print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
print("Nome:", pessoa2.nome)
print("Idade:", pessoa2.idade)
'''


'''exercicio 126:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa = Pessoa("Pedro", 18)
pessoa.apresentar()
'''


''''exercicio 127:
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def dados(self):
        print(f"O produto é {self.nome} e tem o preço de {self.preco} reais")

produto1 = Produto("Arroz", 25)
produto2 = Produto("feijão", 20)
produto3 = Produto("Picanha", 87)
produto1.dados()
produto2.dados()
produto3.dados()
'''


''''exercicio 128:
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        preco_com_desconto = self.preco - desconto
        return preco_com_desconto


produto1 = Produto("Arroz", 25)
print(produto1.desconto(10))
produto2 = Produto("feijão", 20)
print(produto2.desconto(15))
produto3 = Produto("Picanha", 87)
print(produto3.desconto(20))
'''


'''exercicio 129:
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")
conta = ContaBancaria("Pedro", 1000)
conta.depositar(500)
conta.sacar(200)
print(f"Titular: {conta.titular}, Saldo final: R$ {conta.saldo:.2f}")
'''


'''exercicio 130:
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    def calcularmedia(self):
        return sum(self.notas) / len(self.notas)

aluno = Aluno("Pedro", [8.5, 7.0, 9.0])

print(f"Nome do aluno: {aluno.nome}")
print(f"Média das notas: {aluno.calcularmedia():.2f}")
'''


'''exercicio 131:
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    def calcularmedia(self):
        return sum(self.notas) / len(self.notas)
    def situacao(self):
        if self.calcularmedia() >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno = Aluno("Pedro", [8.5, 7.0, 9.0])

print(f"Nome do aluno: {aluno.nome}")
print(f"Média das notas: {aluno.calcularmedia():.2f}")
print(f"Situação: {aluno.situacao()}")
'''


'''exercicio 132:
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calculararea(self):
        return self.largura * self.altura
    def calcularperimetro(self):
        return 2 * (self.largura + self.altura)

retangulo = Retangulo(5, 10)

print(f"Largura: {retangulo.largura}")
print(f"Altura: {retangulo.altura}")
print(f"Área: {retangulo.calculararea()}")
print(f"Perímetro: {retangulo.calcularperimetro()}")
'''

    
'''exercicio 133:
class Carro:
    def __init__(self, modelo, velocidadeatual, velocidademaxima):
        self.modelo = modelo
        self.velocidadeatual = velocidadeatual
        self.velocidademaxima = velocidademaxima
    def acelerar(self, valor):
        if self.velocidadeatual + valor <= self.velocidademaxima:
            self.velocidadeatual += valor
            print(f"Velocidade atual: {self.velocidadeatual} km/h")
        else:
            print("Não é possível acelerar além da velocidade máxima.")
    def frear(self, valor):
        if self.velocidadeatual - valor >= 0:
            self.velocidadeatual -= valor
            print(f"Velocidade atual: {self.velocidadeatual} km/h")
        else:
            print("Não é possível frear abaixo de 0 km/h.")

carro = Carro("Fusca", 0, 120)
carro.acelerar(50)
carro.frear(30)
'''


'''exercicio 134:
class Livro: 
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.listadelivro = []

    def adicionar(self, livro):
        self.listadelivro.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar(self):
        for livro in self.listadelivro:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Disponível: {livro.disponivel}")

    def emprestar(self, titulo):
        for livro in self.listadelivro:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"Livro '{titulo}' emprestado com sucesso!")
                return
        print(f"Livro '{titulo}' não disponível para empréstimo.")

    def devolver(self, titulo):
        for livro in self.listadelivro:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"Livro '{titulo}' devolvido com sucesso!")
                return
        print(f"Livro '{titulo}' não encontrado ou já disponível.")


homemaranha = Livro("Homem Aranha", "Stan Lee")
hulk = Livro("Hulk", "Stan Lee")
thor = Livro("Thor", "Stan Lee")

biblioteca = Biblioteca()
biblioteca.adicionar(hulk)
biblioteca.listar()
biblioteca.emprestar("Hulk")
biblioteca.devolver("Hulk")
''' 