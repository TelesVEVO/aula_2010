from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AAAAAAAAAAAAAAAAAA",
    description="scsdaca",
    docs_uri='/docs' #Habilita o Swagger
)

class InfoPrevisao(BaseModel):
    empresa: str
    volume : float
    prev_fecham : float

@app.get("/")
async def root():
    return {"status": True,
            "message": "Serviço Operando Normalmente"}

@app.get("/predict")
def previsoes(payload: InfoPrevisao) :
    
    if InfoPrevisao.empresa == "aapl":
        w0, w1, w2 = [15.36, 1.06, -3.23]
        previsao = w0 + w1 * InfoPrevisao.prev_fecham + w2 * InfoPrevisao.volume
    else:
        previsao = None

    return {"profecia": previsao}