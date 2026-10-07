from utils.auxiliares import *
from database.database import engine, Base
from models.client import Cliente
from services.client_services import cadastrar_cliente, listar_clientes, buscar_cliente, atualizar_cliente, excluir_cliente

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

def main():

    log('Iniciando o sistema de cadastro de usuário.')

    clientes = list()
    list_cpfs = list()
    list_emails = list()

    while True:

        opcao = menu_option()

        if opcao == 0:
            log('Saindo do sistema. Até logo!', 'SUCESSO')
            time.sleep(2)
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

        elif opcao == 4:
            limpar_tela()
            if not atualizar_cliente(clientes, list_cpfs, list_emails):
                log('Falha ao atualizar cliente.', 'ERRO')
                continue

        elif opcao == 5:
            limpar_tela()
            if not excluir_cliente(clientes, list_cpfs, list_emails):
                log('Falha ao excluir cliente.', 'ERRO')
                continue

if __name__ == "__main__":
    main()