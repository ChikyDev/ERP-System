'''SISTEMA ERP ADMINISTRACION'''
# Sistema ERP básico en consola para consultar información de:
# clientes, productos, ventas, proveedores y empleados.
# El sistema funciona mediante un menú interactivo y búsqueda por ID.


# IMPORTACIÓN DE MÓDULOS
# Cada módulo contiene un diccionario con los datos correspondientes
from proveedores import provedores
from clientes import clientes
from productos import productos
from ventas import ventas
from empleados import empleados


# CÓDIGOS DE COLOR ANSI PARA LA CONSOLA
# Se utilizan únicamente para mejorar la visualización del sistema
ROJO = "\033[91m"
AMARILLO = "\033[93m"
VERDE = "\033[92m"
RESET = "\033[0m"
NEGRITA = "\033[1m"
SUBRAYADO = "\033[4m"
CIAN = "\033[36m"

# REFERENCIAS A LOS MÓDULOS (carga de datos)
provedores
clientes
productos
ventas

# CREACIÓN DEL MENÚ VISUAL DEL ERP
tabla = [' CLIENTES ', ' PRODUCTOS ', ' VENTAS ', ' PROVEDORES ', ' EMPLEADOS ']
tablon = '|'.join(tabla)

while True:

     # CABECERA DEL SISTEMA
    print(SUBRAYADO+'                === SISTEMA ERP ===                '+RESET)
    print(CIAN+ f'\n{tablon}'+RESET)

     # OPCIÓN DE SALIDA DEL SISTEMA
    print('\nSalir del sistema ERP, S/N')
    busqueda = input('Que apartado deseas ver: ').lower()

    # VALIDACIÓN DE LA OPCIÓN INTRODUCIDA
    # Evita accesos a apartados inexistentes
    if busqueda not in ['1', '2', '3','4','5','s','n','si','no','clientes','productos','ventas','empleados','provedores']:
        print(ROJO+'No existe el apartado que indicas'+RESET)

     # SALIDA DEL SISTEMA
    if busqueda == 's' or busqueda == 'si':
        break
    elif busqueda == 'n' or busqueda == 'no':
        pass


    # =========================
    # CLIENTES
    # =========================
    # Consulta de clientes por ID
    if busqueda == 'clientes' or busqueda == '1':
        id_cliente = int(input('Escribe el ID del cliente: '))

        if id_cliente in clientes:
            print(AMARILLO+'Nombre:'+RESET, clientes[id_cliente]['Nombre'])
            print(AMARILLO+'Apellido:'+RESET, clientes[id_cliente]['Apellido'])
            print(AMARILLO+'DNI:'+RESET, clientes[id_cliente]['DNI'])
            print(AMARILLO+'Num. Tel:'+RESET, clientes[id_cliente]['Num. Tel.'])
        else:
            print(ROJO+'No se encontro el cliente'+RESET)

    # =========================
    # PRODUCTOS
    # =========================
    # Consulta de productos por ID
    if busqueda == 'productos' or busqueda == '2':
        id_producto = int(input('ID del producto: '))

        if id_producto in productos:
            print(AMARILLO+'Producto:'+RESET, productos[id_producto]['Producto'])
            print(AMARILLO+'Precio:'+RESET, productos[id_producto]['Precio'])
            print(AMARILLO+'Stock:'+RESET, productos[id_producto]['Stock'])
        else:
            print(ROJO+ f'No se encontro el producto con ID {VERDE}{id_producto}{RESET}'+RESET)

    # =========================
    # VENTAS
    # =========================
    # Consulta de ventas por ID
    if busqueda == 'ventas' or busqueda == '3':
        id_venta = int(input('Introduzca el ID de la venta: '))

        if id_venta in ventas:
            print(AMARILLO+'Producto: '+RESET, ventas[id_venta]['Producto'])
            print(AMARILLO+'Precio: '+RESET, ventas[id_venta]['Precio'])
            print(AMARILLO+'Fecha de venta: '+RESET, ventas[id_venta]['Fecha de venta'])
        else:
            print(ROJO+ f'No se ha localizado ninguna venta con el ID {VERDE}{id_venta}{RESET}'+RESET)

    # =========================
    # PROVEEDORES
    # =========================
    # Consulta de proveedores por ID

    if busqueda == 'provedores' or busqueda == '4':
        id_provedores = int(input('Introduce el ID del provedor: '))

        if id_provedores in provedores:
            print(AMARILLO+'Provedor: '+RESET, provedores[id_provedores]['Provedor'])
            print(AMARILLO+'Precio: '+RESET, provedores[id_provedores]['Precios'])
            print(AMARILLO+'IVA: '+RESET, provedores[id_provedores]['IVA'])
        else:
            print(ROJO+ f'No se ha localizado ningun provedor con el ID{VERDE}{id_provedores}{RESET}'+RESET)

    # =========================
    # EMPLEADOS
    # =========================
    # Consulta de proveedores por ID

    if busqueda == 'empleados' or busqueda == '5':
        id_empleado = int(input('Introduzca la identificacion de el empleado: '))

        if id_empleado in empleados:
            print(AMARILLO+'Empleado: '+RESET, empleados[id_empleado]['Nombre'])
            print(AMARILLO+'ID: '+RESET, empleados[id_empleado]['ID'])
            print(AMARILLO+'DNI: '+RESET, empleados[id_empleado]['DNI'])
            print(AMARILLO+'Num. Tel: '+RESET, empleados[id_empleado]['Num. Tel.'])
        else: 
            print('El empleado no existe')
