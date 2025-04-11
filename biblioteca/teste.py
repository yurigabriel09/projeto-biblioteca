# arquivo para mostrar todos os livros cadastrados no banco de dados.

from database import SessionLocal, Livro
from opcoes.verificacoes.id import buscarID

db = SessionLocal()  # cria uma conexao com o banco de dados. serve para fazer a consulta dos livros!!

livros = db.query(Livro).all()  # cria uma query que retorna um objeto contendo todos os livros encontrados

for livro in livros:
    print(f"{livro.id} - {livro.titulo} - {livro.autor} - {livro.categoria} - {livro.ano_publicacao} - {livro.qtd_estoque} ")

db.close()

buscarID()


def excluirTeste():
    db = SessionLocal()

    try:
        db.query(Livro).filter(Livro.categoria != 'Fantasia').delete()
        livros = db.query(Livro).all()

        for livro in livros:
            print(f'{livro.id}, {livro.titulo}')

    except Exception as e:
        print(f'[ERRO]. {e}')

    db.commit()
    db.close()

# excluirTeste()