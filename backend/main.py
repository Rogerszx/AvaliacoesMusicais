from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Minha API de Músicas com Banco de Dados")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class AlbumSchema(BaseModel):
    titulo: str
    artista: str
    ano: int
    nota: float = Field(..., ge=0, le=10)
    comentario: str
    capa_url: str

@app.get("/")
def home():
    return {"mensagem": "API com banco de dados ativa."}

# ROTA GET: Busca os álbuns salvos no banco de dados
@app.get("/api/albuns")
def listar_albuns(db: Session = Depends(get_db)):
    # O SQLAlchemy faz um 'SELECT * FROM albuns' por baixo dos panos
    albuns_do_banco = db.query(models.AlbumModel).all()
    return albuns_do_banco

# ROTA POST: Salva um novo álbum no banco de dados
@app.post("/api/albuns")
def adicionar_album(album: AlbumSchema, db: Session = Depends(get_db)):
    # Transforma os dados que vieram do site em um modelo de banco de dados
    novo_album = models.AlbumModel(
        titulo=album.titulo,
        artista=album.artista,
        ano=album.ano,
        nota=album.nota,
        comentario=album.comentario,
        capa_url=album.capa_url
    )
    
    db.add(novo_album)      # Coloca o álbum na fila para salvar
    db.commit()             # Grava de fato no arquivo do HD!
    db.refresh(novo_album)  # Atualiza o objeto para pegar o ID gerado pelo banco
    
    return {"mensagem": "Salvo no banco de dados!", "album": novo_album}