# importando a biblioteca SQL Alchemy para usar o SQLite

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

db_url = "sqlite:///biblioteca.db"

engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# criando a tabela 'LIVROS', onde ficarão registrados todos os livros da biblioteca.

class Livro(Base):
    __tablename__ = 'LIVROS'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    categoria = Column(String, nullable=False)
    qtd_estoque = Column(Integer, nullable=False)

Base.metadata.create_all(engine)