from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 1. Importe o middleware

app = FastAPI(title="Minha API de Músicas")

# 2. Configure quais origens podem acessar sua API (vamos liberar tudo por enquanto para facilitar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer frontend acesse a API localmente
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],
)

meus_albuns = [
    {
        "id": 1,
        "titulo": "Reise, Reise",
        "artista": "Rammstein",
        "ano": 2004,
        "nota": 10,
        "comentario": "Meu álbum favorito da banda, com uma sonoridade única e letras impactantes.",
        "capa_url": "https://upload.wikimedia.org/wikipedia/en/a/a6/Rammstein_Reise_Reise.jpg"
    },
    {
        "id": 2,
        "titulo": "Deliverance",
        "artista": "Opeth",
        "ano": 2002,
        "nota": 10,
        "comentario": "Um álbum marcante da banda, que demonstra sua evolução sonora e habilidade composicional.",
        "capa_url": "https://upload.wikimedia.org/wikipedia/en/5/53/Opeth_-_Deliverance.jpg"
    }
]

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API do meu site de reviews de músicas!"}

@app.get("/api/albuns")
def listar_albuns():
    return meus_albuns