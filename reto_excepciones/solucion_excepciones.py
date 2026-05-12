def dividir_numeros():
    try:
        # Solicitar datos
        n1 = input("Introduce el primer número: ")

        print("--------------------------------")

        n2 = input("Introduce el segundo número: ")

        # Conversión y operación
        num1 = int(n1)
        num2 = int(n2)
        resultado = num1 / num2
        
        # Mostramos el resultado AQUÍ para que salga antes que el finally
        print(f"El resultado es: {resultado}")

    except ValueError:
        print("Error: Debes introducir un número válido")
    
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
        
    
    finally:
        # Esto siempre será lo último en imprimirse dentro de la función
        print("Operación finalizada")

# Ejecución
dividir_numeros()