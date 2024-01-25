from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo:str
    autor:str
    paginas:int
    editorial:Optional[str]

@app.get("/")
def index():
    return {"menssage": "hola mundo"}

@app.get("/libros/{id}")
def mostraslibros(id:int):
    return {"data": id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}