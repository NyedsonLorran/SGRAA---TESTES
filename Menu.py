from database import salvar_dados, carregar_dados

class Menu:

    def coletarDadosPretendente(self):
        tipos = ["informações pessoais", "nome", "contato", "endereço"]
        concatena = ""
        for i in range(0,(len(tipos))):
            inf = input(f"informe o {tipos[i]}: ")
            if inf == "0":
                inf = " "
                pass
            elif inf == "00":
                inf = " "
                break
            concatena += (inf + ",")
        return concatena

    def coletarDadosAnimal(self):
        tipos = ["id", "especie", "raca", "idade", "sexo", "porte", "cor", "status", "data_chegada", "data_saida"]
        concatena = ""
        for i in range(0,len(tipos)):
            inf = input(f"informe o {tipos[i]}: ")
            if inf == "0":
                inf = " "
                pass
            elif inf == "00":
                inf = " "
                break
            concatena += (inf + ",")
        return concatena

    def coletarDadosVoluntario(self):
        tipos = ["id", "nome", "contato", "funcao"]
        concatena = ""
        for i in range(0,len(tipos)):
            inf = input(f"informe o {tipos[i]}: ")
            if inf == "0":
                inf = " "
                pass
            elif inf == "00":
                inf = " "
                break
            concatena += (inf + ",")
        return concatena

    def menu(self):
        while True:
            print("\n=== Sistema de Gestão do Centro de Adoção ===")
            print("1. Cadastrar Animal")
            print("2. Listar Animais")
            print("3. Cadastrar Voluntário")
            print("4. Listar Voluntários")
            print("5. Cadastrar Pretendente")
            print("6. Listar Pretendentes")
            print("7. Registrar Doação")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                print("Informe os dados do animal: (digite 0 se tiver a informação e 00 para encerrar)")
                print("==================================")
                dados = self.coletarDadosAnimal()
                salvar_dados("animais.txt", dados)
            elif opcao == "2":
                print("Animais cadastrados:")
                print(''.join(carregar_dados("animais.txt")))
            elif opcao == "3":
                print("Informe os dados do voluntário: (digite 0 se tiver a informação e 00 para encerrar)")
                dados = self.coletarDadosVoluntario()
                salvar_dados("voluntarios.txt", dados)
            elif opcao == "4":
                print("Voluntários cadastrados:")
                print(''.join(carregar_dados("voluntarios.txt")))
            elif opcao == "5":
                print("Registrar pretendente a adoção")
                dados = self.coletarDadosPretendente()
                salvar_dados("pretendente.txt", dados)
            elif opcao == "6":
                print("Pretendentes cadastrados:")
                print(''.join(carregar_dados("voluntarios.txt")))
            elif opcao == "7":
                print("Registrar Doação")
                pass
            else:
                print("Opção inválida! Tente novamente.")