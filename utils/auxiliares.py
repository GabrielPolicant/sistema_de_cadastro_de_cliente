import colorama
import time
from datetime import datetime
import os

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

def limpar_tela():
    # 'cls' se for Windows ('nt'), 'clear' se for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_option():

    log('='*30, cor=colorama.Fore.BLUE)
    log('SISTEMA DE CLIENTES'.center(30), cor=colorama.Fore.GREEN)
    log('='*30, cor=colorama.Fore.BLUE)

    log("1 - Cadastrar Cliente")
    log("2 - Listar Clientes")
    log("3 - Buscar Cliente")
    log("4 - Atualizar Cliente")
    log("5 - Excluir Cliente")
    log("0 - Sair")
        
    log('='*30, cor=colorama.Fore.BLUE)

    try:
        opcao = int(input('Escolha uma opção: '))

        if opcao not in [1, 2, 3, 4, 5, 0]:
            log('Opção inválida. Digite um número entre 1 e 5 ou 0 para sair.', 'ERRO')
            return False

        time.sleep(1)
        if opcao:
            return opcao
        elif str(opcao) == '0':
            return 0

    except ValueError:
        log('Entrada inválida. Por favor, digite um número.', 'ERRO')
        return False

def validando_cpf(cpf, session, Cliente):
    """
    Função para validar o CPF do usuário.
    """

    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        log('CPF inválido. Deve conter 11 dígitos numéricos.', 'ERRO')
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * len(cpf):
        log('CPF inválido. Todos os dígitos são iguais.', 'ERRO')
        return False

    cpf_existente = session.query(Cliente).filter(Cliente.cpf == cpf).first()


    if cpf_existente:
        log('CPF já cadastrado.', 'ERRO')
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

def formata_data(entrada):
    """
    Função para formatar a data de nascimento do usuário.
    """

    try:
        if len(entrada) == 8 and entrada.isdigit():
            data_nascimento = f"{entrada[:2]}/{entrada[2:4]}/{entrada[4:]}"
        else:
            data_nascimento = entrada

        return data_nascimento

    except ValueError:
        log('Data de nascimento inválida. Use o formato dd/mm/aaaa.', 'ERRO')
        return None

def calcular_idade(data_nascimento):
    """
    Função para calcular a idade do usuário a partir da data de nascimento.
    """

    try:

        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        hoje = datetime.now()
        idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
        return idade

    except ValueError:
        log('Data de nascimento inválida. Use o formato dd/mm/aaaa.', 'ERRO')
        return None

def validando_email(email, session, Cliente):

    """
    Função para validar o email do usuário.
    """

    if not email:
        log('Email não pode ser vazio.', 'ERRO')
        return False

    if '@' not in email or '.' not in email:
        log('Email inválido. Deve conter "@" e ".".', 'ERRO')
        return False

    email_existente = session.query(Cliente).filter(Cliente.email == email).first()
    if email_existente:
        log('Email já cadastrado.', 'ERRO')
        return False

    return True