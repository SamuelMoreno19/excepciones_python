# Demasiado genérico
if not os.path.exists(ruta):
    raise Exception("Problema con el archivo")

# Mejor
if not os.path.exists(ruta):
    raise FileNotFoundError(f"No se encontró el archivo:{ruta}")