from pydantic import BaseModel
#Entidad pregunta
class Categoria(BaseModel):
    id: int | None
    nombre: str
    descripcion : str

