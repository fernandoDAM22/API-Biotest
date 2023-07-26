#Esta clase permite conectarnos a la base de datos

import pymysql

class ConexionDB:
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = ''
        self.database = 'preguntas'
        self.connection = None
    
    def conectar(self):
        """
        Este metodo permite conectarnos a la base de datos
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print('Conexión exitosa a la base de datos')
        except pymysql.Error as e:
            print(f'Error al conectar a la base de datos: {e}')
    
    def desconectar(self):
        """
        Este metodo permite desconectarse de la base de datos
        """
        try:
            if self.connection:
                self.connection.close()
                print('Conexión cerrada')
        except pymysql.Error as e:
            print(f'Error al cerrar la conexión: {e}')
    
    def obtener_cursor(self):
        """
        Este metodo permite obtener un cursor para realizar consultas
        Return:
            El cursor en caso de que se cree correctamente
        """
        try:
            if self.connection:
                return self.connection.cursor()
            else:
                print('No hay conexión establecida')
                return None
        except pymysql.Error as e:
            print(f'Error al obtener el cursor: {e}')
            return None

    def confirmar_cambios(self):
        """
        Este metodo permite confirmar los cambios en la base de datos  
        """
        self.connection.commit()
