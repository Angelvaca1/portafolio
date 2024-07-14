#creamos la variable "Number_one" y luego le preguntamos al usuario sobre el numero que desea conocer
number_one = input("Ingresa un número: ")
#clasificamos que la variable soltara resultados "int" a lo cual se refiere como enteros
number_one = int(number_one)
#mandamos al programa a imprimir "number one" Solo, Más uno y Menos uno. Este numero puede ser cambiado por el numero que deseamos conocer
print("Tu número = " + str(number_one))
print("El número anterior = " + str(number_one - 1))
print("El número siguiente = " + str(number_one + 1))