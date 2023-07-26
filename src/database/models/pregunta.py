from pydantic import BaseModel
#Entidad pregunta
class Pregunta(BaseModel):
    id: int | None
    enunciado: str
    respuesta_correcta: str
    respuesta_incorrecta1: str
    respuesta_incorrecta2: str
    respuesta_incorrecta3: str
    id_categoria: int

