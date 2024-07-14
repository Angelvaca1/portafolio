try:
    # Código que puede causar una excepción
    num = int(input("Introduce un numero: "))
    resultado = 10 * num
except ValueError:
    # Se ejecuta si ocurre una excepción de tipo ValueError
    print("El valor introducido no es un número válido")
except ZeroDivisionError:
    # Se ejecuta si ocurre una excepción de tipo ZeroDivisionError
    print("No se puede dividir por cero")
else:
    # Se ejecuta si no ocurre ninguna excepción
    print(f"El resultado es {resultado}")
finally:
    # Se ejecuta siempre, ocurra o no una excepción
    print("Fin del bloque try-except")
