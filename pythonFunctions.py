# -*- coding: utf-8 -*-
"""Jucelio_Brandao_Goncalves_Junior.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j9Xf7AzCMHDCczsq5dcD5Tjv0JC-4p7s

Exercicio 1
"""

# O método int() transforma a string recebida no input em número inteiro
votosA = int(input('Quantidade de votos do partido A: ')) # Introduz a quantidade de votos do partido A
votosB = int(input('Quantidade de votos do partido B: ')) # Introduz a quantidade de votos do partido B
votosC = int(input('Quantidade de votos do partido C: ')) # Introduz a quantidade de votos do partido C
vagas = int(input('Quantidade de vagas na Assembleia ou Câmara: ')) # Introduz a quantidade de vagas na Assembleia ou Câmara

# A seguir calculo o quociente de cada partido e eleitoral
quoEleitoral = int("%.0f" % ((votosA + votosB + votosC) / vagas)) # O "%.0f" é uma sintaxe especial do python que permite escolher a precisão de casas decimais,
                                                                  # nesse caso não estou arredondando, apenas ignorando as casas decimais, porém retorna esse valor
                                                                  # como string, logo tenho que passar novamente como sendo inteiro com o int()
quoA = votosA / quoEleitoral
quoB = votosB / quoEleitoral
quoC = votosC / quoEleitoral

# Informa o coeficiente eleitoral
print('O coeficiente eleitoral é de: ', quoEleitoral)

# Caso exista algum partido com quociente igual a zero, relatar
if(quoA == 0):
  print('O partido A tem quociente partidário igual a 0.')
if(quoB == 0):
  print('O partido B tem quociente partidário igual a 0.')
if(quoC == 0):
  print('O partido C tem quociente partidário igual a 0.')

"""Exercicio 2

"""

numero = int(input('Introduza um número: ')) # Usuario introduz um número que é passado como inteiro

# Lógica para encerrar o programa caso seja digitado 99

if(numero == 99):
  exit(True) # Método exit() para parar a execução do código, com True como paramêtro para continuar a execução do Colab sem problemas

# Lógica para dizer se o número é positivo, negativo ou nulo
elif(numero > 0):
  print('O número', numero, 'é positivo')
elif(numero < 0):
  print('O número', numero, 'é negativo')
elif(numero == 0):
  print('O número', numero, 'é nulo')

"""Exercicio 3

"""

# Preparo as variáveis que serão utilizadas para armazenar a lista de numeros, informações necessárias para o loop e as somas
numeroDeInputs = int(input('Digite a quantidade de números que deseja digitar: '))
index = 0
listaDeNumeros = [];
listaDeNumerosPares = []
listaDeNumerosImpares = []
somaPares = 0
somaImpares = 0

while index != numeroDeInputs: # Enquanto o index não for igual a quantidade de inputs a serem recebidos, o programa continua
  numero = int(input('Digite o número: '))
  if numero < 0: # Caso o número seja negativo, o programa para
    break
  elif ((numero % 2) == 0): # Caso seja par informa que é par e adiciona o número a lista de números pares
    print('O número:', numero, 'é par!')
    listaDeNumerosPares.append(numero)
    index += 1
  else:
    print('O número:', numero, 'é impar!') # Caso não seja par, o mesmo ocorre, mas para lista de números impares
    listaDeNumerosImpares.append(numero)
    index += 1

for numero in listaDeNumerosPares: # Soma todos os pares, um por um
  somaPares += numero

for numero in listaDeNumerosImpares: # Soma todos os impares
  somaImpares += numero

print('A soma de números pares é:', somaPares)
print('A soma de números impares é:', somaImpares)

pctPares = (len(listaDeNumerosPares) / numeroDeInputs) * 100     # Calcula a porcentagem de números pares, utilizando o método len() que retorna a quantidade de elementos na lista 
pctImpares = (len(listaDeNumerosImpares) / numeroDeInputs) * 100 # O mesmo ocorre para os números impares

print('A porcentagem de numeros pares é:', pctPares, '%')
print('A porcentagem de numeros impares é:', pctImpares, '%')

"""Exercicio 4

"""

# Variaveis para o loop e armazenar as idades digitadas
numeroDePessoas = 15
index = 0
listaDeIdades = []

while index != numeroDePessoas:  # Armazena as idades digitadas enquanto o index não atingir o numero necessário de pessoas
  idade = int(input('Informe a idade:'))
  listaDeIdades.append(idade)
  index += 1

maiorIdade = max(listaDeIdades, key=int)  # O método max() pega o maior valor dentro de uma lista,
                                          # a propriedade key= é para informa-lo do que a lista é composta e o que considerar no momento de categorizar o máximo

print('A maior idade é:', maiorIdade)

"""Exercicio 5"""



conceito = input('Informe o conceito da pessoa estudante: ')

