def calculadora():
  print('Bem vindo a calculadora simples')
  print ('Operações disponiveis: +,-,*,/')

  operacao = input ('Escolha uma operação')
  num1 = float (input('Digite o primeiro numero'))
  num2 = float (input('Digite o segundo numero'))

  if operacao == '+':
    print (f'{num1} + {num2} = {num1 + num2}')
  elif operacao == '-':
    print (f'{num1} - {num2} = {num1 - num2}')
  elif operacao == '*':
    print (f'{num1} * {num2} = {num1 * num2}')
  elif operacao == '/':
    print (f'{num1} / {num2} = {num1 / num2}')
  else:
    print ('Operação invalida')

calculadora()