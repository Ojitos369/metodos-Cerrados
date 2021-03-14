#-----------  IMPORTACIONES ----------------
from time import sleep
from src.menus import pausar
import src.menus as menus
from src.funcion import bifurcacion

#-----------  FUNCIONES ----------------

def main():
    mostrar_menu = True
    hay_funcion = True
    no_decimales = 5
    aproximacion = 10
    funcion = ''
    while mostrar_menu:
        opc = menus.principal()
        if opc != 5:
            if opc == 1:
                hay_funcion, funcion = menus.pedir_funcion()
            elif opc == 2:
                if hay_funcion:
                    bifurcacion(-50,50,aproximacion,funcion,no_decimales)
                    pausar()
                else:
                    print('Porfavor Ingresa primero una funcion')
                    pausar()
            elif opc == 3:
                texto = '''Ingresa el nivel de aproximación.
Entre mayor el numero, mayor la aporximación (Por defecto 10): '''
                aproximacion = menus.aproximacion(texto)
            elif opc == 4:
                texto = '''Ingresa el nivel de decimales (Por defecto 5): '''
                no_decimales = menus.aproximacion(texto)
        else:
            mostrar_menu = False
            print('Adios')
            sleep(.5)

#-----------  MAIN ----------------

if __name__ == "__main__":
    main()