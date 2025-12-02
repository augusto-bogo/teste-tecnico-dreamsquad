from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()
load_dotenv()

class Pergunta(BaseModel):
    message: str

class Resposta(BaseModel):
    response: str

@app.post("/chat", response_model=Resposta)
def chat(req: Pergunta):
    result = agent(req.message)
    return Resposta(response=str(result))
