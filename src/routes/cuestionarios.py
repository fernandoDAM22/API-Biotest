from fastapi import APIRouter,status
from routes.jwt_auth_users import current_user
from fastapi import Depends
from database.models.cuestionario import Cuestionario
from tools import exceptions
from database.querys import consultasCuestionarios
from database.models.usuario import User

router = APIRouter(prefix="/cuestionarios",responses={
    404:{
        "message" : "no encontrado"
    }
},tags=["cuestionarios"])

@router.get("/",status_code=status.HTTP_200_OK,response_model=list[Cuestionario],
            response_description="Respuesta existosa",
            summary="Obtener todas los cuestionarios de la base de datos")
async def obtener_cuestionarios(user: User = Depends(current_user)):
    """
    Este metodo permite obtener todas los cuestionarios de la base de datos
    Return:
        una lista con todas los cuestionarios de la base de datos
    """
    return consultasCuestionarios.obtener_cuestionarios()


@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=Cuestionario,
            response_description="Respuesta existosa",
            summary="Obtener un cuestionario de la base de datos a partir de su id")
async def obtener_cuestionario(id: int,user: User = Depends(current_user)):
    """
    Este metodo permite obtener un cuestionario de la base de datos
    a partir de su id
    Param:
        id: es el id del cuestionario que queremos obtener
    Return:
        El cuestionario con el id indicado
    """
    cuestionario = consultasCuestionarios.obtener_cuestionario(id)
    if cuestionario is None:
        raise exceptions.CUESTIONARIO_NO_EXISTE
    else:
        return cuestionario

@router.get("/nombre/{name}",status_code=status.HTTP_200_OK,response_model=Cuestionario,
            response_description="Respuesta existosa",
            summary="Obtener un cuestionario de la base de datos a partir de su nombre")
async def obtener_cuestionario_por_nombre(name: str,user: User = Depends(current_user)):
    """
    Este metodo permite obtener un cuestionario de la base de datos
    a partir de su nombre
    Param:
        nombre: es el nombre del cuestionario que queremos obtener
    Return:
        El cuestionario con el nombre indicado
    """
    cuestionario = consultasCuestionarios.obtener_cuestionario_por_nombre(name)
    print(cuestionario)
    if cuestionario is None:
        raise exceptions.CUESTIONARIO_NO_EXISTE
    else:
        return cuestionario

@router.get("/categoria/{name}",status_code=status.HTTP_200_OK,response_model=list[Cuestionario],
            response_description="Respuesta existosa",
            summary="Obtener todos los cuestionarios de una categoria de la base de datos")
async def obtener_cuestionario_por_nombre(name: str,user: User = Depends(current_user)):
    """
    Este metodo permite obtener todos los cuestionarios de una categoria
    de la base de datos
    Param:
        name: es el nombre de la categoria de la que queremos obtener los cuestionarios
    Return:
        Una lista con los cuestionarios de la categoria indicada
    """
    cuestionario = consultasCuestionarios.obtener_cuestionarios_por_categoria(name)
    print(cuestionario)
    if cuestionario is None:
        raise exceptions.CUESTIONARIO_NO_EXISTE
    else:
        return cuestionario
    
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=dict,
            response_description="Respuesta existosa",
            summary="Inserta un cuestionario en la base de datos")
async def insertar_cuestionario(cuestionario: Cuestionario,user: User = Depends(current_user)):
    """
    Este metodo permite insertar un cuestionario en la base de datos
    Param:
        cuestionario: es la cuestionario que se va a insertar en la base de datos
    Return:
        un dict indicado que se a insertado el cuestionario correctamente
    Raise:
        FORBIDDEN: en caso de que el usuario no tenga permisos para realizar la accion
        CUESTIONARIO_YA_EXISTE: en caso de que se intente insertar un cuestionario que ya existe
        ERROR_INSERTAR_CUESTIONARIO: en caso de que ocurra algun error al insertar el cuestionario 
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if type(consultasCuestionarios.obtener_cuestionario_por_nombre(cuestionario.nombre)) == Cuestionario:
        raise exceptions.CUESTIONARIO_YA_EXISTE
    if consultasCuestionarios.insertar_cuestionario(cuestionario):
        return {
            "detail" : "Cuestionario insertado correctamente"
        }
    else:
        raise exceptions.ERROR_INSERTAR_CUESTIONARIO

@router.put("/",status_code=status.HTTP_200_OK,response_model=dict,
            response_description="Respuesta existosa",
            summary="modifica un cuestionario en la base de datos")
async def modificar_categoria(cuestionario: Cuestionario,user: User = Depends(current_user)):
    """
    Este metodo permite modificar un cuestionario de la base de datos
    Param:
        cuestionario: es el cuestionario que se va a modificar
    Return:
        un dict indicando que se a modificado el cuestionario correctamente
    Raise
        FORBIDDEN: en caso de que el usuario no tenga permisos para realizar la accion
        CUESTIONARIO_YA_EXISTE: en caso de que ya exista un cuestionario con ese nombre
        ERROR_MODIFICAR_CUESTIONARIO: en caso de que ocurra algun error al modificar el cuestionario
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if type(consultasCuestionarios.obtener_cuestionario_por_nombre(cuestionario.nombre)) == Cuestionario:
        raise exceptions.CUESTIONARIO_YA_EXISTE
    if consultasCuestionarios.modificar_cuestionario(cuestionario):
        return {
            "detail" : "cuestionario modificado correctamente"
        }
    else:
        raise exceptions.ERROR_MODIFICAR_CUESTIONARIO


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT,
            response_description="Respuesta existosa",
            summary="modifica un cuestionario en la base de datos")
async def eliminar_categoria(id: int,user: User = Depends(current_user)):
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if not consultasCuestionarios.eliminar_cuestionario(id):
        raise exceptions.ERROR_BORRAR_CUESTIONARIO