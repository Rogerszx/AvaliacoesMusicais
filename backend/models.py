from sqlalchemy import Column, Integer, String, Float
from database import Base

class AlbumModel(Base):
    __tablename__ = "albuns"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True) # ID numérico e único
    titulo = Column(String)
    artista = Column(String)
    ano = Column(Integer)
    nota = Column(Float)
    comentario = Column(String)
    capa_url = Column(String)