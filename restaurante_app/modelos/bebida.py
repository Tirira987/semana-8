from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str) -> None:
        # Inicializa los atributos de la clase base
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano: str = tamano

    def mostrar_informacion(self) -> str:
        # Extiende el comportamiento sin romper la sustitución de Liskov
        return f"[{self.categoria}] Cód: {self.codigo} - {self.nombre} ({self.tamano}) | Precio: ${self.precio:.2f}"