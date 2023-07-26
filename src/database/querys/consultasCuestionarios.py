from database.querys.conexionBD import ConexionDB
from database.models.cuestionario import Cuestionario

def obtener_cuestionarios() -> list[Cuestionario]:
    """
    Este metodo permite obtener todos los cuestionarios de la base de datos
    Return:
        una lista con todos los cuestionarios de la base de datos
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM cuestionarios"
        cursor.execute(consulta)
        lista_cuestionarios = []
        cuestionarios = cursor.fetchall()
        for cuestionario in cuestionarios:
            lista_cuestionarios.append(Cuestionario(
                id=cuestionario[0],
                nombre=cuestionario[1],
                descripcion=cuestionario[2],
                id_categoria=cuestionario[3]
            ))
        return lista_cuestionarios
    finally:
        if conexion is not None:
            conexion.desconectar()

def obtener_cuestionario(id: int) -> Cuestionario | None:
    """
    Este metodo permite obtener un cuestionario de la base de datos
    a partir de su id
    Param:
        id: es el id del cuestionario que queremos obtener
    Return:
        El cuestionario con el id indicado si existe, None si no existe 
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM cuestionarios where id = %s"
        cursor.execute(consulta,(id,))
        cuestionario = cursor.fetchone()
        if cuestionario:
            return Cuestionario(
                id=cuestionario[0],
                nombre=cuestionario[1],
                descripcion=cuestionario[2],
                id_categoria=cuestionario[3]
            )
        else:
            return None
    finally:
        if conexion is not None:
            conexion.desconectar()

def obtener_cuestionario_por_nombre(nombre: str) -> Cuestionario | None:
    """
    Este metodo permite obtener un cuestionario de la base de datos
    a partir de su id
    Param:
        nombre: es el nombre del cuestionario que queremos obtener
    Return:
        El cuestionario con el nombre indicado si existe, None si no existe 
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM cuestionarios where nombre like %s"
        cursor.execute(consulta,(nombre,))
        cuestionario = cursor.fetchone()
        if cuestionario:
            return Cuestionario(
                id=cuestionario[0],
                nombre=cuestionario[1],
                descripcion=cuestionario[2],
                id_categoria=cuestionario[3]
            )
        else:
            return None
    finally:
        if conexion is not None:
            conexion.desconectar()

def obtener_cuestionarios_por_categoria(categoria: str) -> list[Cuestionario]:
    """
    Este metodo permite obtener todos los cuestionarios de una categoria 
    de la base de datos
    Param:
        categoria: es el nombre de la categoria de la que queremos obtener
        los cuestionarios
    Return:
        una lista con todos los cuestionarios de la
        categoria indicada de la base de datos
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT c.* FROM cuestionarios c inner join categoria ca on c.id_categoria = ca.id where ca.nombre like %s"
        cursor.execute(consulta,(categoria,))
        lista_cuestionarios = []
        cuestionarios = cursor.fetchall()
        for cuestionario in cuestionarios:
            lista_cuestionarios.append(Cuestionario(
                id=cuestionario[0],
                nombre=cuestionario[1],
                descripcion=cuestionario[2],
                id_categoria=cuestionario[3]
            ))
        return lista_cuestionarios
    finally:
        if conexion is not None:
            conexion.desconectar()

def insertar_cuestionario(cuestionario: Cuestionario) -> bool:
    """
    Este metodo permite insertar un cuestionario en la base de datos
    Param:
        cuestionario: es el cuestionario que se va a insertar en la base de datos
    Return:
        true si se inserta el cuestionario, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "INSERT INTO cuestionarios(nombre, descripcion,id_categoria) VALUES (%s,%s,%s)"
        cursor.execute(consulta, (cuestionario.nombre,cuestionario.descripcion,cuestionario.id_categoria))
        filas = cursor.rowcount
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()

def modificar_cuestionario(cuestionario: Cuestionario) -> bool:
    """
    Este metodo permite modificar un cuestionario de la base de datos
    Param:
        cuestionario: es el cuestionario que se va a modificar
    Return:
        true si se modifica el cuestionario, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "UPDATE cuestionarios SET nombre=%s,descripcion=%s,id_categoria=%s WHERE id = %s"
        cursor.execute(consulta, (cuestionario.nombre,cuestionario.descripcion,cuestionario.id_categoria,cuestionario.id))
        filas = cursor.rowcount
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()

def eliminar_cuestionario(id: int) -> bool:
    """
    Este metodo permite eliminar un cuestionario de la base de datos
    Param:
        id: es el id del cuestionario que se va a eliminar
    Return:
        true si se modifica el cuestionario, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "delete from cuestionarios where id = %s"
        cursor.execute(consulta, (id,))
        filas = cursor.rowcount
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()