# aqui, verificaremos a disponibilidade de um livro para emprestá-lo a um leitor, ou cadastrar a devolução do livro emprestado.

from database import SessionLocal, Livro

def verificarEstoque():
    db = SessionLocal()

    try:
        print('Você deseja pegar um livro emprestado ou devolver um livro?')
        print('1- Pegar emprestado')
        print('2- Devolver')
        resp = int(input('Escolha a opção desejada: '))

        if resp == 1:
            nomeLivro = input('Digite o nome do livro que quer devolver: ')
            livrosEncontrados = db.query(Livro).filter(Livro.titulo.ilike(f'%{nomeLivro}%')).all()
            listaLivros = []
            idLivros = []

            if livrosEncontrados:
                print(f'Aqui estão os livros encontrados:')

                for livro in livrosEncontrados:
                    print(f'Título: {livro.titulo}. ID: {livro.id}')
                    listaLivros.append(livro.titulo)
                    idLivros.append(livro.id)

                if len(listaLivros) > 1:
                    idLivro = int(input('Digite o ID do livro que quer pegar emprestado: '))

                pegarEmprestado(nomeLivro)
    
    except Exception as e:
        print(f'[ERRO]. {e}')

def pegarEmprestado(livro):
    pass


def devolver():
    pass