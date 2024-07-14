# Definimos la Variable 'q' que Tiene el Mensaje para Solicitar al Usuario el Número de Estudiantes
q = "Ingresa el número de estudiantes de la clase "
# Inicializamos el Contador Para llevar el Seguimiento del Número de Clases Ingresadas
contador = 0
# Definimos el Número Total de Clases
clases = 10
# Inicializamos la Variable que Almacenará la Suma Total de Alumnos
suma_total_alumnos = 0

# Mientras el contador sea Menor que el número total de clases, se Ejecutará el bucle
while contador < clases:
    # Solicitamos al Usuario que Ingrese el Número de Estudiantes Para Cada Clase y lo Sumamos a 'suma_total_alumnos'
    suma_total_alumnos += int(input(q + str(contador+1)))
    # Incrementamos el Contador en 1 Para Pasar a la Siguiente Clase
    contador += 1

# Una Vez Que se Han Ingresado Todos los Datos, Imprimimos la Suma Total de Alumnos
print(suma_total_alumnos)
