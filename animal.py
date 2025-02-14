class Animal:
    def __init__(self, id, especie, raca, idade, sexo, porte, cor, status, data_chegada):
        self.__id = id
        self.__especie = especie
        self.__raca = raca
        self.__idade = idade
        self.__sexo = sexo
        self.__porte = porte
        self.__cor = cor
        self.__status = status
        self.__data_chegada = data_chegada
        self.__data_saida = None
        self.__tratamentos = []
    
    def registrar_tratamento(self, descricao, data):
        self.__tratamentos.append({'descricao': descricao, 'data': data})

    def get_dados(self):
        return (self.__id, self.__especie, self.__raca, self.__idade, self.__sexo, self.__porte, self.__cor, self.__status, self.__data_chegada)

