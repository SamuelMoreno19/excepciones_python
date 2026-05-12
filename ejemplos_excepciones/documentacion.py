def conectar_base_datos(host, puerto, usuario, contraseña):
    """
    Establece conexión con la base de datos.

    Args:
        host (str): Dirección del servidor
        puerto (int): Puerto de conexión
        usuario (str): Nombre de usuario
        contraseña (str): Contraseña de acceso

    Returns:
        Conexión a la base de datos

    Raises:
        ConnectionError: Si no se puede establecer la conexión
        AuthenticationError: Si las credenciales son incorrectas
        TimeoutError: Si la conexión tarda demasiado tiempo
    """
    # Implementación