# Lógica simpes de if/else

if conceito == 'A':
  print('Desempenho excepcional!')
elif conceito == 'B':
  print('Bom desempenho!')
elif conceito == 'C':
  print('Desempenho adequado')
elif conceito == 'D':
  print('Aproveitamento mínimo')
elif conceito == 'F':
  print('Reprovado')
elif conceito == 'O':
  print('Reprovado por falta')
elif conceito == 'I':
  print('Incompleto')
else:
  print('Por favor informar um conceito que seja: A, B, C, D, F, O, I')

"""Exercicio *6* / 7

"""

saque = int(input('Informe o valor a ser sacado: '))
valor = saque # Valor a ser manipulado
cedula = 50 # Maior cédula
quantidadeCedulas = 0

while True: # Loop infinito
  if saque < 0 or saque > 2000: # Caso o valor seja negativo ou maior que 2000, parar o programa
    break
  if valor >= cedula: # Caso a cédula possa ser retirada do valor total
    valor -= cedula # Retira a cédula
    quantidadeCedulas += 1 # Soma mais um a quantidade de cédulas desse valor
  else: # Caso não seja possível retirar, imprime a quantidade de cédulas já retiradas desse valor, e muda o valor da cédula
    if quantidadeCedulas > 0: # Caso tenha alguma cédula do valor, imprimir a quantidade de notas retiradas
      print('Total de cédulas de', quantidadeCedulas, 'de', cedula, 'reais')
    if cedula == 50: # Se for 50, muda para 10
      cedula = 10
    elif cedula == 10: # Se for 10, para 5
      cedula = 5
    elif cedula == 5: # Caso seja 5, para 1
      cedula = 1
    quantidadeCedulas = 0
    if valor == 0: # Se o valor chegar a 0, o programa para
      break

"""Exercicio 8"""

numeroDeClientes = 50
index = 0
prefereMilho = 0
naoPrefereMilho = 0
somaIdade = 0

while index != numeroDeClientes:
  q1 = input('Gosta de milho no hotdog? S ou N ?') # Registra a resposta de ambas perguntas
  q2 = int(input('Qual a sua idade?'))
  if q1 != 'S' and q1 != 'N': # É necessário que seja S ou N, caso seja outra coisa, para o programa
    print('Por favor digitar S ou N na questão 1')
    break
  elif q2 < 10:
    print('A idade minima de participação é 10 anos') # É necessário que a idade seja 10 anos
    break
  elif q1 == 'S': # Caso goste de milho, adiciona um ao contador de pessoas que gostam de milho
    prefereMilho += 1
    index += 1
  elif q2 >= 10: # Caso contrário, se a idade for maior que 10, soma a idade total de pessoas que não gostam e aumenta o número das mesmas
    somaIdade += q2
    naoPrefereMilho += 1
    index += 1
  
if naoPrefereMilho != 0: # Caso resposta válida seja dada, isso é, o numero foi corretamente utilizado
  print('A média da idade de quem não gosta de milho é:', somaIdade / naoPrefereMilho)

if prefereMilho != 0:
  print('A quantidade de clientes que preferem milho é:', prefereMilho)

"""Exercicio 9"""

while True: # Looping infinito
  livros = input('Quantos livros deseja comprar? ')
  if livros == 'F': # Caso o usuario digite F, o programa para
    break

  criterioA = (int(livros) * 0.25) + 7.50 # Calculo dos critérios
  criterioB = (int(livros) * 0.75) + 2.50

  if (criterioA < criterioB): # Imprime qual o critério com menor valor para a quantidade de livros
    print('O valor é menor com o critério A para essa quantidade de livros')
  else:
    print('O valor é menor com o critério B para essa quantidade de livros')

"""Exercicio 10"""

loop = True

while loop:
  user = input('Insira um nome de usuário: ')
  psw = input('Insira uma senha: ')

  if user == psw:
    print('Senha e Nome não podem ser iguais! Insira novamente')
  else:
    loop = False

"""Exercicio 11"""

nome = input('Digite seu nome: ')

if len(nome) < 3:
  print('Nome deve ter mais de três letras')
  quit(True)

idade = int(input('Digite sua idade: '))

if idade < 0 or idade > 150:
  print('Idade deve ser entre 0 e 150 anos')
  quit(True)

salario = int(input('Digite seu salário'))

if salario < 0:
  print('Salário deve ser maior que 0')
  quit(True)

sexo = input('Insira seu sexo (f ou m): ')

if sexo != 'f' and sexo != 'm':
  print('Sexo deve ser m ou f')
  quit(True)

civil = input('Insira seu estado civil (s, c, v ou d): ')

if civil != 's' and civil != 'c' and civil != 'v' and civil != 'd':
  print('Estado civil deve ser s, c, v ou d')
  quit(True)