'''Definindo função'''

def calcular():
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
        
    calcularNovamente()
        
 # Defina a função calcularNovamente () para perguntar ao usuário se ele deseja usar a calculadora novamente
def calcularNovamente():
    calc_nova = input ('''
        Deseja realizar novo calculo?
        Use S para sim e N para Nao.
        ''')
            # se for Y, gera novo calculo
    if calc_nova == 'S' or calc_nova == 'S':
        calcular()
                # se for N, sai da calculadora
    elif calc_nova == 'N' or calc_nova == 'n':
        print('Até mais!!')
                # se não informar nenhuma das alternativas volta para a função 
    else:
        calcularNovamente()

calcular()
