#PROGRAMA PRINCIPAL
#FUNÇÃO MENU
#FUNCÃO CRIA E RECEBE LOGIN
#TRATA LOGIN
#FUNÇÃO CRIA E RECEBE SENHA
#TRATA SENHA

#MENU
def menu():
    print('1 - Login\n2 - Cadastro')
    escolha_opcao = int(input('Digite sua opção: '))
    while escolha_opcao != 1 and escolha_opcao != 2:
        print(f'\nOpção \'{escolha_opcao}\' é inválida')
        print('1 - Login\n2 - Cadastro')
        escolha_opcao = int(input('Digite sua opção: '))
    return escolha_opcao

def recebe_login():
    login = str(input(('Digite um Login: '))).strip()
    if ' ' in login or len(login) < 6:
        print('ERRO: o login deve ter pelo menos 6 caracteres e não pode conter espaços!')
        recebe_login()
    return str(login)


def recebe_senha():
    senha = str(input('Digite sua senha: ')).strip()
    espaco = letra = num = carac = mai = min = 0
    for i in senha:
        if i.isupper():
            mai += 1
        if i.islower():
            min += 1
        if i.isalpha():
            letra += 1
        if i.isnumeric():
            num += 1
        if not i.isalnum():
            carac += 1
        if i == ' ':
            espaco += 1
    if len(senha) < 4 or letra == 0 or num ==0 or carac == 0 or espaco > 0 or mai == 0 or min == 0:
        print('ERRO: Mínimo 4 caracateres com pelo menos 2 letra(1 maiúscula e 1 minúscula), 1 número e 1 caracter especial!')
        recebe_senha()
    return str(senha)


print('---CADASTRO---')
escolhido = menu()
if escolhido == 2:
    login_ok = recebe_login()
    print(f'Login {login_ok[:2]}{(len(login_ok) - 4) * "*"}{login_ok[-2:]} salvo')
    senha_ok = recebe_senha()
    print(f'Senha {len(senha_ok) * "*"} salva')
else:
    print('Bye Bye')
