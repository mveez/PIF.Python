#Importar la base de datos
import sqlite3

#Crear conexiones
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

#Se crea la tabla
cursor.execute (
    """CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        categoria TEXT NOT NULL, 
        precio TEXT NOT NULL) """
)

conn.commit()

#Funcion para saber si existe por ID 
def elemento_existe (id_elemento):
    cursor.execute ("SELECT * FROM stock WHERE id = ?", (id_elemento,))
    return cursor.fetchone () is not None

#Funcion para agregar nuevo elemento 
def agregar_elemento ():
    nombre = input ("Ingresar nombre de libro: ").title()
    descripcion = input ("Ingresar descripcion del libro: ")
    categoria = input ("Ingresar categoria del libro: ").title()
    precio = float (input ("Ingresar precio del libro: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))

    cursor.execute (
        """INSERT INTO stock (nombre, descripcion, categoria, precio, cantidad) 
        VALUES (?,?,?,?,?)""", 
            (nombre, descripcion, categoria, precio, cantidad)
    )

    conn.commit ()
    print("Libro agregado de manera exitosa")

#Mostrar una tabla de los libros 
def mostrar_elemento():
    cursor.execute("SELECT * FROM stock")
    elementos = cursor.fetchall()
    if elementos:
        for elemento in elementos:
            print(elemento)
    else:
        print("No hay libros en el inventario")

#Actualizar cantidad de productos 
def actualizar_elemento():
    id_elemento = int (input ("Ingres el id del producto a actualizar: "))
    #Verificar si existe 
    if elemento_existe (id_elemento): 
        nueva_cantidad = int(input("Ingresar nueva cantidad: "))
        cursor.execute (
            "UPDATE stock SET cantidad = ? WHERE id = ?",
            (nueva_cantidad, id_elemento),
        )
        conn.commit()
        print("Cantidad actualizada exitosamente.")
    else:
        print(f"El libro con ID {id_elemento} no existe.")

#Eliminar elemento
def eliminar_elemento ():
    id_elemento = int(input("Ingrese el ID del libro a eliminar: "))

    # Verificar si el elemento existe utilizando la función elemento_existe
    if elemento_existe(id_elemento):
        cursor.execute("DELETE FROM stock WHERE id = ?", (id_elemento,))
        conn.commit()
        print("Libro eliminada exitosamente.")
    else:
        print(f"El libro con ID {id_elemento} no existe en la base de datos")

#Buscar elemento 
def buscar_elemento():
    id_elemento = int(input("Ingrese el ID del libro: "))

    # Verificar si el elemento existe utilizando la función elemento_existe
    if elemento_existe(id_elemento):
        cursor.execute("SELECT * FROM stock WHERE id = ?", (id_elemento,))
        elemento = cursor.fetchone()
        print(elemento)

    else:
        print(f"El libro con ID {id_elemento} no existe en la base de datos")

#Generar reporte de bajo stock
def reportes_bajo_stock():

    limite = int(input("Ingrese el límite para considerar bajo stock: "))
    cursor.execute("SELECT * FROM stock WHERE cantidad <= ?", (limite,))

    #obtenemos la lista de tuplas de la consulta SQL mediante el execute()
    elementos = cursor.fetchall()
    if elementos:
        for elemento in elementos:
            print(elemento)
    else:
        print("No hay libros con bajo stock.")

#------------------------------------------------------------------------------------------

#generar menu
def mostrar_menu (opciones):
    print('Seleccione una opcion: ');
    for clave in sorted (opciones):
        print (f'{clave}) {opciones[clave][0]}');

def leer_opcion (opciones):
    while (a := input ('Opcion: ')) not in opciones:
        print ('Opcion incorrecta, vuelva a intentarlo ')
    return a 

def ejecutar_opcion(opcion,opciones):
    opciones[opcion][1]();        

def generar_menu (opciones, opcion_salida): 
    opcion = None;
    while opcion != opcion_salida:
        mostrar_menu (opciones);
        opcion = leer_opcion (opciones);
        ejecutar_opcion (opcion, opciones);
        print() # imprime linea en blanco para clarificar la salida por pantalla

def menu_principal ():
    opciones = {
        '1': ('Agregar Producto', accion1),
        '2': ('Mostrar Producto', accion2),
        '3': ('Actualizar Cantidad de Producto', accion3),
        '4': ('Eliminar Producto', accion4),
        '5': ('Buscar Producto', accion5),
        '6': ('Reporte de Bajo Stock', accion6),
        '7': ('Salir', salir)
    };

    generar_menu (opciones, '7');

def accion1():
    print('Has elegido la opción 1');

def accion2():
    print('Has elegido la opción 2');

def accion3():
    print('Has elegido la opción 3');

def accion4():
    print('Has elegido la opción 4');

def accion5():
    print('Has elegido la opción 5');

def accion6():
    print('Has elegido la opción 6');

def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal();

menu_principal()
conn.close()







