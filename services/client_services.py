from utils.auxiliares import *

def cadastrar_cliente(clientes, list_cpfs=None, list_emails=None):

    log('Iniciando o cadastro do usuário.')

    cliente = dict()

    try:
        
        log('Digite os dados do usuário.')

        cliente['id'] = len(list_cpfs) + 1

        cliente['nome'] = input('Nome: ').strip().title()
        if not cliente['nome']:
            log('Nome não pode ser vazio.', 'ERRO')
            return False

        cliente['cpf'] = input('CPF: ').strip()
        if not validando_cpf(cliente['cpf'], list_cpfs):
            return False

        cliente['email'] = input('Email: ').strip()
        if not validando_email(cliente['email'], list_emails):
            return False

        cliente['telefone'] = input('Telefone: ').strip()

        data_nascimento = formata_data(input('Data de Nascimento (dd/mm/aaaa): ').strip())
        cliente['idade'] = calcular_idade(data_nascimento)

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

def buscar_cliente(clientes):
    """
    Função para buscar um cliente pelo ID ou CPF.
    """

    if not clientes:
        log('Nenhum cliente cadastrado.', 'ERRO')
        return True

    cpf_id = input("Digite o CPF ou ID do cliente que deseja buscar: ").strip()
    if not cpf_id:
        log('Entrada inválida. Por favor, digite um CPF ou ID.', 'ERRO')
        return False

    for cliente in clientes:
        if str(cliente['id']) == cpf_id or cliente['cpf'] == cpf_id:
            log('='*30)
            log('Cliente encontrado:'.center(30))
            log('='*30)

            log('='*30)
            log('Informações do usuário cadastrado:')
            for chave, item in cliente.items():
                log(f'{chave.capitalize()}: {item}')
            log('='*30)
            return True

    log('Com base nos dados informados para busca, não existe nenhum cliente correspondente.', 'ERRO')
    return False

def atualizar_cliente(clientes, list_cpfs, list_emails):
    log('Atualizando informações do cliente.')
    id_cliente = input('Digite o id do cliente que deseja atualizar: ').strip()
    
    try:
    
        for cliente in clientes:
            if id_cliente == str(cliente['id']):
                log("Cliente encontrado. Digite os novos dados (deixe em branco para manter o valor atual).")

                novo_nome = input(f'Nome ({cliente["nome"]}): ').strip().title()
                novo_cpf = input(f'CPF ({cliente["cpf"]}): ').strip()
                novo_email = input(f'Email ({cliente["email"]}): ').strip()
                novo_telefone = input(f'Telefone ({cliente["telefone"]}): ').strip()
                data_nascimento = formata_data(input('Data de Nascimento (dd/mm/aaaa): ').strip())

                if novo_nome:
                    cliente['nome'] = novo_nome
                if novo_cpf:
                    if validando_cpf(novo_cpf, list_cpfs):
                        cliente['cpf'] = novo_cpf
                if novo_email:
                    if validando_email(novo_email, list_emails):
                        cliente['email'] = novo_email
                if novo_telefone:
                    cliente['telefone'] = novo_telefone
                if data_nascimento:
                    cliente['idade'] = calcular_idade(data_nascimento)

                log('Informações do cliente atualizadas com sucesso!', 'SUCESSO')
                log('='*30)
                return True
    except Exception as e:
        log(f'Erro ao atualizar cliente: {e}', 'ERRO')
        return False

def excluir_cliente(clientes, list_cpfs, list_emails):
    log("Excluindo cliente do sistema.")
    log('='*30)
    for cliente in clientes:
        log(f'ID: {cliente["id"]}, Nome: {cliente["nome"]}')
    log('='*30)
    id_cliente = input('Digite o id do cliente que deseja excluir: ').strip()

    for cliente in clientes: 
        if id_cliente == str(cliente['id']):
            confirmacao = input(f'Tem certeza que deseja excluir o cliente {cliente["nome"]}? (s/n): ').strip().lower()[0]
            if confirmacao != 's':
                log('Exclusão cancelada.', 'ERRO')
                return False
            clientes.remove(cliente)
            list_cpfs.remove(cliente['cpf'])
            list_emails.remove(cliente['email'])
            log('Cliente excluído com sucesso!', 'SUCESSO')
            return True

    log('Cliente não encontrado.', 'ERRO')
    return False