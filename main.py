<<<<<<< HEAD
from database import salvar_dados, carregar_dados

def menu():
    while True:
        print("\n=== Sistema de Gestão do Centro de Adoção ===")
        print("1. Cadastrar Animal")
        print("2. Listar Animais")
        print("3. Cadastrar Voluntário")
        print("4. Listar Voluntários")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            dados = input("Informe os dados do animal (id, especie, raca, idade, sexo, porte, cor, status, data_chegada): ")
            salvar_dados("animais.txt", dados)
        elif opcao == "2":
            print("Animais cadastrados:")
            print(''.join(carregar_dados("animais.txt")))
        elif opcao == "3":
            dados = input("Informe os dados do voluntário (id, nome, contato, funcao): ")
            salvar_dados("voluntarios.txt", dados)
        elif opcao == "4":
            print("Voluntários cadastrados:")
            print(''.join(carregar_dados("voluntarios.txt")))
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def main():
    print("Sistema de Gestão do Centro de Adoção inicializado.")
    menu()
    
if __name__ == "__main__":
    main()
=======
print("projeto testes")
>>>>>>> cd85d9ad778a0b734e153c7dfb28d00d81d4e094giyt
