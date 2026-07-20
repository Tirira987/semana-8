from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def ejecutar_menu() -> None:
    servicio: Restaurante = Restaurante()

    while True:
        print("\n" + "="*40)
        print("        SISTEMA DE RESTAURANTE")
        print("="*40)
        print("1. Registrar producto")
        print("2. Registrar bebida")
        print("3. Registrar cliente")
        print("-"*40)
        print("4. Listar productos")
        print("5. Listar clientes")
        print("-"*40)
        print("6. Salir")
        
        opcion: str = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            codigo: str = input("Código: ").strip()
            nombre: str = input("Nombre: ").strip()
            categoria: str = input("Categoría (ej. Entradas, Platos Fuertes): ").strip()
            try:
                precio: float = float(input("Precio: "))
                nuevo_producto = Producto(codigo, nombre, categoria, precio)
                if servicio.registrar_producto(nuevo_producto):
                    print("¡Producto registrado con éxito!")
                else:
                    print("Error: El código de producto ya existe.")
            except ValueError:
                print("Error: El precio debe ser un valor numérico.")

        elif opcion == "2":
            print("\n--- Registrar Bebida ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría (ej. Bebidas Calientes, Jugos): ").strip()
            try:
                precio = float(input("Precio: "))
                tamano: str = input("Tamaño/Presentación (ej. 500ml, Personal): ").strip()
                # Bebida es instanciada y será tratada como un Producto en el servicio
                nueva_bebida = Bebida(codigo, nombre, categoria, precio, tamano)
                if servicio.registrar_producto(nueva_bebida):
                    print("¡Bebida registrada con éxito!")
                else:
                    print("Error: El código de producto/bebida ya existe.")
            except ValueError:
                print("Error: El precio debe ser un valor numérico.")

        elif opcion == "3":
            print("\n--- Registrar Cliente ---")
            identificacion: str = input("Identificación/Cédula: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo: str = input("Correo electrónico: ").strip()
            
            nuevo_cliente = Cliente(identificacion, nombre, correo)
            if servicio.registrar_cliente(nuevo_cliente):
                print("¡Cliente registrado con éxito!")
            else:
                print("Error: La identificación del cliente ya existe.")

        elif opcion == "4":
            print("\n--- Lista de Productos ---")
            productos = servicio.obtener_productos()
            if not productos:
                print("No hay productos registrados en el sistema.")
            else:
                # Aquí se evidencia el polimorfismo puro sin verificar isinstance()
                for prod in productos:
                    print(prod.mostrar_informacion())

        elif opcion == "5":
            print("\n--- Lista de Clientes ---")
            clientes = servicio.obtener_clientes()
            if not clientes:
                print("No hay clientes registrados en el sistema.")
            else:
                for cli in clientes:
                    print(cli.mostrar_informacion())

        elif opcion == "6":
            print("\nGracias por utilizar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()