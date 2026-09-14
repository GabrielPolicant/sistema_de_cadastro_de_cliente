from utils.auxiliares import *
from services.client_services import cadastrar_cliente

def main():

    log('Iniciando o sistema de cadastro de usuário.')
    while True:

        opcao = menu_option()

        if opcao == 6:
            log('Saindo do sistema. Até logo!', 'SUCESSO')
            break

        cliente = dict()
        list_cpfs = []

        if opcao == 1:
            if not cadastrar_cliente(cliente, list_cpfs):
                log('Falha ao cadastrar cliente.', 'ERRO')
                continue

if __name__ == "__main__":
    main()