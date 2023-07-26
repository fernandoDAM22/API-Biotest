from pydantic import BaseModel
#Entidad user
class User(BaseModel):
    id: int | None
    nombre: str
    contrasena: str | None
    email: str
    telefono: str
    tipo: str
