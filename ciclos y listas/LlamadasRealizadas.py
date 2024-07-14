# Conjunto de Números que ya Han Sido llamados
numeros_ya_llamados = {1, 2, 12, 4}

# Se Solicita al Usuario que Ingrese un Número Para llamar
numero_llamado = int(input("¿A qué número hay que llamar?"))

# Se Comprueba si el Número Ingresado por el Usuario está en el Conjunto de Números ya llamados
if numero_llamado in numeros_ya_llamados:
    # Si el Número ya ha Sido llamado, se Imprime un Mensaje Indicando que el Número ya ha sido llamado
    print('¡Este número ya ha sido llamado!')
else:
    # Si el Número no ha Sido llamado Previamente, se Imprime un Mensaje Indicando que se Mostrará en la Pantalla
    print("Número mostrado en la pantalla")