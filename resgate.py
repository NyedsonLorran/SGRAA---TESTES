class Resgate:
    def __init__(self, id, data, localidade):
        self.__id = id
        self.__data = data
        self.__localidade = localidade
        self.__animais_resgatados = []
    
    def adicionar_animal(self, animal_id):
        self.__animais_resgatados.append(animal_id)

    def get_dados(self):
        return (self.__id, self.__data, self.__localidade)