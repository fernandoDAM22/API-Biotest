from fastapi import APIRouter,status
from routes.jwt_auth_users import current_user
from fastapi import Depends
from database.models.categoria import Categoria
from tools import exceptions
from database.querys import consultasCategorias
from database.models.categoria import Categoria
from database.models.usuario import User

router = APIRouter(prefix="/categorias",responses={
    404:{
        "message" : "no encontrado"
    }
},tags=["categorias"])


@router.get("/",status_code=status.HTTP_200_OK,response_model=list[Categoria],
            response_description="Respuesta existosa",
            summary="Obtener todas las categorias de la base de datos")
async def obtener_categorias(user: User = Depends(current_user)):
    """
    Este metodo permite obtener todas las categorias de la base de datos
    Return:
        una lista con todas las categoria de la base de datos
    """
    return consultasCategorias.obtener_categorias()

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=Categoria,
            response_description="Respuesta existosa",
            summary="Obtener una categoria de la base de datos a partir de su id")
async def obtener_categoria(id: int,user: User = Depends(current_user)):
    """
    Este metodo permite obtener una categoria de la base de datos
    a partir de su id
    Param:
        es el id de la categoria que queremos obtener
    Return:
        La categoria con el id indicado
    """
    categoria = consultasCategorias.obtener_categoria(id)
    if categoria is None:
        raise exceptions.CATEGORIA_NO_EXISTE
    else:
        return categoria

@router.get("/nombre/{nombre}",status_code=status.HTTP_200_OK,response_model=Categoria,
            response_description="Respuesta existosa",
            summary="Obtener una categoria de la base de datos a partir de su nombre")
async def obtener_preguntas_por_nombre(nombre: str,user: User = Depends(current_user)):
    """
    Este metodo permite obtener una categoria de la base de datos
    a partir de su id
    Param:
        es el id de la categoria que queremos obtener
    Return:
        La categoria con el id indicado
    """
    categoria = consultasCategorias.obtener_categoria_por_nombre(nombre)
    if categoria is None:
        raise exceptions.CATEGORIA_NO_EXISTE
    else:
        return categoria

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=dict,
            response_description="Respuesta existosa",
            summary="Inserta una categoria en la base de datos")
async def insertar_categoria(categoria: Categoria,user: User = Depends(current_user)):
    """
    Este metodo permite insertar una categoria en la base de datos
    Param:
        categoria: es la categoria que se va a insertar en la base de datos
    Return:
        un dict indicado que se a insertado la categoria correctamente
    Raise:
        FORBIDDEN: en caso de que el usuario no tenga permisos para realizar la accion
        CATEGORIA_YA_EXISTE: en caso de que se intente insertar una categoria que ya existe
        ERROR_INSERTAR_CATEGORIA: en caso de que ocurra algun error al insertar la categoria 
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if type(consultasCategorias.obtener_categoria_por_nombre(categoria.nombre)) == Categoria:
        raise exceptions.CATEGORIA_YA_EXISTE
    if consultasCategorias.insertar_categoria(categoria):
        return {
            "detail" : "Categoria insertada correctamente"
        }
    else:
        raise exceptions.ERROR_INSERTAR_CATEGORIA 

@router.put("/",status_code=status.HTTP_200_OK,response_model=dict,
            response_description="Respuesta existosa",
            summary="modifica una categoria en la base de datos")
async def modificar_categoria(categoria: Categoria,user: User = Depends(current_user)):
    """
    Este metodo permite modificar una categoria de la base de datos
    Param:
        categoria: es la categoria que se va a modificar
    Return:
        un dict indicando que se a modificado la categoria correctamente
    Raise
        FORBIDDEN: en caso de que el usuario no tenga permisos para realizar la accion
        CATEGORIA_YA_EXISTE: en caso de que ya exista una categoria con ese nombre
        ERROR_MODIFICAR_CATEGORIA: en caso de que ocurra algun error al modificar la categoria
    """
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if type(consultasCategorias.obtener_categoria_por_nombre(categoria.nombre)) == Categoria:
        raise exceptions.CATEGORIA_YA_EXISTE
    if consultasCategorias.modificar_categoria(categoria):
        return {
            "detail" : "Categoria modificada correctamente"
        }
    else:
        raise exceptions.ERROR_MODIFICAR_CATEGORIA

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT,
            response_description="Respuesta existosa",
            summary="modifica una categoria en la base de datos")
async def eliminar_categoria(id: int,user: User = Depends(current_user)):
    if user.tipo != "admin":
        raise exceptions.FORBIDDEN
    if not consultasCategorias.eliminar_categoria(id):
        raise exceptions.ERROR_BORRAR_CATEGORIA