class TiendaVirtual:
    def __init__(self):
        self.cuenta = 0

    def procesar_pago(self, precio_producto, dinero_recibido):
        if dinero_recibido < precio_producto:
            return "Dinero insuficiente. Por favor, proporcione más dinero."
        else:
            cambio = dinero_recibido - precio_producto
            self.cuenta += precio_producto
            return f"Cambio: ${cambio:.2f}. Gracias por su compra."

tienda = TiendaVirtual()
precio = 30.00
dinero_recibido = 100.00

mensaje = tienda.procesar_pago(precio, dinero_recibido)
print(mensaje)
print(f"Dinero en la cuenta de la tienda: ${tienda.cuenta:.2f}")