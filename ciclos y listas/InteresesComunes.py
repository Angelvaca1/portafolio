# Crear Conjuntos Vacíos Para Almacenar los Intereses del Usuario
conjunto1 = set()
conjunto2 = set()

# Solicitar al Usuario la Cantidad de Intereses que Desea Ingresar y Agregarlos al Primer Conjunto
numero_interes = int(input("¿Cuántos intereses deseas ingresar?"))
for i in range(numero_interes):
    interes_usuario = input("Dame tu interés: ")
    conjunto1.add(interes_usuario)

# Solicitar al Usuario la Cantidad de Intereses que Desea Ingresar y Agregarlos al Segundo Conjunto
numero_interes = int(input("¿Cuántos intereses deseas ingresar?"))
for i in range(numero_interes):
    interes_usuario = input("Dame tu interés: ")
    conjunto2.add(interes_usuario)

# Crear un Conjunto Vacío Para Almacenar los Intereses Comunes
conjunto_comun = set()

# Iterar a Través de los Elementos del Primer Conjunto
for elemento_conjunto1 in conjunto1:
    # Verificar si el Elemento del Primer Conjunto Está Presente en el Segundo Conjunto
    if elemento_conjunto1 in conjunto2:
        # Si el Elemento Está Presente en Ambos Conjuntos, Agregarlo al Conjunto Común
        conjunto_comun.add(elemento_conjunto1)

# Verificar si hay Intereses Comunes y Mostrarlos si los hay, de lo Contrario, Imprimir un Mensaje
if conjunto_comun:
    print("Intereses comunes encontrados:", conjunto_comun)
else:
    print("No hay intereses comunes")
