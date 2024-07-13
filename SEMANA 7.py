class FileHandler:
    """
    Clase FileHandler para manejar la apertura y cierre de archivos.
    El constructor abre el archivo y el destructor cierra el archivo.
    """

    def __init__(self, file_name, mode):
        """
        Constructor que inicializa el objeto FileHandler.

        :param file_name: Nombre del archivo.
        :param mode: Modo de apertura del archivo (e.g., 'r', 'w', 'a').
        """
        self.file_name = file_name
        self.mode = mode
        self.file = None
        try:
            self.file = open(file_name, mode)
            print(f"Archivo '{file_name}' abierto en modo '{mode}'.")
        except IOError as e:
            print(f"Error al abrir el archivo '{file_name}': {e}")

    def write_data(self, data):
        """
        Método para escribir datos en el archivo.

        :param data: Datos a escribir en el archivo.
        """
        if self.file and not self.file.closed:
            self.file.write(data)
            print(f"Datos escritos en el archivo '{self.file_name}'.")
        else:
            print(f"No se puede escribir en el archivo '{self.file_name}' porque no está abierto.")

    def __del__(self):
        """
        Destructor que cierra el archivo si está abierto.
        """
        if self.file and not self.file.closed:
            self.file.close()
            print(f"Archivo '{self.file_name}' cerrado.")
        else:
            print(f"El archivo '{self.file_name}' ya estaba cerrado o no se abrió correctamente.")


# Uso de la clase FileHandler
def main():
    # Crear un objeto FileHandler y escribir datos en el archivo
    file_handler = FileHandler('example.txt', 'w')
    file_handler.write_data('Hola, este es un ejemplo de uso de constructores y destructores en Python.\n')

    # La instancia file_handler se elimina al final del alcance de la función, invocando el destructor
    # Si deseas eliminar el objeto antes explícitamente, puedes usar del file_handler


if __name__ == "__main__":
    main()
    # En este punto, si el archivo no fue cerrado explícitamente, el destructor __del__ se encargará de cerrarlo.
º13
