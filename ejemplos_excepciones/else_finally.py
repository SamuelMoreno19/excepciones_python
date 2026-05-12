# --- BLOQUE 1: MANEJO DE ARCHIVOS ---
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")
    archivo = open("datos.txt", "w")
    archivo.write("Archivo creado automáticamente")
    contenido = "Archivo creado automáticamente" # Definimos contenido para que el else no falle
else:
    print(f"Contenido leído: {contenido}")
finally:
    print("Operación de archivo completada.")
    archivo.close()

# --- BLOQUE 2: FUNCIÓN DE ORDEN ---
def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
        # x = 1 / 0  # Descomenta para probar el error
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else")
    finally:
        print("4. Ejecutando bloque finally")

    print("5. Continuando después del bloque try")

# Llamada a la función (sin espacios al inicio)
demostrar_orden()

def dividir(a, b):
    try:
        resultado = a / b
        return resultado  # Este return no se ejecuta inmediatamente
    except ZeroDivisionError:
        print("Error: División por cero")
        return None  # Este return tampoco se ejecuta inmediatamente
    finally:
        print("División finalizada")  # Esto se ejecuta antes de cualquier return
        # Ahora sí se devuelve el valor correspondiente

print(dividir(10, 2))  # Imprime "División finalizada" y luego 5.0
print(dividir(10, 0))  # Imprime "Error: División por cero", "División finalizada" y luego None

try:
    1 / 0  # Genera ZeroDivisionError
except ZeroDivisionError:
    print("Capturada división por cero")
    # La excepción ha sido manejada
finally:
    # Si descomentas la siguiente línea, el ZeroDivisionError original se perderá
    # y será reemplazado por este ValueError
    # int("abc")  # Genera ValueError
    print("Bloque finally ejecutado")