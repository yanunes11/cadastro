#ENTRA COM NUMERO
#CALCULA

def fatorial_yan (numero):
    print('---FATORIAL---')
    #num = int(input('Digite um número inteiro: '))
    num = int(numero)
    fat = []
    soma = 1
    for i in range(num, 0, -1):
        fat.append(i)
    for i in range(0, num):
        soma *= fat[i]
    print(f'{num}! =', end='')
    for i in range(0, num):
        if fat[i] != 1:
            print(f' {fat[i]} X', end='')
        else:
            print(f' {fat[i]} = ', end='')
    print(soma)
