class Cliente:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Cliente: {self.nombre} | Email: {self.correo}"