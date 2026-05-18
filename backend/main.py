from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 1. Importe o middleware
from pydantic import BaseModel, Field

app = FastAPI(title="Minha API de Músicas")

# 2. Configure quais origens podem acessar sua API (vamos liberar tudo por enquanto para facilitar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer frontend acesse a API localmente
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],
)

class Album(BaseModel):
    titulo: str
    artista: str
    ano: int
    nota: int = Field(..., ge=0, le=10) 
    comentario: str
    capa_url: str

meus_albuns = [
    {
        "titulo": "Reise, Reise",
        "artista": "Rammstein",
        "ano": 2004,
        "nota": 10,
        "comentario": "Pessoalmente meu álbum favorito da banda, onde acredito terem alcançado o ponto de equilíbrio entre maturidade e agressividade sonora, além de letras mais profundas e interessantes.",
        "capa_url": "https://dn710605.ca.archive.org/0/items/mbid-2f55fcce-b536-3ec4-92f7-54f5f8fa1edf/mbid-2f55fcce-b536-3ec4-92f7-54f5f8fa1edf-21713078387.jpg"
    },
    {
        "titulo": "Deliverance",
        "artista": "Opeth",
        "ano": 2002,
        "nota": 10,
        "comentario": "A cada audição essa peça se torna melhor. O ápice da fase mais pesada da banda após os 3 primeiros álbuns, com uma produção crua, agressiva e bruta, mas sem perder a complexidade e a melodia características da banda.",
        "capa_url": "https://ia801600.us.archive.org/23/items/mbid-777871be-214d-4a9c-9476-978acd1c44c5/mbid-777871be-214d-4a9c-9476-978acd1c44c5-17989501029.jpg"
    }
]

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API do meu site de reviews de músicas!"}

@app.get("/api/albuns")
def listar_albuns():
    return meus_albuns

@app.post("/api/albuns")
def adicionar_album(album: Album):

    novo_album = album.model_dump()

    novo_album["id"] = len(meus_albuns) + 1

    meus_albuns.append(novo_album)
    return {"mensagem": "Avaliação adicionada", "album": novo_album}

