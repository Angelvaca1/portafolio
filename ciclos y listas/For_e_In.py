# Solicitamos al Usuario que Ingrese la Cadena de PIalabras Searadas por Espacios
user = input("Ingrese la cadena de palabras separadas por espacios: ")

# Definimos una Función llamada 'calcular_codigo_encriptado' que Toma un Texto Como Entrada
def calcular_codigo_encriptado(texto):
    # Dividimos el Texto en Palabras Usando el Método split(), Separando por Espacios
    palabras = texto.split()
    # Inicializamos una variable para Almacenar el Código Encriptado
    codigo_encriptado = ""
    # Ciclamos sobre Cada Palabra en la Lista de Palabras
    for palabra in palabras:
        # Para Cada Palabra, Calculamos su Longitud y la Agregamos al Código Encriptado Como una Cadena
        codigo_encriptado += str(len(palabra))
    # Retornamos el Código Encriptado
    return codigo_encriptado

# Llamamos a la Función 'calcular_codigo_encriptado' con la Cadena Ingresada por el Usuario y Almacenamos el Resultado
codigo_encriptado = calcular_codigo_encriptado(user)
# Imprimimos el Código Encriptado
print("El código encriptado es:", codigo_encriptado)
