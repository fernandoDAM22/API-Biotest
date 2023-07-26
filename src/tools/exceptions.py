from fastapi import HTTPException, status

#Se lanza cuando el token de autenticacion es invalido
CREDENCIALES_INVALIDAS = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales de autenticación inválidas",
                headers={"WWW-Authenticate": "Bearer"})
#Se lanza cuando las credenciales de autenticacion son invalidas
LOGIN_INCORRECTO = HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Credenciales inválidas")
#Se lanza cuando el usuario intenta realizar una accion para cual no tiene permisos
FORBIDDEN = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="No tienes permiso para realizar esta operacion")
#Se lanza cuando se intenta obtener una pregunta que no existe
PREGUNTA_NO_EXISTE =  HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No existe esa pregunta"
)
#Se lanza cuando se intenta obtener una categoria que no existe
CATEGORIA_NO_EXISTE =  HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No existe esa categoria"
)
#Se lanza cuando se intenta insertar una pregunta con un enunciado que ya existe
PREGUNTA_YA_EXISTE = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Ya existe una pregunta con ese enunciado"
)
#Se lanza cuando ocurre un error al insertar una pregunta
ERROR_INSERTAR_PREGUNTA = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No se ha podido insertar la pregunta"
)
#Se lanza cuando ocurre un error al modificar una pregunta
ERROR_MODIFICAR_PREGUNTA = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No se ha podido modificar la pregunta"
)
#Se lanza cuando ocurre un error al eliminar una pregunta
ERROR_BORRAR_PREGUNTA = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No se ha podido borrar la pregunta"
)
#Se lanza cuando se intenta obtener una categoria que no existe
CATEGORIA_NO_EXISTE = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No existe esa categoria"
)
#Se lanza cuando se intenta insertar una categoria que ya existe
CATEGORIA_YA_EXISTE = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Ya existe esa categoria"
)
#Se lanza cuando ocurre algun error al insertar una categoria
ERROR_INSERTAR_CATEGORIA = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error al insertar la categoria"
)
#Se lanza cuando ocurre un error al modificar una categoria
ERROR_MODIFICAR_CATEGORIA = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No se ha podido modificar la categoria"
)
#Se lanza cuando se intenta borrar una categoria y ocurre algun error
ERROR_BORRAR_CATEGORIA = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No se ha podido eliminar la categoria"
)
#Se lanza cuando se intenta obtener un cuestionario que no existe
CUESTIONARIO_NO_EXISTE = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No existe ese cuestionario"
)
#Se lanza cuando se intenta insertar un cuestionario que ya existe
CUESTIONARIO_YA_EXISTE = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Ya existe ese cuestionario"
)
#Se lanza cuando ocurre algun error al insertar un cuestionario
ERROR_INSERTAR_CUESTIONARIO = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error al insertar el cuestionario"
)
#Se lanza cuando ocurre un error al modificar un cuestionario
ERROR_MODIFICAR_CUESTIONARIO = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No se ha podido modificar el cuestionario"
)
#Se lanza cuando se intenta borrar un cuetionario y ocurre algun error
ERROR_BORRAR_CUESTIONARIO = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No se ha podido eliminar la categoria"
)
#Se lanza cuando se intenta obtener un usuario que no existe
USUARIO_NO_EXISTE = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="No existe ese usuario"
)
#Se lanza cuando se intenta insertar un cuestionario usuario que ya existe
USUARIO_YA_EXISTE = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Ya existe ese usuario"
)
#Se lanza cuando ocurre algun error al insertar un usuario
ERROR_INSERTAR_USUARIO = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error al insertar el usuario"
)
#Se lanza cuando ocurre algun error al modificar un usuario
ERROR_MODIFICAR_USUARIO = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error al modificar un usuario"
)
#Se lanza cuando ocurre algun error al eliminar un usuario
ERROR_ELIMINAR_USUARIO = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error al eliminar un usuario"
)