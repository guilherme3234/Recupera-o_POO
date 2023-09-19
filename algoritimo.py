from classes import*
import os 

def main():
 while True:
    try:  
        print("--MENU--")
        print("[1] - Cadastrar")
        print("[2] - Login")
        print("[3] - sacar")
        print("[4] - depositar")
        print("[5] - transferir")
        print("[6] - saldo")
        print("[7] - sair")
        print("")
        menu = int(input(">"))
        os.system("Pause")
        
        match menu:
            case 1:
               print("informe seu nome")
               print("informe seu CPF")
               print("informe seu email")
               print("informe sua data de nacimento")
               print("Cadastro concluido")
               Listar_Cadastar_cliente = []
               os.system("cls")
               os.system("pause")
            
            case 2:
               print("informe seu nome")
               print("informe seu CPF")
               os.system("cls")
               os.system("pause")
            
            case 3:
              print("Qual o valor que dejesa depositar? ")
           
            case 4:
              pass
             
            case 5:
              pass
            
            case 6:
              pass
           
            case 7:
              pass
           
            case _:
              print("opção invalida!")
            
    except Exception as erro:
        print(ValueError)