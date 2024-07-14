# Hacemos la Pregunta Sobre el Nombre de Hulk.
q = "¿Cuál es el nombre de Hulk en los cómics de Marvel?"

# Definimos la Respuesta Correcta.
r_answer = "Bruce Banner"

# Solicitamos al Usuario que Ingrese su Respuesta.
answer = input(q)

# Mientras que la Respuesta del Usuario no Coincida con la Respuesta correcta, se Seguirá Solicitando la Respuesta.
while r_answer != answer:
    # Si la Respuesta no es Correcta, se le Indica al Usuario que lo Intente de Nuevo.
    print("¡Inténtalo nuevamente!")
    # Se solicita Nuevamente al Usuario que Ingrese su Respuesta.
    answer = input(q)

# Cuando la Respuesta del Usuario Coincide con la Respuesta Correcta, se Imprime un Mensaje.
print("¡Sí, correcto!")
