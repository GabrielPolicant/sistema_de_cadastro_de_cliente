from utils.auxiliares import *

def cadastrar_cliente(clientes, list_cpfs=None, list_emails=None):

    log('Iniciando o cadastro do usuário.')

    cliente = dict()

    try:
        
        log('Digite os dados do usuário.')

        cliente['id'] = len(list_cpfs) + 1
        cliente['nome'] = input('Nome: ').strip().title()
        cliente['cpf'] = input('CPF: ').strip()
        cliente['email'] = input('Email: ').strip()
        cliente['telefone'] = input('Telefone: ').strip()
        data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ').strip()

        cliente['idade'] = calcular_idade(data_nascimento)

        #Validando informações do cliente
        if not cliente['nome']:
            log('Nome não pode ser vazio.', 'ERRO')
            return False

        if not validando_cpf(cliente['cpf'], list_cpfs):
            return False

        if not validando_email(cliente['email'], list_emails):
            return False

        log('Usuário cadastrado com sucesso!', 'SUCESSO')

        log('='*30)
        log('Informações do usuário cadastrado:')
        for chave, item in cliente.items():
            log(f'{chave.capitalize()}: {item}')
        log('='*30)

        clientes.append(cliente)
        return True
        
    except Exception as e:
        log(f'Erro na hora do cadastro, erro: {e}.', 'ERRO')
        return False

def listar_clientes(clientes):
    """
    Função para listar os clientes cadastrados.
    """

    if not clientes:
        log('Nenhum cliente cadastrado.', 'ERRO')
        return False

    log('='*30)
    log('Listando clientes cadastrados:'.center(30))
    log('='*30)

    for cliente in clientes:
        log('-'*30)
        log(f"""
    ID: {cliente['id']}, 
    Nome: {cliente['nome']}, 
    CPF: {cliente['cpf']}, 
    Email: {cliente['email']}, 
    Telefone: {cliente['telefone']}, 
    Idade: {cliente['idade']}
        """)

    return True