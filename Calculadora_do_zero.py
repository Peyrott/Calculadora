# PROJETO CALCULADORA
import os

def limpar_tela():
    
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def menu():
    #os.system("cls" if os.name == "nt" else "clear")

    print('\n\t ::::: CALCULADORA BÁSICA VICENTE PEYROT :::::\t\n')
    print('1 - ADICAO')
    print('2 - SUBTRACAO')
    print('3- MULTIPLICACAO')
    print('4 -DIVISAO')
    print('opção 9 - SAIR\n')
    val1 = int(input('Digite o primeiro valor: '))
    val2 = int(input('Digite o segundo valor: '))
    opcao= input('escolha a sua função: ')
    return opcao, val1,val2

def somar(val1,val2):
    resultado = val1 + val2
    return(resultado)
    
def sub(val1,val2):
    resultado = val1 - val2
    return(resultado)

def mult(val1,val2):
    resultado = val1 * val2
    return(resultado)

def div(val1,val2):
    resultado = val1 / val2
    return(resultado)


if __name__=="__main__":
   opcao = '0'
   val1 = 0
   val2 = 0

while opcao != '9':
    opcao, val1, val2 = menu()

    if opcao == '1':
         print(f'{val1} + {val2} = {somar(val1,val2)}')
         input("Pressione Enter para limpar a tela...")
         limpar_tela()
    elif opcao == '2':
        print(f'{val1} - {val2} = {sub(val1,val2)}')
        input("Pressione Enter para limpar a tela...")
        limpar_tela()
    elif opcao == '3':
         print(f'{val1} x {val2} = {mult(val1,val2)}')
         input("Pressione Enter para limpar a tela...")
         limpar_tela()
    elif opcao == '4':
         print(f'{val1} / {val2} = {div(val1,val2)}')
         input("Pressione Enter para limpar a tela...")
         limpar_tela()
    elif opcao == '9':
        print('Saindo...')
        input("Pressione Enter para limpar a tela...")
        limpar_tela()
        break
        
    else:
        print('Erro - Digite um numero valido')
        limpar_tela()
    