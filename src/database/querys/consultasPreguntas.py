#Imports
from database.querys.conexionBD import ConexionDB
from database.models.pregunta import Pregunta

def obtener_preguntas() -> list[Pregunta]:
    """
    Este metodo permite obtener todas las preguntas de la base de datos
    Return
        Una lista con todas las preguntas de la base de datos
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM preguntas"
        cursor.execute(consulta)
        lista_preguntas = []
        preguntas = cursor.fetchall()
        for pregunta in preguntas:
            lista_preguntas.append(Pregunta(
                id=pregunta[0],
                enunciado=pregunta[1],
                respuesta_correcta=pregunta[2],
                respuesta_incorrecta1=pregunta[3],
                respuesta_incorrecta2=pregunta[4],
                respuesta_incorrecta3=pregunta[5],
                id_categoria=pregunta[6]
            ))
        return lista_preguntas
    finally:
        if conexion is not None:
            conexion.desconectar()


def obtener_pregunta(id: int) -> Pregunta | None:
    """
    Este metodo permite obtener una pregunta de la base de datos a partir de su id
    Params:
        id: es el id de la pregunta que queremos obtener
    Return: la pregunta con el id indicado si existe, None si no existe
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM preguntas WHERE id = %s"
        cursor.execute(consulta, (id,))
        pregunta = cursor.fetchone()

        if pregunta:
            return Pregunta(
                id=pregunta[0],
                enunciado=pregunta[1],
                respuesta_correcta=pregunta[2],
                respuesta_incorrecta1=pregunta[3],
                respuesta_incorrecta2=pregunta[4],
                respuesta_incorrecta3=pregunta[5],
                id_categoria=pregunta[6]
            )
        return None
    finally:
        if conexion is not None:
            conexion.desconectar()


def obtener_pregunta_por_enunciado(enunciado: str):
    """
    Este metodo permite obtener una pregunta de la base de datos a partir de su enunciado
    Params:
        enunciado: es el enunciado de la pregunta que queremos obtener
    Return: la pregunta con el enunciado indicado si existe, None si no existe
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM preguntas WHERE enunciado LIKE %s"
        cursor.execute(consulta, (f'%{enunciado}%',))
        pregunta = cursor.fetchone()

        if pregunta:
            return Pregunta(
                id=pregunta[0],
                enunciado=pregunta[1],
                respuesta_correcta=pregunta[2],
                respuesta_incorrecta1=pregunta[3],
                respuesta_incorrecta2=pregunta[4],
                respuesta_incorrecta3=pregunta[5],
                id_categoria=pregunta[6]
            )
        return None
    finally:
        if conexion is not None:
            conexion.desconectar()

def obtener_pregunta_por_categoria(categoria: str) -> list[Pregunta]:
    """
    Este metodo permite obtener todas las preguntas de 
    una categoria de la base de datos
    Param:
        categoria: es el nombre de la categoria de la queremos obtener las preguntas
    Return
        Una lista con todas las preguntas de la categoria de la base de datos
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()

        consulta = "SELECT * FROM preguntas  p inner join categoria c on p.id_categoria = c.id where c.nombre like %s"
        cursor.execute(consulta,(categoria,))
        lista_preguntas = []
        preguntas = cursor.fetchall()
        for pregunta in preguntas:
            lista_preguntas.append(Pregunta(
                id=pregunta[0],
                enunciado=pregunta[1],
                respuesta_correcta=pregunta[2],
                respuesta_incorrecta1=pregunta[3],
                respuesta_incorrecta2=pregunta[4],
                respuesta_incorrecta3=pregunta[5],
                id_categoria=pregunta[6]
            ))
        print(lista_preguntas)
        return lista_preguntas
    finally:
        if conexion is not None:
            conexion.desconectar()

def insertar_pregunta(pregunta: Pregunta) -> bool:
    """
    Este metodo permite insertar una pregunta en la base de datos
    Param:
        Pregunta: es la pregunta que se va a insertar en la base de datos
    Return:
        true si se inserta la pregunta, false si no se inserta
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "INSERT INTO preguntas(enunciado, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2, respuesta_incorrecta3, id_categoria) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(consulta, (pregunta.enunciado, pregunta.respuesta_correcta, pregunta.respuesta_incorrecta1, pregunta.respuesta_incorrecta2, pregunta.respuesta_incorrecta3, pregunta.id_categoria))
        filas = cursor.rowcount
        print(filas)
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()

def actualizar_pregunta(pregunta: Pregunta) -> bool:
    """
    Este metodo nos permite actualizar una pregunta de la base de datos
    Param:
        pregunta: contiene los datos de la pregunta que se va a modificar
    Return:
        True si la pregunta se modifica, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "UPDATE preguntas set enunciado=%s,respuesta_correcta=%s,respuesta_incorrecta1=%s,respuesta_incorrecta2=%s,respuesta_incorrecta3=%s,id_categoria=%s WHERE id = %s"
        cursor.execute(consulta, (pregunta.enunciado, pregunta.respuesta_correcta, pregunta.respuesta_incorrecta1, pregunta.respuesta_incorrecta2, pregunta.respuesta_incorrecta3, pregunta.id_categoria,pregunta.id))
        filas = cursor.rowcount
        print(filas)
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()

def eliminar_pregunta(id: int) -> bool:
    """
    Este metodo permite borrar una pregunta de la base da datos
    Param:
        id: es el id de la pregunta que queremos eliminar
    Return:
        true si la pregunta se borra, false si no
    """
    conexion = ConexionDB()
    try:
        conexion.conectar()
        cursor = conexion.obtener_cursor()
        consulta = "Delete from preguntas where id = %s"
        cursor.execute(consulta, (id,))
        filas = cursor.rowcount
        print(filas)
        conexion.confirmar_cambios()
        return filas > 0 
    finally:
        if conexion is not None:
            conexion.desconectar()