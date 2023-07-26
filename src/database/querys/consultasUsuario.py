#En este archivo se definen las consultas relacionadas con la tabla usuarios

from .conexionBD import ConexionDB
from ..models.usuario import User
from tools.cifrado import cifrar_contrasena

def obtener_usuarios() -> list[User]:
    """
    Este metodo permite obtener todos los usuarios de la base de datos a traves
    de su nombre
    Return:
        Una lista con todos los usuarios de la base de datos
    """
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.obtener_cursor()

    consulta = "SELECT * FROM usuarios"
    cursor.execute(consulta)
    lista_usuarios = []
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        lista_usuarios.append(User(id=usuario[0], 
                    nombre=usuario[1], 
                    contrasena=usuario[2], 
                    email=usuario[3], 
                    telefono=usuario[4], 
                    tipo=usuario[5]))
    return lista_usuarios

def obtener_usuario(id: int) -> User | None:
    """
    Este metodo permite obtener un usuario de la base de datos a traves
    de su id
    Param:
        id: es el id del usuario
    Return:
        el usuario si existe un usuario con ese id en la base de datos,
        None si no existe
    """
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.obtener_cursor()

    consulta = "SELECT * FROM usuarios WHERE id = %s"
    cursor.execute(consulta, (id,))
    
    usuario = cursor.fetchone()
    if usuario:
        user = User(id=usuario[0], 
                    nombre=usuario[1], 
                    contrasena=usuario[2], 
                    email=usuario[3], 
                    telefono=usuario[4], 
                    tipo=usuario[5])
        return user
    else:
        return None
            

def obtener_usuario_por_nombre(name: str) -> User | None:
    """Este metodo permite obtener un usuario de la base de datos a traves
    de su nombre
    Param:
        name: es el nombre del usuario
    Return:
        el usuario si existe un usuario con ese nombre en la base de datos,
        None si no existe
    """
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.obtener_cursor()

    consulta = "SELECT * FROM usuarios WHERE nombre LIKE %s"
    cursor.execute(consulta, (name,))
    
    usuario = cursor.fetchone()
    if usuario:
        user = User(id=usuario[0], 
                    nombre=usuario[1], 
                    contrasena=usuario[2], 
                    email=usuario[3], 
                    telefono=usuario[4], 
                    tipo=usuario[5])
        return user
    else:
        return None
        
def modificar_usuario(usuario: User) -> bool:
    """
    Este metodo permite modificar un usuario en la base de datos
    Param:
        Usuario: es el usuario con los datos a modificar
    Return:
        true si se modifica el usuario, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "UPDATE usuarios SET nombre=%s,contrasena=%s,email=%s,telefono=%s,tipo=%s WHERE id = %s"
        cursor.execute(consulta, (usuario.nombre,cifrar_contrasena(usuario.contrasena),usuario.email,usuario.telefono,usuario.tipo,usuario.id))
        filas = cursor.rowcount
        print(filas)
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()

def eliminar_usuario(id: int) -> bool:
    """
    Este metodo permite eliminar un usuario en la base de datos
    Param:
       id: es el id del usuario que vamos a eliminar
    Return:
        true si se elimina el usuario, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "delete from usuarios where id = %s"
        cursor.execute(consulta, (id,))
        filas = cursor.rowcount
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()