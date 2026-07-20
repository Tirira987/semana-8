# Sistema de Gestión - restaurante_app

**Estudiante:** Richard Arturo Tirira Díaz
**Asignatura:** Programación Orientada a Objetos - Semana 8  
**Institución:** Universidad Estatal Amazónica (UEA)  

## Descripción del Sistema
Este sistema es una aplicación de consola modular desarrollada en Python que permite simular la administración básica de un restaurante (registro y listado de productos gastronómicos, bebidas específicas y clientes). El proyecto ha sido diseñado aplicando los principios SOLID correspondientes a la unidad académica para garantizar la mantenibilidad y extensibilidad del software.

## Estructura del Proyecto
```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

Responsabilidad de cada Clase y Archivo
modelos/__init__.py y servicios/__init__.py: Archivos vacíos obligatorios requeridos para inicializar y reconocer las carpetas como paquetes modulares en Python.

modelos/producto.py (Producto): Clase base del dominio encargada únicamente de representar las propiedades y el comportamiento común de cualquier artículo del restaurante (código, nombre, categoría y precio).

modelos/bebida.py (Bebida): Clase especializada cuya única responsabilidad es modelar las características exclusivas de una bebida (como tamaño, presentación o envase) extendiendo la información general.

modelos/cliente.py (Cliente): Clase independiente asignada exclusivamente a la representación de los datos de identidad y contacto de los clientes registrados (identificación, nombre y correo).

servicios/restaurante.py (Restaurante): Clase de servicio encargada de controlar el estado del negocio. Administra las colecciones en memoria, implementa las reglas de validación de unicidad y expone los métodos de acceso para listar información.

main.py: Punto de arranque y coordinador de la interfaz. Su única responsabilidad es gestionar el flujo del menú, capturar datos del usuario mediante consola empleando input() y redirigir las solicitudes a los métodos correspondientes del servicio.

Relación entre Producto y Bebida
La relación entre Producto (clase base) y Bebida (clase hija) se establece mediante herencia pura ("es un"). Debido a que una bebida es conceptualmente una especialización de un producto del restaurante, hereda todos sus atributos y métodos comunes. Esta vinculación jerárquica permite que los objetos de tipo Bebida sean tratados de manera uniforme, inyectados y administrados dentro de la misma colección genérica de productos del servicio, compartiendo una interfaz común mediante la sobrescritura del método .mostrar_informacion().

Identificación de los Principios SOLID Aplicados
1. Principio de Responsabilidad Única (SRP)
Cada componente del sistema atiende una sola razón de cambio. Las clases del módulo modelos se limitan a estructurar datos; la clase Restaurante en el módulo servicios centraliza la lógica operacional y del negocio; mientras que main.py aísla por completo la lectura y escritura por consola de los datos subyacentes.

2. Principio de Abierto/Cerrado (OCP)
El software demuestra estar abierto a la extensión pero cerrado a la modificación. La adición de la entidad Bebida añade nuevas funcionalidades y campos especializados a la aplicación sin necesidad de alterar una sola línea de código existente dentro de la clase base Producto, ni forzar cambios estructurales en el servicio que procesa los registros generales.

3. Principio de Sustitución de Liskov (LSP)
Las subclases son completamente intercambiables por sus clases base sin alterar el comportamiento correcto del programa. El servicio Restaurante almacena instancias de Producto y Bebida indistintamente en la misma lista. Durante el listado, el programa itera la colección invisibilizando los tipos específicos e invocando .mostrar_informacion() de manera puramente polimórfica, logrando que cada objeto responda según su naturaleza específica sin recurrir a validaciones manuales de tipo (isinstance).

Instrucciones de Ejecución
Verifique tener instalado Python 3.8 o una versión superior en su entorno de ejecución.

Abra una ventana de terminal en el directorio raíz del proyecto (donde se ubica este archivo README.md).

Ejecute el siguiente comando para inicializar el menú de consola:

Bash
python restaurante_app/main.py

Importancia de Diseñar Proyectos Mantenibles (Reflexión Breve)
El diseño de software orientado a la mantenibilidad es la barrera que divide a un prototipo efímero de un sistema empresarial exitoso. Al construir arquitecturas desacopladas bajo estándares SOLID, mitigamos el efecto dominó, donde corregir un error o implementar un cambio en un sector destruye inesperadamente otra funcionalidad. Un proyecto mantenible no solo reduce drásticamente los costos de soporte técnico a largo plazo, sino que permite a los equipos de desarrollo escalar aplicaciones de forma ágil, segura y ordenada ante las dinámicas necesidades del entorno del negocio.
