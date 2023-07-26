from fastapi import APIRouter,status
from routes.jwt_auth_users import current_user
from fastapi import Depends
from database.models.usuario import User
from tools import exceptions
from database.querys import consultasUsuario

router = APIRouter(prefix="/usuarios",responses={
    404:{
        "message" : "no encontrado"
    }
},tags=["usuarios"])

@router.get("/",status_code=status.HTTP_200_OK,response_model=list[User],
            response_description="Respuesta existosa",
            summary="Obtener todos los usuarios de la base de datos")
async def obtener_usuarios(user: User = Depends(current_user)):
    """
    Este metodo permite devolver todos los usuarios de la base de datos
    Return:
        Una lista con todos los usuarios de la base de datos
    """
    return consultasUsuario.obtener_usuario
@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=User,
            response_description="Respuesta existosa",
            summary="Obtener un usuario de la base de datos a partir de su id")
async def obtener_usuario(id: int,user: User = Depends(current_user)):
    """
    Este metodo permite obtener un usuario de la base de datos
    a partir de su id
    Param:
        id: es el id del usuario que queremos obtener
    Return:
        El usuario con el id indicado si existe, none si no existe
    """
    usuario = consultasUsuario.obtener_usuario(id)
    if usuario is None:
        raise exceptions.USUARIO_NO_EXISTE
    else:
        return usuario

@router.get("/nombre/{name}",status_code=status.HTTP_200_OK,response_model=User,
            response_description="Respuesta existosa",
            summary="Obtener un usuario de la base de datos a partir de su nombre")
async def obtener_usuario_por_nombre(name: str,user: User = Depends(current_user)):
    """
    Este metodo permite obtener un usuario de la base de datos
    a partir de su nombre
    Param:
        nombre: es el nombre del usuario que queremos obtener
    Return:
        El usuario con el nombre indicado si existe, none si no existe
    """
    usuario = consultasUsuario.obtener_usuario_por_nombre(name)
    if usuario is None:
        raise exceptions.USUARIO_NO_EXISTE
    else:
        return usuario

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=dict,
            response_description="Respuesta existosa",
            summary="Inserta un usuario en la base de datos")
async def insertar_cuestionario(usuario: User):
    """
    Este metodo permite insertar un usuario en la base de datos
    Param:
        usuario: es el usuario que se va a insertar en la base de datos
    Return:
        un dict indicado que se a insertado el usuario correctamente
    Raise:
        USUARIO_YA_EXISTE: en caso de que se intente insertar un cuestionario que ya existe
        ERROR_INSERTAR_USUARIO: en caso de que ocurra algun error al insertar el cuestionario 
    """
    if type(consultasUsuario.obtener_usuario_por_nombre(usuario.nombre)) == User:
        raise exceptions.USUARIO_YA_EXISTE
    if consultasUsuario.insertar_usuario(usuario):
        return {
            "detail" : "usuario insertado correctamente"
        }
    else:
        raise exceptions.ERROR_INSERTAR_USUARIO

@router.put("/",status_code=status.HTTP_201_CREATED,response_model=dict,
            response_description="Respuesta existosa",
            summary="modifica un usuario de la base de datos")
async def modificar_usuario(usuario: User, user: User = Depends(current_user)):
    """
    Este metodo permite modificar un usuario de la base de datos
    Param:
        usuario: es el usuario que se va a modificar
    Return:
        un dict indicado que se a modificado el usuario correctamente
    Raise:
        FORBIDDEN: en caso de que el usuario no tenga permisos para realizar esa accion
        USUARIO_YA_EXISTE: en caso de que ya exista un usuario con ese nombre en la base de datos
        ERROR_MODIFICAR_USUARIO: en caso de que ocurra algun error al modificar el usuario
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if type(consultasUsuario.obtener_usuario_por_nombre(usuario.nombre)) == User:
        raise exceptions.USUARIO_YA_EXISTE
    if consultasUsuario.modificar_usuario(usuario):
        return {
            "detail" : "usuario modificado correctamente"
        }
    else:
        raise exceptions.ERROR_MODIFICAR_USUARIO

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT,
            response_description="Respuesta existosa",
            summary="elimina un usuario de la base de datos")
async def eliminar_usuario(id: int, user: User = Depends(current_user)):
    """
    Este metodo permite eliminar un usuario de la base de datos
    Param:
        cuestionario: es el usuario que se va a insertar en la base de datos
    Return:
        un dict indicado que se a modificado el usuario correctamente
    Raise:
        FORBIDDEN: en caso de que el usuario no tenga permisos para realizar esa accion
        ERROR_ELIMINAR_USUARIO: en caso de que ocurra algun error al eliminar el usuario
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if consultasUsuario.eliminar_usuario(id):
        return {
            "detail" : "usuario eliminado correctamente"
        }
    else:
        raise exceptions.ERROR_ELIMINAR_USUARIO