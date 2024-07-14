def crear_diccionario_personas(num_personas):
    # Inicializar un Diccionario Vacío para Almacenar las Personas y sus Tallas
    diccionario_personas = {}
    
    # Ciclamos según el número de personas proporcionado
    for _ in range(num_personas):
        # Solicitar al Usuario el Nombre de la Persona
        nombre = input("Ingrese el Nombre de la Persona: ")
        # Solicitar al Usuario la Talla de la Persona
        talla = input(f"Ingrese la talla para {nombre} (XS, S, M, L, XL, XXL o XXXL): ")
        # Agregar el Nombre y la Talla al Diccionario de Personas
        diccionario_personas[nombre] = talla
    
    # Devolver el Diccionario de Personas Creado
    return diccionario_personas

def obtener_talla(diccionario, persona):
    # Verificar si la Persona Está en el Diccionario
    if persona in diccionario:
        # Devolver la talla de la Persona si se Encuentra en el Diccionario
        return diccionario[persona]
    else:
        # Devolver un mensaje de Error si la Persona no Está en el Diccionario
        return "No se encontró la Persona."

# Solicitar al Usuario el Número de Personas que Desea Ingresar
num_personas = int(input("Ingrese el Número de Personas en la Lista: "))

# Crear el Diccionario de Personas Utilizando la Función crear_diccionario_personas
diccionario_personas = crear_diccionario_personas(num_personas)

# Solicitar al Usuario el Nombre de la Persona de la Cual Desea Conocer la Talla
nombre_buscar = input("Ingrese el nombre de la persona cuya talla desea conocer: ")

# Obtener la Talla de la Persona Utilizando la Función Obtener_Talla
talla_persona = obtener_talla(diccionario_personas, nombre_buscar)

# Imprimir la Talla de la Persona o un Mensaje de Error si la Persona no Está en el Diccionario
print(f"Talla de {nombre_buscar}: {talla_persona}")
