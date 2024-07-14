# Solicita al Usuario que Ingrese un digito
num1 = int(input("Ingresa un número: "))
# Inicializa una variable num2 en 0
num2 = 0
# Comienza un Ciclo While que se Ejecutará Mientras num2 sea Menor que 10
while num2 < 10:
    # En cada iteración, incrementa num2 en 1
    num2 = num2 + 1
    
    # Imprime el resultado de elevar num1 a la potencia num2
    print("Tu número " + str(num1) + " elevado a la " + str(num2) + " = " + str(num1 ** num2))

# Una vez que num2 alcanza 10, el bucle while termina
# Imprime "¡Cálculos completados!" para indicar que todos los cálculos han sido realizados
print("¡Cálculos completados!")
