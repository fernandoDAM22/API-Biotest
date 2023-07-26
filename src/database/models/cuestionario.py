from pydantic import BaseModel
#Entidad pregunta
class Cuestionario(BaseModel):
    id: int | None
    nombre: str
    descripcion: str
    id_categoria: int

