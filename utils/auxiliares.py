import colorama
import time

colorama.init(autoreset=True)

def log(mensagem, tipo = 'INFO', cor = colorama.Fore.WHITE):

    tipo = tipo.upper().strip()

    if tipo == 'INFO':
        print(cor + f'{mensagem}')

    elif tipo == 'ERRO':
        print(colorama.Fore.RED + f'{mensagem}')

    elif tipo == 'SUCESSO':
        print(colorama.Fore.GREEN + f'{mensagem}')

    else:
        print(cor + f'{mensagem}')

def menu_option():

    log('='*30, cor=colorama.Fore.BLUE)
    log('SISTEMA DE CLIENTES'.center(30), cor=colorama.Fore.GREEN)
    log('='*30, cor=colorama.Fore.BLUE)

    log("1 - Cadastrar Cliente")
    log("2 - Listar Clientes")
    log("3 - Buscar Cliente")
    log("4 - Atualizar Cliente")
    log("5 - Excluir Cliente")
    log("6 - Sair")
        
    log('='*30, cor=colorama.Fore.BLUE)

    try:
        opcao = int(input('Escolha uma opção: '))

        if opcao not in [1, 2, 3, 4, 5, 6]:
            log('Opção inválida. Digite um número entre 1 e 6.', 'ERRO')
            return False

        time.sleep(1)
        if opcao:
            return opcao

    except ValueError:
        log('Entrada inválida. Por favor, digite um número.', 'ERRO')
        return False

def validando_cpf(cpf, list_cpfs=None):
    """
    Função para validar o CPF do usuário.
    """

    cpf = cpf.replace('.', '').replace('-', '')

    if cpf in list_cpfs:
        log('CPF já cadastrado.', 'ERRO')
        return False

    list_cpfs.append(cpf)

    if len(cpf) != 11 or not cpf.isdigit():
        log('CPF inválido. Deve conter 11 dígitos numéricos.', 'ERRO')
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * len(cpf):
        log('CPF inválido. Todos os dígitos são iguais.', 'ERRO')
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10

    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        return True

    else:
        log('CPF inválido. Dígitos verificadores não conferem.', 'ERRO')
        return False