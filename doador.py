class Doador:
    def __init__(self, id, nome, tipo, contato):
        self.__id = id
        self.__nome = nome
        self.__tipo = tipo  # Individual ou Instituicao
        self.__contato = contato
        self.__doacoes = []
    
    def registrar_doacao(self, item, quantidade, data):
        self.__doacoes.append({'item': item, 'quantidade': quantidade, 'data': data})

    def get_dados(self):
        return (self.__id, self.__nome, self.__tipo, self.__contato)