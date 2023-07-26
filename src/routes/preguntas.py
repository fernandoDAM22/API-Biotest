# En este archivo se definen los metodos expuestos por la api
# relacionados con la tabla preguntas

#Imports
from fastapi import APIRouter,status
from routes.jwt_auth_users import current_user
from fastapi import Depends
from database.models.usuario import User
from tools import exceptions
from database.querys import consultasPreguntas
from database.models.pregunta import Pregunta

router = APIRouter(prefix="/preguntas",responses={
    404:{
        "message" : "no encontrado"
    }
},tags=["preguntas"])

@router.get("/",status_code=status.HTTP_200_OK,response_model=list[Pregunta],
            response_description="Respuesta existosa",
            summary="Obtener todas las preguntas de la base de datos")
async def obtener_preguntas(user: User = Depends(current_user)):
    """
    Este metodo permite devolver todas las preguntas de la base de datos en formato JSON
    Return:
        Todas las preguntas de la base de datos en formato JSON
    """
    return consultasPreguntas.obtener_preguntas()

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=Pregunta,
            response_description="Respuesta existosa",
            summary="Obtener una pregunta a partir de su id")
async def obtener_pregunta(id: int,user: User = Depends(current_user)):
    """
    Este metodo permite obtener una pregunta a partir de su id
    Param:
        id: es el id de la pregunta que queremos obtener
    Return:
        La pregunta con el id indicado
    Raise:
        HTTPException, status = 404 en caso de que no exista una pregunta con ese id
    """
    pregunta = consultasPreguntas.obtener_pregunta(id)
    if pregunta is None:
        raise exceptions.PREGUNTA_NO_EXISTE
    else:
        return pregunta
    
@router.get("/enunciado/{enunciado}",status_code=status.HTTP_200_OK,response_model=Pregunta,
            response_description="Respuesta existosa",
            summary="Obtener una pregunta a partir de su enunciado")
async def obtener_pregunta(enunciado: str,user: User = Depends(current_user)):
    """
    Este metodo permite obtener una pregunta a partir de su enunciado
    Param:
        enunciado: es el enunciado de la pregunta que queremos obtener
    Return:
        La pregunta con el enunciado indicado
    Raise:
        HTTPException, status = 404 en caso de que no exista una pregunta con ese enunciado
    """
    pregunta = consultasPreguntas.obtener_pregunta_por_enunciado(enunciado)
    if pregunta is None:
        raise exceptions.PREGUNTA_NO_EXISTE
    else:
        return pregunta
@router.get("/categoria/{name}",status_code=status.HTTP_200_OK,response_model=list[Pregunta],
            response_description="Respuesta existosa",
            summary="Obtener todas las preguntas de una categoria a partir de id")
async def obtener_pregunta(name: str,user: User = Depends(current_user)):
    """
    Este metodo permite obtener toda las preguntas de una categoria
    Param:
        id_categoria: es el id de la categoria de la que queremos obtener las preguntas
    Return:
        Una lista con las preguntas de esa categoria
    Raise:
        HTTPException, status = 404 en caso de que no exista esa categoria
    """
    preguntas = consultasPreguntas.obtener_pregunta_por_categoria(name)
    if len(preguntas) == 0:
        raise exceptions.CATEGORIA_NO_EXISTE
    return preguntas

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=dict,
            response_description="Respuesta existosa",
            summary="Insertar una pregunta en la base de datos")
async def insertar_pregunta(pregunta: Pregunta,user: User = Depends(current_user)):
    """
    Este metodo permite insertar una pregunta en la base de datos
    Param:
        pregunta: es la pregunta que se va a insertar
    Return:
        un dict indicando que se a insertado la pregunta correctamente
    Raise
        FORBIDDEB: en caso de que el usuario no tenga permisos para realizar la accion
        PREGUNTA_YA_EXISTE: en caso de que la pregunta ya exista
        ERROR_INSERTAR_PREGUNTA: en caso de que no se pueda insertar la pregunta
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if type(consultasPreguntas.obtener_pregunta_por_enunciado(pregunta.enunciado)) == Pregunta:
        raise exceptions.PREGUNTA_YA_EXISTE
    if consultasPreguntas.insertar_pregunta(pregunta) == True:
        return {
            "Estado" : "Pregunta insertada correctamente"
        }
    else:
        raise exceptions.ERROR_INSERTAR_PREGUNTA

@router.put("/",status_code=status.HTTP_200_OK,response_model=dict,
            response_description="Respuesta existosa",
            summary="modifica una pregunta de la base de datos")
async def actualizar_pregunta(pregunta: Pregunta,user: User = Depends(current_user)):
    """
    Este metodo permite modificar una pregunta de la base de datos
    Param:
        pregunta: contiene los datos de la pregunta que se va a modificar
    Return:
        un dict indicando que se a modificado la pregunta correctamente
    Raise
        FORBIDDEB: en caso de que el usuario no tenga permisos para realizar la accion
        ERROR_MODIFICAR_PREGUNTA: en caso de que no se pueda modificar la pregunta
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if consultasPreguntas.actualizar_pregunta(pregunta) == True:
        return {
            "Estado" : "Pregunta actualizada correctamente"
        }
    else:
        raise exceptions.ERROR_MODIFICAR_PREGUNTA

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT,
            response_description="Respuesta existosa",
            summary="elimina una pregunta de la base de datos")
async def eliminar_pregunta(id: int,user: User = Depends(current_user)):
    """
    Este metodo permite eliminar una pregunta de la base de datos
    Param:
        id: es el id de la pregunta que queremos eliminar
    Return:
        status code 204 No content
    Raise:
        FORBIDDEB: en caso de que el usuario no tenga permisos para realizar la accion
        ERROR_ELIMINAR_PREGUNTA: en caso de que no se pueda eliminar la pregunta
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if not consultasPreguntas.eliminar_pregunta(id):
        raise exceptions.ERROR_BORRAR_PREGUNTA