# Usamos una Función llamada 'generar_numeros_limite' que Toma un Parámetro 'limite'
def generar_numeros_limite(limite):
    #  sobre los números en el rango de 1 hasta el límite proporcionado por el usuario
    for i in range(1, limite):
        # Comprobamos si el número actual es divisible por 12
        if i % 12 == 0:
            #Ciclamos Si el número es Divisible por 12, Imprimimos un Mensaje Indicando que es una Docena del panadero
            print("¡Docena del panadero!")
        else:
            # Si el Número no es Divisible por 12, Simplemente lo Imprimimos
            print(i)

# Solicitamos al Usuario que Ingrese un Número límite
limite_usuario = int(input("Ingrese un Número límite: "))

# Llamamos a la Función 'generar_numeros_limite' con el Límite Proporcionado por el Usuario
generar_numeros_limite(limite_usuario)
