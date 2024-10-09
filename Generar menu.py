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







