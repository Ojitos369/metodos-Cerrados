#-----------  IMPORTACIONES ----------------
from src.extras import pausar,limpiar, convertir, convertirFloat
from src.operaciones import validarFuncion
#-----------  FUNCIONES ----------------
def principal():
    incorrecto = True
    while incorrecto:
        limpiar()
        print('https://github.com/Ojitos369/metodos-Cerrados.git')
        opc = input('''1.- Introducir ecuación
2.- Resolver por bifurcación
3.- Resolver por raphson
4.- Introducir Derivada
5.- Configurar aproximación
6.- Configurar numero de decimales
7.- Configurar Rangos
8.- Configurar inicial para Raphson
9.- Salir
Elige una opción: ''')
        opc = convertir(opc)
        if opc < 5 or opc > 0:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente. ')
            pausar()
    return opc

def aproximacion(texto):
    incorrecto = True
    while incorrecto:
        limpiar()
        opc = input(texto)
        opc = convertir(opc)
        if opc > 0:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente. ')
            pausar()
    return opc

def numero(texto):
    incorrecto = True
    while incorrecto:
        limpiar()
        opc = input(texto)
        opc = convertir(opc)
        if opc != 0:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente. ')
            pausar()
    return opc

def rangos():
    incorrecto = True
    while incorrecto:
        limpiar()
        menor = input('Ingrese el rango menor')
        menor = convertirFloat(menor)
        mayor = input('Ingrese el rango mayor')
        mayor = convertirFloat(menor)
        if mayor > menor:
            incorrecto = False
        else:
            print('El rango mayor debe ser mayor al rango menor')
            pausar()
    return [menor,mayor]

def pedir_funcion():
    permitidos = 'x/*0123456789+-^()'
    opc = ''
    incorrecto = True
    while incorrecto:
        incorrecto = False
        limpiar()
        opc = input('''Ingresa la función. Ejemplo: x^2+3(x-1)^3+5: \n''')
        
        for i in range (len(opc)):
            if opc[i] in permitidos:
                pass
            else:
                incorrecto = True
        #incorrecto = validarFuncion(opc)
        if incorrecto:
            print('No puedo resolver esa función de momento. Intenta con otra')
            pausar()
    return [True, opc]