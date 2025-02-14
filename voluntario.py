class Voluntario:
    def __init__(self, id, nome, contato, funcao):
        self.__id = id
        self.__nome = nome
        self.__contato = contato
        self.__funcao = funcao
        self.__escala = []
    
    def adicionar_escala(self, data, turno):
        self.__escala.append({'data': data, 'turno': turno})

    def get_dados(self):
        return (self.__id, self.__nome, self.__contato, self.__funcao)
