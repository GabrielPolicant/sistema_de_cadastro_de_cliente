from utils.auxiliares import *
from services.client_services import cadastrar_cliente, listar_clientes, buscar_cliente

def main():

    log('Iniciando o sistema de cadastro de usuário.')

    clientes = list()
    list_cpfs = list()
    list_emails = list()

    while True:

        opcao = menu_option()

        if opcao == 6:
            log('Saindo do sistema. Até logo!', 'SUCESSO')
            limpar_tela()
            break

        if opcao == 1:
            limpar_tela()
            if not cadastrar_cliente(clientes, list_cpfs, list_emails):
                log('Falha ao cadastrar cliente.', 'ERRO')
                continue

        elif opcao == 2:
            limpar_tela()
            if not listar_clientes(clientes):
                log('Falha ao listar clientes.', 'ERRO')
                continue

        elif opcao == 3:
            limpar_tela()
            if not buscar_cliente(clientes):
                log('Falha ao buscar cliente.', 'ERRO')
                continue

if __name__ == "__main__":
    main()