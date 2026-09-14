import colorama

def log(mensagem, cor, tipo):

    cor = cor.upper().strip()
    tipo = tipo.upper().strip()
    
    colorama.init(autoreset=True)

    if tipo == 'info':
        print(f'{cor}[INFO] {mensagem}')

    elif tipo == 'erro':
        print(f'{cor}[ERRO] {mensagem}')

    elif tipo == 'sucesso':
        print(f'{cor}[SUCESSO] {mensagem}')

    else:
        print(f'{cor}[LOG] {mensagem}')