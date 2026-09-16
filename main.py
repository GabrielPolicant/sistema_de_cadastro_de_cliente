from utils.auxiliares import *
from services.client_services import cadastrar_cliente, listar_clientes

def main():

    log('Iniciando o sistema de cadastro de usuário.')

    clientes = list()
    list_cpfs = list()
    list_emails = list()

    while True:

        opcao = menu_option()

        if opcao == 6:
            log('Saindo do sistema. Até logo!', 'SUCESSO')
            break

        if opcao == 1:
            if not cadastrar_cliente(clientes, list_cpfs, list_emails):
                log('Falha ao cadastrar cliente.', 'ERRO')
                continue

        elif opcao == 2:
            if not listar_clientes(clientes):
                log('Falha ao listar clientes.', 'ERRO')
                continue

if __name__ == "__main__":
    main()