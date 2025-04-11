# aqui, estamos consultando todos os ids cadastrados dentro do nosso banco de dados e retornando ao módulo cadastrar.py

from database import Livro, SessionLocal

def buscarID():
    db = SessionLocal()

    try:
        idsOBJ = db.query(Livro).filter(Livro.id).all()

        idsList = []
        for id in idsOBJ:
            idsList.append(id.id)
        
        return idsList

    except Exception as e:
        print(f'[ERRO]. {e}')

    db.close()