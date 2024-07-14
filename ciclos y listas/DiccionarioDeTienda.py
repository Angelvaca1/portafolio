# Creamos un Diccionario llamado PriceList para Almacenar los precios de los productos.
PriceList = {}

# Agregamos los Precios de los Productos al Diccionario PriceList.
PriceList["Chile"] = "$5"
PriceList["Sopa"] = "$4"
PriceList["Ensalada"] = "$4.50"
PriceList["Jugo"] = "$1"
PriceList["Perro caliente"] = "$2"
PriceList["Helado"] = "#1.50/bola"

# Solicitamos al Usuario que Ingrese el Producto que Desea.
user = input("Pide lo que necesites: ")

# Buscamos el Precio del Producto Ingresado por el Usuario en el Diccionario PriceList.
precio = PriceList.get(user)

# Imprimimos el Precio del Producto.
print(precio)
