#Esta clase implementa el mecanismo de autenticacion

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from database.querys import consultasUsuario
from database.models.usuario import User
import hashlib
from passlib.context import CryptContext
from tools import exceptions

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 60
SECRET = "7ce95d4de48274d42ab8c4aec12567411c91a21d1969320d352af2c502217bc3"
router = APIRouter(prefix="/login", responses={
    404: {
        "message": "no encontrado"
    }
}, tags=["login"])

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


def verify_password(password: str, password_hash: str) -> bool:
    """
    Esta funcion permite verificar que una contrasena coincide con su hash 
    Params: 
        password: es la contrasena que queremos comprobar
        password_hash: es el hash con el cual se va a comprobar la contrasena
    Return:
        true si la contrasena coincide con el hash, false si no
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password == password_hash

async def auth_user(token: str = Depends(oauth2)) -> User:
    """
    Esta funcion permite obtener un usuario de la base de datos a partir de su token
    Params:
        token: es el token del usuario
    Return:
        el usuario al cual pertenece el token, null en caso de que el token no pertenezca a ningun usuario
    Raise
        JWTError: en caso de que ocurra algun error con la decodificacion del token
    """
    try:
        #obtenemos los datos del usuario a partir del token
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username = payload.get("name")
        password = payload.get("password")
        if username is None or password is None:
            raise exceptions.CREDENCIALES_INVALIDAS
    except JWTError:
        raise exceptions.CREDENCIALES_INVALIDAS
    return search_user_password(username, password)


def search_user(name: str, password: str) -> User:
    """
    Esta funcion permite obtener un usuario a partir de su nombre y su contrasena
    Params:
        name: es el nombre del usuario
        password: es la contrasena del usuario
    Return: 
        el usuario en caso de que las credenciales sean correctas, null si son incorrectas
    """
    #obtenemos el usuario
    user = consultasUsuario.obtener_usuario_por_nombre(name)
    if user is not None:
        #comprobamos su contrena y si es correcto retornamos el usuario
        password_hash = user.contrasena
        if verify_password(password, password_hash):
            return user

def search_user_password(name: str, password: str) -> User:
    """
    Este metodo permite obtener un usuario de la base de datos, teniendo su contrasna cifrada
        Params:
        name: es el nombre del usuario
        password: es la contrasena cifrada del usuario
    Return: 
        el usuario en caso de que las credenciales sean correctas, null si son incorrectas
    """
    user = consultasUsuario.obtener_usuario_por_nombre(name)
    print(user)
    if user is not None:
        if password == user.contrasena:
            print("correcto")
            return user


async def current_user(user: User = Depends(auth_user)) -> User:
    """
    Este metodo retorna el usuario del cual se espeficica el token
    Return:
        El usuario si el token es valido, null si no lo es
    """
    return user

@router.post("/")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    Esta funcion permite obtener el token de acceso de un usuario,
    las credenciales del usuario se obtienen a traves del formulario de la peticion
    Return:
        El token del usuario en caso de que las credenciales sean correctas
    """
    #Obtenemos el usuario
    user = search_user(form.username, form.password)
    if user is None:
        raise exceptions.LOGIN_INCORRECTO
    #creamos su token
    access_token = {
        "name": user.nombre,
        "password": user.contrasena,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    #lo retornamos
    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }
