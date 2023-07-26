from database.querys.conexionBD import ConexionDB
from database.models.categoria import Categoria

def obtener_categorias() -> list[Categoria]:
    """
    Este metodo permite obtener todas las categorias de la base de datos
    Return:
        una lista con todas las categoria de la base de datos
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM categoria"
        cursor.execute(consulta)
        lista_categorias = []
        categorias = cursor.fetchall()
        for categoria in categorias:
            lista_categorias.append(Categoria(
                id=categoria[0],
                nombre=categoria[1],
                descripcion=categoria[2]
            ))
        return lista_categorias
    finally:
        if conexion is not None:
            conexion.desconectar()

def obtener_categoria(id: int) -> Categoria | None:
    """
    Este metodo permite obtener una categoria de la base de datos
    a partir de su id
    Param:
        id: es el id de la categoria que queremos obtener
    Return:
        la categoria con el id indicado si existe, None si no existe 
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM categoria where id = %s"
        cursor.execute(consulta,(id,))
        categoria = cursor.fetchone()
        if categoria:
            return Categoria(
                id=categoria[0],
                nombre=categoria[1],
                descripcion=categoria[2]
            )
        else:
            return None
    finally:
        if conexion is not None:
            conexion.desconectar()

def obtener_categoria_por_nombre(nombre: str) -> Categoria | None:
    """
    Este metodo permite obtener una categoria de la base de datos
    a partir de su nombre
    Param:
        nombre: es el nombre de la categoria que queremos obtener
    Return:
        la categoria con el nombre indicado si existe, None si no existe 
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM categoria where nombre like %s"
        cursor.execute(consulta,(nombre))
        categoria = cursor.fetchone()
        if categoria:
            return Categoria(
                id=categoria[0],
                nombre=categoria[1],
                descripcion=categoria[2]
            )
        else:
            return None
    finally:
        if conexion is not None:
            conexion.desconectar()

def insertar_categoria(categoria: Categoria) -> bool:
    """
    Este metodo permite insertar una categoria en la base de datos
    Param:
        categoria: es la categoria que se va a insertar en la base de datos
    Return:
        true si se inserta la categoria, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "INSERT INTO categoria(id, nombre, descripcion) VALUES (%s,%s,%s)"
        cursor.execute(consulta, (categoria.id,categoria.nombre,categoria.descripcion))
        filas = cursor.rowcount
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()

def modificar_categoria(categoria: Categoria) -> bool:
    """
    Este metodo permite modificar una categoria de la base de datos
    Param:
        categoria: es la categoria que se va a modificar
    Return:
        true si se modifica la categoria, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "UPDATE categoria SET nombre=%s,descripcion=%s WHERE id = %s"
        cursor.execute(consulta, (categoria.nombre,categoria.descripcion,categoria.id))
        filas = cursor.rowcount
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()

def eliminar_categoria(id: int) -> bool:
    """
    Este metodo permite eliminar una categoria de la base de datos
    Param:
        id: es el id de la categoria que se va a eliminar
    Return:
        true si se modifica la categoria, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "delete from categoria where id = %s"
        cursor.execute(consulta, (id,))
        filas = cursor.rowcount
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()