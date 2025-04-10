# FUNÇÃO PARA CADASTRAR LIVROS

from database import SessionLocal, Livro

def cadastrarLivro():
    db = SessionLocal()  # variável para criar conexões com o banco de dados (fazer consultas, etc.)

    try:
        print('Se quiser voltar ao menu principal, digite 0.')
        id = int(input('Digite o ID do livro: '))

        if id == 0:
            return id
        
        while id < 0:
            print('[ERRO]. O ID não pode ser negativo. Digite um número válido.')
            id = int(input('Digite o ID do livro: '))

        titulo = input('Digite o título do livro: ')
        autor = input('Digite o autor do livro: ')
        anoPublicacao = int(input('Digite o ano de publicação do livro: '))
        categoria = input('Digite a categoria do livro: ')
        qtdEstoque = int(input('Digite quantas unidades terá em estoque: '))
        
        while qtdEstoque < 1:
            print('[ERRO]. Você deve inserir, pelo menos, um livro no estoque.')
            qtdEstoque = int(input('Digite quantas unidades terá em estoque: '))
        
        novoLivro = Livro(id=id, titulo=titulo, autor=autor, ano_publicacao=anoPublicacao, categoria=categoria, qtd_estoque=qtdEstoque)

        db.add(novoLivro)
        db.commit()
        db.close()

        print('Livro cadastrado com sucesso!')
    
    except Exception as e:
        db.rollback()
        print(f'Erro ao cadastrar o livro: {e}')
