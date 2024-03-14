
from typing import Optional, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Animal(BaseModel):
    id : Optional[str]
    name : str
    idade : int
    sexo : str
    cor : str


banco: List[Animal] = []



@app.get('/animais')
def lista_animais():
    return banco

@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return ("Animal cadastrado!")

@app.get('/animais/{id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal_id == animal_id:
            return animal
    return ('Animal não encontrado!')

@app.delete('/animais/{id}')
def deletar_animal(animal_id: str):
    for animal in banco:
        if animal_id == animal_id:
            banco.remove(animal)
    else:
        return ('Animal com id especificado não encontrado!')