#-----------  IMPORTACIONES ----------------
from time import sleep
from src.menus import pausar, limpiar
import src.menus as menus
from src.funcion import bifurcacion, raphson

#-----------  FUNCIONES ----------------

def main():
    mostrar_menu = True
    hay_funcion = True
    hay_derivada = True
    no_decimales = 5
    aproximacion = 10
    rango_menor = -50
    rango_mayor = 50
    inicial = 100
    funcion = '2x-3x^2+4'
    derivada = '2-6x'
    while mostrar_menu:
        opc = menus.principal()
        if opc != 9:
            if opc == 1:
                hay_funcion, funcion = menus.pedir_funcion()
            elif opc == 2:
                if hay_funcion:
                    bifurcacion(rango_menor,rango_mayor,aproximacion,funcion,no_decimales)
                    pausar()
                else:
                    print('Porfavor Ingresa primero una funcion')
                    pausar()
            elif opc == 3:
                if hay_funcion and hay_derivada:
                    limpiar()
                    print(f'Funcion: {funcion}')
                    print(f'Derivada: {derivada}')
                    raphson(funcion,derivada,aproximacion,no_decimales,inicial)
                    pausar()
                else:
                    print('Porfavor Ingresa primero una funcion y su derivada')
                    pausar()
            elif opc == 4:
                hay_derivada, derivada = menus.pedir_funcion()
            elif opc == 5:
                texto = '''Ingresa el nivel de aproximación.
Entre mayor el numero, mayor la aporximación (Por defecto 10): '''
                aproximacion = menus.aproximacion(texto)
            elif opc == 6:
                texto = '''Ingresa el nivel de decimales (Por defecto 5): '''
                no_decimales = menus.aproximacion(texto)
            elif opc == 7:
                rango_menor,rango_mayor = menus.rangos()
            elif opc == 8:
                texto = '''Ingresa inicial para Raphson (por defecto 100) '''
                inicial = menus.numero(texto)
        else:
            mostrar_menu = False
            print('Adios')
            sleep(.5)
            limpiar()

#-----------  MAIN ----------------

if __name__ == "__main__":
    main()