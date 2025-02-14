def salvar_dados(arquivo, dados):
    with open(arquivo, 'a') as f:
        f.write(dados + '\n')

def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []