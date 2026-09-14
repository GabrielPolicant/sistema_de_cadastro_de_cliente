from utils.auxiliares import *

def cadastrar_cliente(cliente, list_cpfs=None, list_emails=None):

    log('Iniciando o cadastro do usuário.')

    try:
        
        log('Digite os dados do usuário.')

        cliente['id'] = len(list_cpfs) + 1
        cliente['nome'] = input('Nome: ').strip().title()
        cliente['cpf'] = input('CPF: ').strip()
        cliente['email'] = input('Email: ').strip()
        cliente['telefone'] = input('Telefone: ').strip()
        data_nascimento = input('Data de Nascimento (dd/mm/aaaa): ').strip()

        #Validando informações do cliente
        if not cliente['nome']:
            log('Nome não pode ser vazio.', 'ERRO')
            return False

        if not validando_cpf(cliente['cpf'], list_cpfs):
            return False

        log('Usuário cadastrado com sucesso!', 'SUCESSO')
        
        for chave, item in cliente.items():
            log(f'{chave.capitalize()}: {item}')

        return True
        
    except Exception as e:
        log(f'Erro na hora do cadastro, erro: {e}.', 'ERRO')
        return False