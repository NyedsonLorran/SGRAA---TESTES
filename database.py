def salvar_dados(arquivo, dados):
    with open(arquivo, 'a') as f:
        f.write(dados + '\n')

def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def buscar_dado(arquivo, termo):
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                if termo in linha:
                    return linha.strip()
    except FileNotFoundError:
        return None
    return None
