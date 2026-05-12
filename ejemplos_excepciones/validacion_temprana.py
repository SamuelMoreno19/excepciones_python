def procesar_datos(datos):
    # Validación al inicio
    if datos is None:
        raise ValueError("Los datos no pueden ser None")
    if not isinstance(datos, list):
        raise TypeError("Los datos deben ser una lista")
    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacía")

    # Procesamiento principal
    resultado = []
    for item in datos:
        # Agregamos una lógica simple para que no esté vacío
        resultado.append(f"Procesado: {item}")
    
    return resultado

# Para que veas el resultado en la terminal, hay que "atrapar" los raise con un try-except
try:
    # Prueba cambiar esto por None, por [] o por una lista con números [1, 2, 3]
    mi_lista = [10, 20, 30] 
    print(f"Enviando datos: {mi_lista}")
    
    salida = procesar_datos(mi_lista)
    print(f"Resultado final: {salida}")

except (ValueError, TypeError) as e:
    print(f"Se detuvo el proceso: {e}")