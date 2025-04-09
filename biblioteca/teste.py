# arquivo para mostrar todos os livros cadastrados no banco de dados.

from database import SessionLocal, Livro

db = SessionLocal()  # cria uma conexao com o banco de dados. serve para fazer a consulta dos livros!!

livros = db.query(Livro).all()  # cria uma query que retorna um objeto contendo todos os livros encontrados

for livro in livros:
    print(f"{livro.id} - {livro.titulo} - {livro.autor} - {livro.categoria} - {livro.ano_publicacao} - {livro.qtd_estoque} ")

db.close()