import hashlib

def cifrar_contrasena(contrasena: str) -> str:
    """
    Este metodo permite cifrar una contrasena en formato sha-256
    Param:
        contasena: es la contrasena que queremos cifrar
    Return:
        la contasena cifrafada
    """
    # Codifica la contraseña en formato UTF-8 antes de cifrarla
    contrasena_codificada = contrasena.encode('utf-8')
    # Crea un objeto hash SHA-256
    sha256_hash = hashlib.sha256()
    # Actualiza el hash con la contraseña codificada
    sha256_hash.update(contrasena_codificada)
    # Obtiene la representación hexadecimal del hash
    contrasena_cifrada = sha256_hash.hexdigest()
    return contrasena_cifrada

