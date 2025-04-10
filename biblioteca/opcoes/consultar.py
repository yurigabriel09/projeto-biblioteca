# aqui ficará a função para consultar qualquer livro de maneira individual, qualquer autor de maneira individual, ou consultar todos os livros de uma categoria especifica.

from database import SessionLocal, Livro

def consultarLivro():
    print('\nDigite 0 se quiser voltar ao menu principal.')
    nomeLivro = input('Digite o nome do livro que deseja consultar: ')
    if nomeLivro == '0':
        return nomeLivro
    else:
        buscarLivro(nomeLivro)


def consultarAutor():
    nomeAutor = input('Digite o nome do autor que deseja consultar: ')
    buscarAutor(nomeAutor)


def buscarLivro(livro):
    db = SessionLocal()

    try:
        livrosEncontrados = db.query(Livro).filter(Livro.titulo.ilike(f'%{livro}%')).all()
        # .ilike torna a sentença case-insensitive (ignora maiusculas e minusculas)
        # o sinal de % no começo e no fim da string retorna valores aproximados. por exemplo, se digitar só metade do nome, ele vai associar e retornar um valor correspondente.
        # .all() serve para retornar todos os resultados encontrados

        if livrosEncontrados:
            print('\nAqui estão os livros encontrados!\n')
            for livro in livrosEncontrados:
                print(f'ID: {livro.id} - {livro.titulo}, {livro.autor}. Quantidade em estoque: {livro.qtd_estoque}')

            # perguntar se ele quer pegar algum livro emprestado, digitar o ID

        else:
            print('Não foi encontrado nenhum livro com este título!')
        
        db.close()

    except Exception as e:
        db.rollback()
        print(f'[ERRO]. {e}')


def buscarAutor(autor):
    db = SessionLocal()

    try:
        autoresEncontrados = db.query(Livro).filter(Livro.autor.ilike(f'%{autor}%')).all()

        if autoresEncontrados:
            print('Aqui estão os autores encontrados!')
            for autor in autoresEncontrados:
                print(f'{autor.autor}, {autor.titulo}')
            
            # perguntar se ele quer pegar algum livro do autor emprestado

        else:
            print('Não foi encontrado nenhum autor(a) com esse nome!')
        
        db.close()

    except Exception as e:
        db.rollback()
        print(f'[ERRO]. {e}')