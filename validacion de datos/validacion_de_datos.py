try:
    # Código que puede causar una excepción
    num = int(input("Introduce un numero: "))
    resultado = 10 / num
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
    print("Fin del calculo")
#########################################################################################################################

class NegativeNumberError(Exception):
    "Excepción personalizada para manejar números negativos.8"
    pass

def calcular_division():
    while True:
        try:
            num = input("Introduce un número: ").strip()
            if not num.isdigit() and not (num.startswith("-") and num[1:].isdigit()):
                raise ValueError("No se introdujo un número válido.")
            
            num = int(num)
            if num < 0:
                raise NegativeNumberError("El número no puede ser negativo.")
            
            resultado = 10 / num
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
        except NegativeNumberError as ne:
            print(f"Error: {ne}")
        else:
            print(f"El resultado es {resultado:.2f}")
            break  # Salir del bucle si todo va bien
        finally:
            print("Intento completado.")
    
    print("Fin del cálculo.")

# Llamar a la función
calcular_division()
#################################################################################################
