from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Dizemos ao Python para criar um arquivo chamado 'musicas.db' na pasta atual
SQLALCHEMY_DATABASE_URL = "sqlite:///./musicas.db"

# O engine é o motor de conexão. O 'check_same_thread' é uma exigência específica do SQLite para o FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cada SessionLocal será uma sessão ativa para ler/gravar dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A classe Base será usada para criar os modelos de tabelas
Base = declarative_base()

# Função auxiliar (Dependência) que abre a conexão antes de uma rota rodar e fecha depois
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()