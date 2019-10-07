'''operadores matematicos'''
operacao = input('''
    Favor escolher uma das operações abaixo:
    + para Adição
    - para Subtração
    * para Multiplicação
    / para Divisão
    ''')

'''solicitando numeros'''
num_1 = int(input ('informe o primeiro numero: '))
num_2 = int(input ('informe o segundo numero: '))


'''validando o operador selecionado'''

if operacao == '+':
    print ('{} + {} = '.format(num_1, num_2),(num_1 + num_2))

elif operacao == '-':
    print ('{} - {} = '.format(num_1, num_2),(num_1 - num_2))

elif operacao == '*':
    print ('{} * {} = '.format(num_1, num_2),(num_1 * num_2))

elif operacao == '/':
    print ('{} / {} = '.format(num_1, num_2),(num_1 / num_2))

else:
    print ('Operador invalido!!!')

