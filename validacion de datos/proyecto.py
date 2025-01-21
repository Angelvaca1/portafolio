import re
import sqlite3

class DataValidationApp:
    """Una aplicación para validar y almacenar datos en una base de datos."""

    def __init__(self):
        self.db_name = "validacion_datos.db"
        self.create_database()

    def create_database(self):
        """Crea la base de datos y la tabla de usuarios si no existen."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE,
                telefono TEXT NOT NULL UNIQUE
            )
            """
        )
        conn.commit()
        conn.close()

    def validar_nombre(self, nombre):
        """Valida que el nombre solo contenga letras y espacios."""
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre):
            raise ValueError("El nombre solo puede contener letras y espacios.")

    def validar_correo(self, correo):
        """Valida que el correo tenga un formato válido."""
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", correo):
            raise ValueError("El correo electrónico no es válido.")

    def validar_telefono(self, telefono):
        """Valida que el número de teléfono tenga exactamente 10 dígitos."""
        if not re.match(r"^\d{10}$", telefono):
            raise ValueError("El número de teléfono debe contener exactamente 10 dígitos.")

    def guardar_usuario(self, nombre, correo, telefono):
        """Guarda un usuario en la base de datos si los datos son válidos."""
        try:
            self.validar_nombre(nombre)
            self.validar_correo(correo)
            self.validar_telefono(telefono)

            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, telefono) VALUES (?, ?, ?)",
                (nombre, correo, telefono)
            )
            conn.commit()
            conn.close()
            print("Usuario registrado con éxito.")
        except sqlite3.IntegrityError as e:
            print("Error: El correo o el teléfono ya están registrados.")
        except ValueError as e:
            print(f"Error de validación: {e}")

    def mostrar_usuarios(self):
        """Muestra todos los usuarios registrados en la base de datos."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, correo, telefono FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()

        print("\nUsuarios registrados:")
        print("ID | Nombre | Correo | Teléfono")
        print("-" * 40)
        for usuario in usuarios:
            print(f"{usuario[0]} | {usuario[1]} | {usuario[2]} | {usuario[3]}")

if __name__ == "__main__":
    app = DataValidationApp()

    while True:
        print("\nOpciones:")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            nombre = input("Introduce el nombre: ").strip()
            correo = input("Introduce el correo: ").strip()
            telefono = input("Introduce el número de teléfono: ").strip()
            app.guardar_usuario(nombre, correo, telefono)
        elif opcion == "2":
            app.mostrar_usuarios()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
