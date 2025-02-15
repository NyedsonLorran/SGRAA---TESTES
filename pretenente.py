class Pretendente:
    def __init__(self, id, nome, contato, endereco):
        self.__id = id
        self.__nome = nome
        self.__contato = contato
        self.__endereco = endereco
        self.__adocoes = []
    
    def registrar_adocao(self, animal_id, data, termo_assinado):
        self.__adocoes.append({'animal_id': animal_id, 'data': data, 'termo_assinado': termo_assinado})

    def get_dados(self):
        return (self.__id, self.__nome, self.__contato, self.__endereco)

    def getAdocoes(self):
        return self.__adocoes