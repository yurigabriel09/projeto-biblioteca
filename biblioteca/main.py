# arquivo principal para execução do programa
# para executá-lo, escreva 'py main.py' no terminal do vs code.

from opcoes.cadastrar import cadastrarLivro
from opcoes.consultar import consultarLivro, consultarAutor

def main():
    while True:
        def validarOpcao():
            numValidos = [1, 2, 3, 4, 5, 6, 7, 8]
            while True:
                try:   
                    num = int(input())

                    if num in numValidos:
                        break
                    else:
                        print('[ERRO]. Digite uma opção válida!\n')
                        
                except:
                    print('[ERRO]. Digite uma opção válida!\n')
                            
            if num == 1:
                resposta = cadastrarLivro()
                if resposta == 0:
                    main()

            elif num == 2:
                resposta = consultarLivro()
                if resposta == '0':
                    main()

            elif num == 3:
                consultarAutor()
                if resposta == 0:
                    main()

            elif num == 8:
                return None
            
            elif num > 3 and num < 8:
                # aqui, vou colocar uma sequencia de if e else para verificar o numero digitado.
                # dependendo do numero digitado, chamarei uma função correspondente.
                print('Funcionando!')
                return None
            

        print('\nOlá! Seja bem-vindo(a) ao nosso sistema bibliotecário. Escolha um dos números abaixo para continuar:')
        print('1. Cadastrar um livro')
        print('2. Consultar um livro')
        print('3. Consultar um autor')
        print('4. Consultar uma categoria')
        print('5. Emprestar/Devolver')
        print('6. Editar um livro')
        print('7. Excluir um livro')
        print('8. Sair')
        print('')

        exec = validarOpcao()
        if exec == None:
            break


main()