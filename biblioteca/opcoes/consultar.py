# aqui ficará a função para consultar qualquer livro de maneira individual, qualquer autor de maneira individual, ou consultar todos os livros de uma categoria especifica.

from database import SessionLocal, Livro


def consultarLivro():

    print('Digite 0 se quiser voltar ao menu principal.')
    nomeLivro = input('Digite o nome do livro que deseja consultar: ')
    if nomeLivro == '0':
        return nomeLivro
    else:
        buscarLivro(nomeLivro)


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


def consultarAutor():

    print('Digite 0 se quiser voltar ao menu principal.')
    nomeAutor = input('Digite o nome do autor que deseja consultar: ')
    if nomeAutor == '0':
        return nomeAutor
    else:
        buscarAutor(nomeAutor)
    

def buscarAutor(autor):
    db = SessionLocal()

    try:
        autoresEncontrados = db.query(Livro).filter(Livro.autor.ilike(f'%{autor}%')).all()

        if autoresEncontrados:
            print('\nAqui estão os autores encontrados!\n')
            for autor in autoresEncontrados:
                print(f'{autor.autor}, {autor.titulo}')
            
            # perguntar se ele quer pegar algum livro do autor emprestado

        else:
            print('\nNão foi encontrado nenhum autor(a) com esse nome!')
        
        db.close()

    except Exception as e:
        db.rollback()
        print(f'[ERRO]. {e}')


def consultarCategoria():

    print('Essas são as categorias disponíveis:')
    print(f'[ Biografia, Fantasia, Poesia, Romance, Suspense ].')
    print('\nDigite 0 se quiser voltar ao menu.')

    categoria = input('Digite a categoria que você quer consultar: ').capitalize()
    if categoria == '0':
        return categoria
        
    categorias = ['Biografia', 'Fantasia', 'Poesia', 'Romance', 'Suspense']

    while categoria not in categorias:
        categoria = input('\nCategoria inválida! Digite novamente ou digite 0 pra voltar ao menu: ').capitalize()

        if categoria == '0':
            return categoria
    else:
        buscarCategoria(categoria)


def buscarCategoria(categoria):
    db = SessionLocal()

    try:
        print(f'\nAqui estão os livros da categoria {categoria}:\n')
        livros = db.query(Livro).filter(Livro.categoria == categoria).all()

        if livros:
            for livro in livros:
                print(f'{livro.titulo}, {livro.autor}. Quantidade em estoque: {livro.qtd_estoque}')
        else:
            print(f'Ainda não temos nenhum livro cadastrado na categoria {categoria}!')

    except Exception as e:
        print(f'[ERRO]. {e}')